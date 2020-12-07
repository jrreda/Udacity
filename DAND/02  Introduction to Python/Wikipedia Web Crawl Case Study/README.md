# Automating the Wikipedia Crawl

Whilst it's interesting to click through Wikipedia, it takes a lot of time to click through and read all those articles. We're going to work on automating this process, ending up with a program that will go through Wikipedia for us, keeping track of the first links on each page and seeing where they lead. In order to do this, we'll need to find out about how web pages work and get to know some of the Python tools we can use to interact with the web and web content.



## Breaking the Problem into Steps

Now that we've explored the libraries we'll use to crawl Wikipedia, let's think about the steps our crawler program will execute. The manual process we followed was this:

1. Open an article
2. Find the first link in the article
3. Follow the link
4. Repeat this process until we reach the Philosophy article, or get stuck in an article cycle.

The key phrase in this process is **"Repeat"**. This four-step process is essentially a loop! If our program duplicates the manual process, our program will consist of one big loop.



## Pseudo Code

```py
page = a random starting page  
article_chain = []  
while title of page isn't 'Philosophy' and we have not discovered a cycle:  
    append page to article_chain  
    download the page content
    find the first link in the content
    page = that link
    pause for a second
```


## Resources

- If you're curious you can learn more about relative and absolute urls at the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL).
