# Deep Learning (PyTorch) Nanodegree

This repository contains material related to Udacity's [Deep Learning v7 Nanodegree program](https://www.udacity.com/course/deep-learning-nanodegree--nd101). It consists of a bunch of tutorial notebooks for various deep learning topics. In most cases, the notebooks lead you through implementing models such as convolutional networks, recurrent networks, and GANs. There are other topics covered such as weight initialization and batch normalization.

There are also notebooks used as projects for the Nanodegree program. In the program itself, the projects are reviewed by real people (Udacity reviewers), but the starting code is available here, as well.

## Table Of Contents

### Convolutional Neural Networks

* [Convolutional Neural Networks](https://github.com/jrreda/Udacity/tree/master/DLND/Convolutional%20Neural%20Networks%20PyTorch/convolutional-neural-networks): Visualize the output of layers that make up a CNN. Learn how to define and train a CNN for classifying [MNIST data](https://en.wikipedia.org/wiki/MNIST_database), a handwritten digit database that is notorious in the fields of machine and deep learning. Also, define and train a CNN for classifying images in the [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).
* [Transfer Learning](https://github.com/jrreda/Udacity/tree/master/DLND/Convolutional%20Neural%20Networks%20PyTorch/style-transfer). In practice, most people don't train their own networks on huge datasets; they use **pre-trained** networks such as VGGnet. Here you'll use VGGnet to help classify images of flowers without training an end-to-end network from scratch.
* [Weight Initialization](https://github.com/jrreda/Udacity/tree/master/DLND/Convolutional%20Neural%20Networks%20PyTorch/weight-initialization): Explore how initializing network weights affects performance.
* [Autoencoders](https://github.com/jrreda/Udacity/tree/master/DLND/Convolutional%20Neural%20Networks%20PyTorch/autoencoder): Build models for image compression and de-noising, using feedforward and convolutional networks in PyTorch.
* [Style Transfer](https://github.com/jrreda/Udacity/tree/master/DLND/Convolutional%20Neural%20Networks%20PyTorch/style-transfer): Extract style and content features from images, using a pre-trained network. Implement style transfer according to the paper, [Image Style Transfer Using Convolutional Neural Networks](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf) by Gatys et. al. Define appropriate losses for iteratively creating a target, style-transferred image of your own design!

### Recurrent Neural Networks

* [Intro to Recurrent Networks (Time series & Character-level RNN)](https://github.com/jrreda/Udacity/tree/master/DLND/Recurrent%20Neural%20Networks%20PyTorch/recurrent-neural-networks): Recurrent neural networks are able to use information about the sequence of data, such as the sequence of characters in text; learn how to implement these in PyTorch for a variety of tasks.
* [Embeddings (Word2Vec)](https://github.com/jrreda/Udacity/tree/master/DLND/Recurrent%20Neural%20Networks%20PyTorch/word2vec-embeddings): Implement the Word2Vec model to find semantic representations of words for use in natural language processing.
* [Sentiment Analysis RNN](https://github.com/jrreda/Udacity/tree/master/DLND/Recurrent%20Neural%20Networks%20PyTorch/sentiment-rnn): Implement a recurrent neural network that can predict if the text of a moview review is positive or negative.
* [Attention](https://github.com/jrreda/Udacity/tree/master/DLND/Recurrent%20Neural%20Networks%20PyTorch/Attention): Implement attention and apply it to annotation vectors.

### Generative Adversarial Networks

* [Generative Adversarial Network on MNIST](https://github.com/jrreda/Udacity/tree/master/DLND/Generative%20Adversarial%20Networks%20PyTorch/gan-mnist): Train a simple generative adversarial network on the MNIST dataset.
* [Batch Normalization](https://github.com/jrreda/Udacity/tree/master/DLND/Generative%20Adversarial%20Networks%20PyTorch/batch-norm): Learn how to improve training rates and network stability with batch normalizations.
* [Deep Convolutional GAN (DCGAN)](https://github.com/jrreda/Udacity/tree/master/DLND/Generative%20Adversarial%20Networks%20PyTorch/dcgan-svhn): Implement a DCGAN to generate new images based on the Street View House Numbers (SVHN) dataset.
* [CycleGAN](https://github.com/jrreda/Udacity/tree/master/DLND/Generative%20Adversarial%20Networks%20PyTorch/cycle-gan): Implement a CycleGAN that is designed to learn from unpaired and unlabeled data; use trained generators to transform images from summer to winter and vice versa.

### Projects

* [Predicting Bike-Sharing Patterns](https://github.com/jrreda/Udacity/blob/master/DLND/02%20Neural%20Networks/05_Project%20Predicting%20Bike%20Sharing%20Data/Your_first_neural_network_Solution.ipynb): Implement a neural network in NumPy to predict bike rentals.
* [Dog Breed Classifier](https://github.com/jrreda/Udacity/blob/master/DLND/03%20Convolutional%20Networks/dog_app.ipynb): Build a convolutional neural network with PyTorch to classify any image (even an image of a face) as a specific dog breed.
* [TV Script Generation](https://github.com/jrreda/Udacity/tree/master/DLND/project-tv-script-generation): Train a recurrent neural network to generate scripts in the style of dialogue from Seinfeld.
* [Face Generation](https://github.com/jrreda/Udacity/tree/master/DLND/project-face-generation): Use a DCGAN on the CelebA dataset to generate images of new and realistic human faces.

