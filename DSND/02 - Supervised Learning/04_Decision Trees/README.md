In this section you've learned all about decision trees, and how to use them to make predictions.


# Hyperparameters for Decision Trees

In order to create decision trees that will generalize to new problems well, we can tune a number of different aspects about the trees. We call the different aspects of a decision tree "hyperparameters". These are some of the most important hyperparameters used in decision trees:  

    1. **Maximum Depth**  

        The maximum depth of a decision tree is simply the largest length between the root to a leaf. A tree of maximum length `k` can have at most `2^k` leaves.  
        ![Maximum depth of a decision tree](https://github.com/jrreda/Udacity/tree/master/DSND/02%20-%20Supervised%20Learning/04_Decision%20Trees/maximum-depth.png)    


    2. **Minimum number of samples per leaf**  

        When splitting a node, one could run into the problem of having 99 samples in one of them, and 1 on the other. This will not take us too far in our process, and would be a waste of resources and time. If we want to avoid this, we can set a minimum for the number of samples we allow on each leaf.  

        ![Minimum number of samples per leaf](https://github.com/jrreda/Udacity/tree/master/DSND/02%20-%20Supervised%20Learning/04_Decision%20Trees/minimum-leaf-samples.png)  

        This number can be specified as an integer, or as a float. If it's an integer, it's the number of minimum samples in the leaf. If it's a float, it'll be considered as the minimum percentage of samples on each leaf. For example, 0.1, or 10%, implies that a cut will not be allowed if in one of the leaves there is less than 10% of the samples on that node.  


    3. **Minimum number of samples per split**  

        This is the same as the minimum number of samples per leaf, but applied on any split of a node.


    4. **Maximum number of features**  

        Oftentimes, we will have too many features to build a tree. If this is the case, in every split, we have to check the entire dataset on each of the features. This can be very expensive.   
        A solution for this is to limit the number of features that one looks for in each split.  
        If this number is large enough, we're very likely to find a good feature among the ones we look for (although maybe not the perfect one). However, if it's not as large as the number of features, it will speed up our calculations significantly.
