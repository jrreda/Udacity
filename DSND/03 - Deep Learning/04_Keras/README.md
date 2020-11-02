# Neural Networks in Keras

Luckily, every time we need to use a neural network, we won't need to code the activation function, gradient descent, etc. There are lots of packages for this, which we recommend you to check out, including the following:

* [Keras](https://keras.io/)  
* [TensorFlow](https://www.tensorflow.org/)  
* [Caffe](http://caffe.berkeleyvision.org/)  
* [Theano](http://deeplearning.net/software/theano/)  
* [Scikit-learn](http://scikit-learn.org/)  
* And many others!  

In this course, we will learn [Keras](https://keras.io/). Keras makes coding deep neural networks simpler. To demonstrate just how easy it is, you're going to build a simple fully-connected network in a few dozen lines of code.

The general idea for this example is that you'll first load the data, then define the network, and then finally train the network.


## Keras Optimizers

There are many optimizers in Keras, that we encourage you to explore further, in this [link](https://keras.io/optimizers/), or in this excellent [blog post](http://ruder.io/optimizing-gradient-descent/index.html#rmsprop). These optimizers use a combination of the tricks above, plus a few others. Some of the most common are:

### SGD

This is Stochastic Gradient Descent. It uses the following parameters:  

* Learning rate.  
* Momentum (This takes the weighted average of the previous steps, in order to get a bit of momentum and go over bumps, as a way to not get stuck in local minima).  
* Momentum (This slows down the gradient when it's close to the solution).  

### Adam

Adam (Adaptive Moment Estimation) uses a more complicated exponential decay that consists of not just considering the average (first moment), but also the variance (second moment) of the previous steps.

### RMSProp

RMSProp (RMS stands for Root Mean Squared Error) decreases the learning rate by dividing it by an exponentially decaying average of squared gradients. 
