# Introduction to Data Wrangling

Data wrangling is a core skill that *everyone* who works with data should be familiar with since so much of the world's data isn't clean.

Though this course is geared towards those who use Python to analyze data, the high-level concepts can be applied in all programming languages and software applications for data analysis.


**Data Wrangling Setps:**
1. Gathering
2. Assessing
3. Cleaning

The goal of this walkthrough is awareness rather than mastery, so you'll be able to start wrangling your own data even after just this first lesson.
Data Wrangling Walkthrough Checklist


## A Definition

**wrangling** means to round up, herd, or take charge of livestock, like horses or sheep. Let's focus in on the sheep example.

A shepherd's main goals are to get their sheep to their pastures to let them graze, guide them to market to shear them, and put them in the barn to sleep. Before any of that though, they must be rounded up in a nice and organized group. The consequences if they're not? These tasks take longer. If they're all scattered, some could also run off and get lost. A wolf could even sneak into the pack and feast on a few of them.


## An Analogy

The same idea of organizing before acting is true for those who are shepherds of data. We need to wrangle our data for good outcomes, otherwise there could be consequences. If we analyze, visualize, or model our data before we wrangle it, our consequences could be making mistakes, missing out on cool insights, and wasting time. So best practices say wrangle. Always.

The development of Python and its libraries have made wrangling easier. In this course, you'll learn how to wrangle data like modern day data professionals.



## Best Practice: Downloading Files Programmatically

When downloading files from the internet, downloading can be done manually by clicking the download button (or sometimes right-clicking on a link and clicking "Save file as"). But best practice is actually to download files programmatically, i.e. with code, for two reasons: **scalability** and **reproducibility**.

- **Scalability**: Imagine you had a thousand files to download on a thousand different web pages, instead of just one. It'd take an eternity to point and click a thousand times. You can do the same with a few lines of code.

- **Reproducibility**: Someone, whether it's you or another person, is likely going to want to run your analysis later, so make downloading the dataset or datasets as easy on that person as possible. Reproducibility is also one of the main principles of the [scientific method](https://en.wikipedia.org/wiki/Scientific_method#Documentation_and_replication). You want to be able to prove to people that your analysis, visualization, etc. is legitimate. People need to know that given your data, your computational environment, your code, etc., that they can reproduce your results! Plus, the dataset or the web page it lives on may change, so if you include the date you downloaded the dataset, you give these future onlookers a chance to access archived copies of the dataset or at least understand why their results are different.



## Wrangling vs. EDA vs. ETL

At another point in the Data Analyst Nanodegree or if you're taking this course individually, another point in your data journey, you will encounter a topic called exploratory data analysis (EDA). If you've encountered EDA already you might be thinking: data wrangling seems very similar to exploratory data analysis. And that's because they are very similar and often get confused.

Here is one definition of EDA: *an analysis approach that focuses on identifying general patterns in the data, and identifying outliers and features of the data that might not have been anticipated.*

So where does **data wrangling** end and **EDA** start?

- **Data wrangling** - is about gathering the right pieces of data, assessing your data's quality and structure, then modifying your data to make it clean. But the assessments you make and convert to cleaning operations won't make your analysis, viz, or model better, though. The goal is to just make them possible, i.e., functional.

- **EDA** is about exploring your data to later augment it to maximize the potential of our analyses, visualizations, and models. When exploring, simple visualizations are often used to summarize your data's main characteristics. From there you can do things like remove outliers and create new and more descriptive features from existing data, also known as [feature engineering](https://en.wikipedia.org/wiki/Feature_engineering). Or detect and remove outliers so your model's fit is better.

In practice, wrangling and EDA can and often do occur together, but we're going to separate them for teaching purposes.

- **ETL** - You also may have heard of the [extract-transform-load process](https://en.wikipedia.org/wiki/Extract,_transform,_load) also known as ETL. ETL differs from data wrangling in three main ways:

1. The users are different
2. The data is different
3. The use cases are different

This article ([Data Wrangling Versus ETL: What’s the Difference?](https://tdwi.org/articles/2017/02/10/data-wrangling-and-etl-differences.aspx)) by Wei Zhang explains these three differences well.
---

# Data Wrangling Summary

1. Gather
2. Assess
3. Clean
4. Reassess and Iterate
5. Store (Optional)


### Gather

* Depending on the source of your data, and what format it's in, the steps in gathering data vary.
* High-level gathering process: obtaining data (downloading a file from the internet, scraping a web page, querying an API, etc.) and importing that data into your programming environment (e.g., Jupyter Notebook).


### Assess

**Assess data for:**

- *Quality*: issues with content. Low quality data is also known as **dirty data**.
- *Tidiness*: issues with structure that prevent easy analysis. Untidy data is also known as **messy data**.  

Tidy data requirements:

1. Each variable forms a column.
2. Each observation forms a row.
3. Each type of observational unit forms a table.


**Types of assessment:**

1. *Visual assessment*: scrolling through the data in your preferred software application (Google Sheets, Excel, a text editor, etc.).
2. *Programmatic assessment*: using code to view specific portions and summaries of the data (pandas' head, tail, and info methods, for example).


### Clean

**Types of cleaning:**

- Manual (not recommended unless the issues are single occurrences)
- Programmatic


**The programmatic data cleaning process:**

1. *Define*: convert our assessments into defined cleaning tasks. These definitions also serve as an instruction list so others (or yourself in the future) can look at your work and reproduce it.
2. *Code*: convert those definitions to code and run that code.
2. *Test*: test your dataset, visually or with code, to make sure your cleaning operations worked.

Always make copies of the original pieces of data before cleaning!


### Reassess and Iterate

After cleaning, always reassess and iterate on any of the data wrangling steps if necessary.


### Store (Optional)

Store data, in a file or database for example, if you need to use it in the future.
















## More Information

- [Wikipedia: Click-through rate (CTR)](https://en.wikipedia.org/wiki/Click-through_rate).
- [Charlie Park: Edward Tufte's "Slopegraphs"](http://charliepark.org/slopegraphs/).
- [David Venturi: This year’s Leafs offense is historically improved](http://bluesteam.hockey/this-years-leafs-offense-is-historically-improved/).
- [Lifewire: What Is a ZIP File?](https://www.lifewire.com/zip-file-2622675).
- [Jeff Knupp: Context Managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/) or [this](https://www.youtube.com/watch?v=-aKFBoZpiqA&ab_channel=CoreySchafer) YouTube video.
- [DigitalOcean: Aliasing Modules](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3#aliasing-modules).
- [Stack Overflow: Can you define aliases for imported modules in Python?](https://stackoverflow.com/questions/706595/can-you-define-aliases-for-imported-modules-in-python).
- [Wikipedia: Escape characters](https://en.wikipedia.org/wiki/Escape_character).
-
