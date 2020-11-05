# Imports here
import torch
import utils
import warnings
warnings.filterwarnings('ignore')



#### Create initials
# load dataloaders
train_dataset, trainloader, validloader, _, _ = utils.load_datasets(data_dir='flowers', labels_map='cat_to_name.json', batch_size=64)
# load model, criterion, optimizer
model, criterion, optimizer, device = utils.build_model(arch="densenet121", hidden_layers=[1024, 512], output_layer=102, learning_rate=0.003, device="cuda")
# for training loop: 
running_loss, steps = 0, 0
epochs = int(input('How many epochs do you want?...\n >>> '))  # 5 epochs
print_every = 40


# Train the classifier layers using backpropagation using the pre-trained network to get the features
for e in range(epochs):
    # Make sure training mode is on
    model.train()

    for images, labels in trainloader:
        steps += 1
        # Move input and label tensors to the default device
        images, labels = images.to(device), labels.to(device)

        # Forward pass
        logits = model.forward(images)
        loss = criterion(logits, labels)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # add the loss
        running_loss += loss.item()

        if steps % print_every == 0:
            # Make sure network is in eval mode for inference
            model.eval()

            # Turn off gradients for validation, saves memory and computations
            with torch.no_grad():
                valid_loss, accuracy = utils.network_validation(model, criterion, validloader)

            # print Inference
            print("Epoch: {}/{}.. ".format(e+1, epochs),
                  "Training Loss: {:.3f}.. ".format(running_loss/print_every),
                  "Validation Loss: {:.3f}.. ".format(valid_loss/len(validloader)),
                  "Validation Accuracy: {:.3f}".format(accuracy/len(validloader)))

            # Reset running_loss
            running_loss = 0

            # Make sure training mode is back on
            model.train()


# Save the checkpoint
checkpoint = {'layers': [1024, 512, 102],
              'lr': 0.003,
              'dropout': 0.2,
              'epochs': epochs,
              'structure': 'densenet121',
              'state_dict': model.state_dict(),
              'class_to_idx': train_dataset.class_to_idx,
              'classifier': model.classifier
              }

torch.save(checkpoint, 'checkpoint.pth')
