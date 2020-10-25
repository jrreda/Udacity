# Ensembles

This whole lesson (on ensembles) is about how we can combine (or ensemble) the models you have already seen in a way that makes the combination of these models better at predicting than the individual models.

Commonly the *"weak" learners* you use are decision trees. In fact the default for most ensemble methods is a decision tree in sklearn. However, you can change this value to any of the models you have seen so far.



## The goal of ensemble methods

is to combine the predictions of several base estimators built with a given learning algorithm in order to improve generalizability / robustness over a single estimator.  

Two families of ensemble methods are usually distinguished:  

1. In **averaging methods**, the driving principle is to build several estimators independently and then to average their predictions. On average, the combined estimator is usually better than any of the single base estimator because its variance is reduced.  

Examples: [Bagging methods](https://scikit-learn.org/stable/modules/ensemble.html#bagging), [Forests of randomized trees](https://scikit-learn.org/stable/modules/ensemble.html#forest), …  

2. By contrast, in **boosting methods**, base estimators are built sequentially and one tries to reduce the bias of the combined estimator. The motivation is to combine several weak models to produce a powerful ensemble.  

Examples: [AdaBoost](https://scikit-learn.org/stable/modules/ensemble.html#adaboost), [Gradient Tree Boosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting), …



## Why Would We Want to Ensemble Learners Together?

There are two competing variables in finding a well fitting machine learning model:  

* Bias  
* Variance  

It is common in interviews for you to be asked about this topic and how it pertains to different modeling techniques. As a first pass, [the wikipedia is quite useful](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). However, I will give you my perspective and examples:


### Bias:

When a model has high bias, this means that means it doesn't do a good job of bending to the data. An example of an algorithm that usually has high bias is linear regression. Even with completely different datasets, we end up with the same line fit to the data. When models have high bias, this is bad.

![Bias Vs Variance](https://github.com/jrreda/Udacity/blob/master/DSND/02%20-%20Supervised%20Learning/07_Ensemble%20Methods/images/anscombes-quartet-3.svg)


### Variance:

When a model has high variance, this means that it changes drastically to meet the needs of every point in our dataset. Linear models like the one above is low variance, but high bias. An example of an algorithm that tends to have a high variance and low bias is a decision tree (especially decision trees with no early stopping parameters). A decision tree, as a high variance algorithm, will attempt to split every point into it's own branch if possible. This is a trait of high variance, low bias algorithms - they are extremely flexible to fit exactly whatever data they see.



***High Bias, Low Variance*** models tend to *underfit* data, as they are not flexible. Linear models fall into this category of models.

***High Variance, Low Bias*** models tend to *overfit* data, as they are too flexible. Decision trees fall into this category of models.



## Introducing Randomness Into Ensembles

By combining algorithms, we can often build models that perform better by meeting in the middle in terms of bias and variance. There are some other tactics that are used to combine algorithms in ways that help them perform better as well. These ideas are based on minimizing bias and variance based on mathematical theories, like the central limit theorem.

![decision tree sketch](https://github.com/jrreda/Udacity/blob/master/DSND/02%20-%20Supervised%20Learning/07_Ensemble%20Methods/images/decision-tree-sketch.png)  

Another method that is used to improve ensemble methods is to introduce randomness into high variance algorithms before they are ensembled together. The introduction of randomness combats the tendency of these algorithms to overfit (or fit directly to the data available).  

There are two main ways that randomness is introduced:

1. **Bootstrap the data** - that is, sampling the data with replacement and fitting your algorithm and fitting your algorithm to the sampled data.

2. **Subset the features** - in each split of a decision tree or with each algorithm used an ensemble only a subset of the total possible features are used.

In fact, these are the two random components used in an algorithm called **random forests**.



## Techniques

You saw a number of ensemble methods in this lesson including:

* [BaggingClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier).  
* [RandomForestClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier).  
* [AdaBoostClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier).  

Another really useful guide for ensemble methods can be found **[in the documentation here](http://scikit-learn.org/stable/modules/ensemble.html)**. These methods can also all be extended to regression problems, not just classification.



## AdaBoost Hyperparameters

When we define the model, we can specify the hyperparameters. In practice, the most common ones are:  

* `base_estimator`: The model utilized for the weak learners (Warning: Don't forget to import the model that you decide to use for the weak learner).  
* `n_estimators`: The maximum number of weak learners used.



## Additional Resources on Boosting

1. [The original paper](https://cseweb.ucsd.edu/~yfreund/papers/IntroToBoosting.pdf) - A link to the original paper on boosting by Yoav Freund and Robert E. Schapire.

2. [An explanation about why boosting is so important](http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/) - A great article on boosting by a Kaggle master, Ben Gorman.

3. [A useful Quora post](https://www.quora.com/What-is-an-intuitive-explanation-of-Gradient-Boosting) - A number of useful explanations about boosting.
