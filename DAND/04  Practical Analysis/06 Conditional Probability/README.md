# Conditional Probability

In this lesson you learned about **conditional probability**. Often events are not independent like with coin flips and dice rolling. Instead, the outcome of one event depends on an earlier event.


For example, the probability of obtaining a positive test result is dependent on whether or not you have a particular condition. If you have a condition, it is more likely that a test result is positive. We can formulate conditional probabilities for any two events in the following way:  

``P(A∣B)=P(A ∩ B)P(B)P(A|B) = \frac{P(A\text{ }\cap\text{ }B)}{P(B)}P(A∣B)=P(B)P(A ∩ B)``  

In this case, we could have this as:  

```
P(positive∣disease)=P(positive ∩ disease)P(disease)P(positive|disease) = \frac{P(\text{positive }\cap\text{ disease})}{P(disease)}P(positive∣disease)=P(disease)P(positive ∩ disease)​
```

where `|` represents "given" and `∩\cap∩` represents "and".
