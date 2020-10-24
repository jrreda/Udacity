# Building a Spam Classifier

Spam detection is one of the major applications of Machine Learning in the interwebs today. Pretty much all of the major email service providers have spam detection systems built in and automatically classify such mail as *'Junk Mail'*.   

In this mission we will be using the Naive Bayes algorithm to create a model that can classify **[dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)** SMS messages as spam or not spam, based on the training we give to the model. It is important to have some level of intuition as to what a **spammy** text message might look like. Usually they have words like ``'free', 'win', 'winner', 'cash', 'prize'`` and the like in them as these texts are designed to catch your eye and in some sense tempt you to open them. Also, spam messages tend to have words written in all capitals and also tend to use a lot of exclamation marks. To the recipient, it is usually pretty straightforward to identify a spam text and our objective here is to train a model to do that for us!  

Being able to identify spam messages is a binary classification problem as messages are classified as either 'Spam' or 'Not Spam' and nothing else. Also, this is a supervised learning problem, as we will be feeding a labelled dataset into the model, that it can learn from, to make future predictions.


## Overview

This project has been broken down in to the following steps:  

    - Step 0: Introduction to the Naive Bayes Theorem  

    - Step 1.1: Understanding our dataset  
    - Step 1.2: Data Preprocessing  

    - Step 2.1: Bag of Words (BoW)  
    - Step 2.2: Implementing BoW from scratch  
    - Step 2.3: Implementing Bag of Words in scikit-learn  

    - Step 3.1: Training and testing sets  
    - Step 3.2: Applying Bag of Words processing to our dataset.  

    - Step 4.1: Bayes Theorem implementation from scratch  
    - Step 4.2: Naive Bayes implementation from scratch  

    - Step 5: Naive Bayes implementation using scikit-learn  

    - Step 6: Evaluating our model  

    - Step 7: Conclusion    


***What does the term 'Naive' in 'Naive Bayes' mean ?***

The term *'Naive'* in Naive Bayes comes from the fact that the algorithm considers the features that it is using to make the predictions to be independent of each other, which may not always be the case. So in our Diabetes example, we are considering only one feature, that is the test result. Say we added another feature, 'exercise'. Let's say this feature has a binary value of `0` and `1`, where the former signifies that the individual exercises less than or equal to 2 days a week and the latter signifies that the individual exercises greater than or equal to 3 days a week. If we had to use both of these features, namely the test result and the value of the 'exercise' feature, to compute our final probabilities, Bayes' theorem would fail.  
Naive Bayes' is an extension of Bayes' theorem that assumes that all the features are independent of each other.  


## Naive Bayes Advantages

    1. Its ability to handle an extremely large number of features. In our case, each word is treated as a feature and there are thousands of different words.  
    2. It performs well even with the presence of irrelevant features and is relatively unaffected by them.  
    3. It has is its relative simplicity.  
    4. Naive Bayes' works well right out of the box and tuning it's parameters is rarely ever necessary, except usually in cases where the distribution of the data is known.  
    5. It rarely ever overfits the data.  
    6. Its model training and prediction times are very fast for the amount of data it can handle.  

All in all, Naive Bayes' really is a gem of an algorithm!
