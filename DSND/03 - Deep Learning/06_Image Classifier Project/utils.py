# Imports here
import numpy as np
np.random.seed(42)
import torch
from torch import nn, optim
from torchvision import datasets, transforms, models
import json
from PIL import Image
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



#### Loading the data
def load_datasets(data_dir='flowers', labels_map='cat_to_name.json', batch_size=64):
    '''Define tansormations, load the dataset with ImageFolder and labels_file, define the dataloaders.
    Returns:
        train_dataset, trainloader, validloader, testloader & labels_file
    '''
    # define train, valid & test directories
    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'
    test_dir = data_dir + '/test'

    # Define your transforms for the training, validation, and testing sets
    data_transforms = {'train_transforms': transforms.Compose([transforms.Resize(255),
                                                               transforms.CenterCrop(224),
                                                               transforms.RandomHorizontalFlip(),
                                                               transforms.RandomRotation(30),
                                                               transforms.ToTensor(),
                                                               transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                                               ]),
                       'valid_test_transforms': transforms.Compose([transforms.Resize(255),
                                                                    transforms.CenterCrop(224),
                                                                    transforms.ToTensor(),
                                                                    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                                                    ]),
                      }
    # Load the datasets with ImageFolder
    image_datasets = {'train_dataset': datasets.ImageFolder(train_dir, transform=data_transforms['train_transforms']),
                      'valid_dataset': datasets.ImageFolder(valid_dir, transform=data_transforms['valid_test_transforms']),
                      'test_dataset': datasets.ImageFolder(test_dir, transform=data_transforms['valid_test_transforms'])}
    # Using the image datasets and the trainforms, define the dataloaders
    dataloaders = {'trainloader': torch.utils.data.DataLoader(image_datasets['train_dataset'], batch_size, shuffle=True),
                   'validloader': torch.utils.data.DataLoader(image_datasets['valid_dataset'], batch_size),
                   'testloader': torch.utils.data.DataLoader(image_datasets['test_dataset'], batch_size)}
    train_dataset, trainloader, validloader, testloader = image_datasets['train_dataset'], dataloaders['trainloader'], dataloaders['validloader'], dataloaders['testloader']
    # Label mapping
    with open(labels_map, 'r') as f:
        cat_to_name = json.load(f)
    # return dataloaders and labels_file
    return train_dataset, trainloader, validloader, testloader, cat_to_name



#### Building and training the classifier
def build_model(arch="densenet121", hidden_layers=[1024, 512], output_layer=102, learning_rate=0.003, device="cuda"):
    '''return a pretrained model with the specified classifier.
    '''
    # Try to create a model from torchvision.models subpackage
    try:
        model = eval("models." + arch +"(pretrained=True)")
    except AttributeError:
        print("Model not available. Please try another architecture. Ex:'densenet121'")
        return None
    # Freeze parameters so we don't backprop through them
    for param in model.parameters():
        param.requires_grad = False
    # Define a new, untrained feed-forward network as a classifier, using ReLU activations and dropout
    classifier = nn.Sequential(nn.Linear(hidden_layers[0], hidden_layers[1]),
                               nn.ReLU(),
                               nn.Dropout(0.2),
                               nn.Linear(hidden_layers[1], output_layer),
                               nn.LogSoftmax(dim=1))
    # Assign the classifier to the Pre-trained model
    model.classifier = classifier
    # Define the criterion
    criterion = nn.NLLLoss()
    # Only train the classifier parameters, feature parameters are frozen
    optimizer = optim.Adam(model.classifier.parameters(), lr=0.003)
    # Use GPU if it's available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # Return the structured model
    return model.to(device), criterion, optimizer, device



#### Create a validation function
def network_validation(model, criterion, validloader):
    '''See how the model doing on the validation set.
    returns:
        loss, accuracy
    '''
    loss, accuracy = 0, 0
    for images, labels in validloader:
        # Move input and label tensors to the default device
        images, labels = images.to("cuda" if torch.cuda.is_available() else "cpu"), labels.to("cuda" if torch.cuda.is_available() else "cpu")
        output = model(images)
        loss += criterion(output, labels).item()
        # calcutate Accuracy
        ps = torch.exp(output) # probablities
        top_p, top_class = ps.topk(1, dim=1)
        equality = (top_class == labels.view(*top_class.shape))
        accuracy += equality.type(torch.FloatTensor).mean()
        # return loss & accuracy
    return loss, accuracy



#### Testing your network
def testing_network(model, criterion, testloader):
    '''See how the model doing on the test set.
    returns:
        loss, accuracy in %
    '''
    # Use GPU
    model.to("cuda" if torch.cuda.is_available() else "cpu")
    # Make sure network is in eval mode for inference
    model.eval()
    # Turn off gradients for validation, saves memory and computations
    with torch.no_grad():
        test_loss, accuracy = network_validation(model, criterion, testloader)
    # print Inference
    print("Test Loss: {:.3f}.. ".format(test_loss/len(testloader)),
          "Test Accuracy: {:.3f} %".format(accuracy/len(testloader)*100))


#### Loading the checkpoint
def load_checkpoint(filepath):
    '''load the checkpoint saved in train.py
    Returns:
        loaded model from train.py
    '''
    #loading checkpoint from a file
    checkpoint = torch.load(filepath)
    # load the model and its specifications
    model = models.densenet121(pretrained=True)
    model.classifier = checkpoint['classifier']
    model.class_to_idx = checkpoint['class_to_idx']
    model.load_state_dict(checkpoint['state_dict'])
    # return the model
    return model


#### Image Preprocessing
def process_image(image):
    '''
    Scales, crops, and normalizes a PIL image for a PyTorch model.
    returns:
        an Numpy array
    '''
    # Process a PIL image for use in a PyTorch model
    transformations = transforms.Compose([transforms.Resize(255),
                                         transforms.CenterCrop(224),
                                         transforms.ToTensor(),
                                         transforms.Normalize([0.485, 0.456, 0.406],
                                                              [0.229, 0.224, 0.225])
                                         ])
    # return the preprossed image ready for PyTorch model
    return transformations(Image.open(image))


#### create a Visualization function
def imshow(image, ax=None, title=None):
    """Imshow for Tensor.
    Example:
        imshow( process_image('/flowers/train/1/image_06744.jpg') )
    """
    if ax is None:
        fig, ax = plt.subplots()
    # PyTorch tensors assume the color channel is the first dimension
    # but matplotlib assumes is the third dimension
    image = image.numpy().transpose((1, 2, 0))
    # Undo preprocessing
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    image = std * image + mean
    # Image needs to be clipped between 0 and 1 or it looks like noise when displayed
    image = np.clip(image, 0, 1)
    ax.imshow(image)
    # return the image
    return ax
