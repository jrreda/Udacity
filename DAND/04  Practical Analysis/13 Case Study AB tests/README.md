# Case Study: A/B tests

In this case study, you'll apply what you've learned on confidence intervals and hypothesis testing to help a company decide whether to launch two new features on their website. To do this, you'll analyze results from A/B testing, a valuable and widely practiced method in industry.  


## A/B tests usage

A/B tests are used to test changes on a web page by running an experiment where a **control group** sees the old version, while the **experiment group** sees the new version. A **metric** is then chosen to measure the level of engagement from users in each group. These results are then used to judge whether one version is more effective than the other. A/B testing is very much like hypothesis testing with the following hypotheses:  

* **Null Hypothesis**: The new version is no better, or even worse, than the old version.  
* **Alternative Hypothesis**: The new version is better than the old version.

If we fail to reject the null hypothesis, the results would suggest keeping the old version. If we reject the null hypothesis, the results would suggest launching the change. These tests can be used for a wide variety of changes, from large feature additions to small adjustments in color, to see what change maximizes your metric the most.


## A/B tests drawbacks

**A/B testing** also has its drawbacks. It can help you compare two options, but it can't tell you about an option you haven’t considered. It can also produce bias results when tested on existing users, due to factors like change aversion and novelty effect.  

* **Change Aversion**: Existing users may give an unfair advantage to the old version, simply because they are unhappy with change, even if it’s ultimately for the better.  
* **Novelty Effect**: Existing users may give an unfair advantage to the new version, because they’re excited or drawn to the change, even if it isn’t any better in the long run.  



## steps we took to analyze the results of this A/B test  

1. We computed the **observed difference** between the metric, click through rate, for the control and experiment group.  
2. We simulated the **sampling distribution** for the difference in proportions (or difference in click through rates).  
3. We used this sampling distribution to simulate the **distribution under the null** hypothesis, by creating a random normal distribution centered at *0* with the same spread and size.  
4. We computed the **p-value** by finding the proportion of values in the null distribution that were greater than our observed difference.  
5. We used this p-value to determine the **statistical significance** of our observed difference.  



## Difficulties in A/B Testing  

Being able to determine the statistical significance of performance differences in A/B test results is valuable. However, there are many other factors to consider to ensure your A/B tests are successful. In the real world, designing, running, and drawing conclusions from an A/B test to lead you to the right decisions can be tricky.
