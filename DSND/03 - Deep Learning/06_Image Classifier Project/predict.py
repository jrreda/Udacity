# Imports here
import torch
import utils
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# define image path
try:
    image_path = str(input("What image dou want to predict it's name? \n >>> "))
except AttributeError:
    print("Image not exist!. Please try another path.\n >>> Ex:'flowers/train/1/image_06744.jpg'")


# read testloader & labels_map
_, _, _, testloader, cat_to_name = utils.load_datasets(data_dir='flowers', labels_map='cat_to_name.json', batch_size=64)

# Loading the checkpoint
model = utils.load_checkpoint('checkpoint.pth')

# make sure to use CPU insted of GPU
model.to('cpu')

# Make sure network is in eval mode for inference
model.eval()

# Freeze parameters so we don't backprop through them
for param in model.parameters():
    param.requires_grad = False

# preprossed image
img = utils.process_image(image_path)
tensor_img = img.unsqueeze_(dim=0).type(torch.FloatTensor)

# Calculate the class probabilities (softmax) for img
with torch.no_grad():
    output = model.forward(tensor_img)
    ps = torch.exp(output) # probablities
    top_p, top_classes = ps.topk(5, dim=1)
    # convert top_p, top_classes to list
    top_p, top_classes = list(top_p.numpy()[0]), list(top_classes.numpy()[0])


# Mapping index to class
mapping = {val: key for key, val in model.class_to_idx.items()}
top_classes = [mapping[item] for item in top_classes]
classes_names = [cat_to_name[item] for item in top_classes]



### Plotting reults
fig, (ax1, ax2) = plt.subplots(figsize=(5,6), nrows=2)

# plot Image
ax1.axis('off')
utils.imshow(utils.process_image(image_path))
ax1.set_title(classes_names[0])

# plot barchart - top classes
ax2.barh(classes_names, top_p)

# # show the 2 images
plt.show()

#### Testing your network
# load model, criterion, optimizer
_, criterion, _, _ = utils.build_model(arch="densenet121", hidden_layers=[1024, 512], output_layer=102, learning_rate=0.003, device="cpu")
utils.testing_network(model, criterion, testloader)
