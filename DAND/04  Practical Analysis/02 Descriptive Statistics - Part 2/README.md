# Descriptive Statistics - Part II
In this section, we learned about how **Inferential Statistics** differs from **Descriptive Statistics**.

## Table of contents

- [Measures of Spread](#mos)
- [Histograms](#hist)
- [The 5 Number Summary](#5ns)
- [Standard Deviation and Variance](#std)
- [Shape of The Distribution](#sod)
- [Outliers](#out)
- [Descriptive Statistics](#ds)
- [Inferential Statistics](#is)



## Measures of Spread <a name="mos"></a>

**Measures of Spread** are used to provide us an idea of how spread out our data are from one another. Common measures of spread include:

1. Range
2. Interquartile Range (IQR)
3. Standard Deviation
4. Variance



## Histograms <a name="hist"></a>

Histograms are super useful to understanding the different aspects of quantitative data. In the upcoming concepts, you will see histograms used all the time to help you understand the four aspects we outlined earlier regarding a quantitative variable:

- center
- spread
- shape
- outliers


## The 5 Number Summary <a name="5ns"></a>

The five number summary consist of 5 values:

1. **Minimum**: The *smallest* number in the dataset.
2. **Q1​**: The value such that *25%* of the data fall below.
3. **Q2​**: The value such that *50%* of the data fall below.
4. **Q3​**: The value such that *75%* of the data fall below.
5. **Maximum**: The *largest* value in the dataset.

Calculating each of these values was essentially just finding the median of a bunch of different dataset. Because we are essentially calculating a bunch of medians, the calculation depends on whether we have an odd or even number of values.

### Range:
**The range** is then calculated as the difference between the **maximum** and the **minimum**.

### IQR
The **interquartile range** is calculated as the difference between **Q3​** and **Q1​**.



## Standard Deviation and Variance <a name="std"></a>

- The **standard deviation** is one of the most common measures for talking about the spread of data.
- It is defined as the **average distance of each observation from the mean**.
- The **variance** is used to compare the spread of two different groups.
- A set of data with *higher variance* is more spread out than a dataset with *lower variance*. Be careful though, there might just be an outlier (or outliers) that is increasing the variance, when most of the data are actually very close.


### Important Final Points:
1. When comparing the spread between two datasets, the units of each must be the same.
2. When data are related to money or the economy, higher variance (or standard deviation) is associated with higher risk.
3. The standard deviation is used more often in practice than the variance, because it shares the units of the original dataset.



## Shape of The Distribution  <a name="sod"></a>

From a histogram we can quickly identify the shape of our data, which helps influence all of the measures we learned in the previous concepts. We learned that the distribution of our data is frequently associated with one of the three *shapes*:

1. Right-skewed
2. Left-skewed
3. Symmetric (frequently normally distributed)

Depending on the shape associated with our dataset, certain measures of center or spread may be better for summarizing our dataset.



## Outliers <a name="out"></a>

- We learned that *outliers* are points that fall very far from the rest of our data points.  
- This influences measures like the mean and standard deviation much more than measures associated with the five number summary.

### Identifying Outliers:
There are a number of different techniques for identifying outliers. A full paper on this topic is provided [here](http://d-scholarship.pitt.edu/7948/1/Seo.pdf). In general, I usually just look at a picture and see if something looks suspicious!


### Working With Outliers

When outliers are present we should consider the following points.

1. Noting they exist and the impact on summary statistics.
2. If typo - remove or fix
3. Understanding why they exist, and the impact on questions we are trying to answer about our data.
4. Reporting the 5 number summary values is often a better indication than measures like the mean and standard deviation when we have outliers.
5. Be careful in reporting. Know how to ask the right questions.


### Outliers Advice

Below are my guidelines for working with any column (random variable) in your dataset.

1. Plot your data to identify if you have outliers.
2. Handle outliers accordingly via the methods above.
3. If data follow a **normal distribution** (*no outliers*)- use the `mean` and `standard deviation` to describe your dataset, and report that the data are normally distributed.
4. If you have **skewed data** or **outliers**, use the `five number summary` to summarize your data and report the outliers.



## Descriptive Statistics <a name="ds"></a>

`Descriptive statistics` **is about describing our collected data** using the measures discussed throughout this lesson:  

- measures of center.  
- measures of spread.  
- shape of our distribution.  
- outliers.   

We can also use plots of our data to gain a better understanding.


## Inferential Statistics <a name="is"></a>

`Inferential Statistics` **is about using our collected data to draw conclusions to a larger population**. Performing inferential statistics well requires that we take a sample that accurately represents our population of interest.

A common way to collect data is via a survey. However, surveys may be extremely biased depending on the types of questions that are asked, and the way the questions are asked. This is a topic you should think about when tackling the first project.


We looked at specific examples that allowed us to identify the

- **Population** - our entire group of interest.
- **Parameter** - numeric summary about a population
- **Sample** - subset of the population
- **Statistic** - numeric summary about a sample
