Wow! That was a ton. We learned:


    1. How to set up hypothesis tests. You learned the **null hypothesis** is what we assume to be true before we collect any data, and the **alternative** is usually what we want to try and prove to be true.


    2. You learned about **Type I** and **Type II** errors. You learned that Type I errors are the worst type of errors, and these are associated with choosing the alternative when the null hypothesis is actually true.


    3. You learned that **p-values** are the probability of observing your data or something more extreme in favor of the *alternative* given the* null hypothesis* is true. You learned that using a confidence interval from the bootstrapping samples, you can essentially make the same decisions as in hypothesis testing (without all of the confusion of p-values).


    4. You learned how to make decisions based on **[p-values](https://rebeccaebarnes.github.io/2018/05/01/what-is-a-p-value)**. That is, if the p-value is less than your Type I error threshold, then you have evidence to reject the null and choose the alternative. Otherwise, you fail to reject the null hypothesis.


    5. You learned that when sample sizes are really large, everything appears **statistically significant** (that is you end up rejecting essentially every null), but these results may not **be practically significant**.


    6. You learned that when performing **multiple hypothesis tests**, your errors will compound. Therefore, using some sort of correction to maintain your true Type I error rate is important. A simple, but very conservative approach is to use what is known as a Bonferroni correction, which says you should just divide your α\alphaα level (or Type I error threshold) by the number of tests performed.