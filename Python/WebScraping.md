# Web Scraping Using Python

#### Author : Sudeshna Bora

Web Scraping is extraction of data from website. 

---

#### Libraries used 

1. <b>Requests</b>

This is used for http requests. 

2. <b>lxml</b>

HTML and XML parsing library

3. <b>Beautiful Soup</b>

Creates a tree parser of XML and HTML.
Can use ```lxml``` as underneath parser.

4. <b> Selenium </b>

Selenium web scraper for scraping non static (dynamic)
websites.

5. <b> Scrapy </b>

Web scraping framework.

---

#### Use Case 

Let us work out an example for understanding a simple web scraping
use case.

We have a [url](https://www.moneycontrol.com/financials/coalindia/cash-flowVI/CI11/1#CI11).

This url gives us the information of the cash flow of a company (Coal India)
in this matter. 
Moreover, this url provides we can go to previous cash flows and the only 
change in the url is the number in the last portion.

What we want to do is fetch all these url and scrape the table and store it in 
a single dataframe.

We will be using ```requests, lxml``` and ```beautiful soup```.

---

Let us focus on the logic we use for get the data 

First , we will get the web content. For that, we
use ```urlopen```

```python
from urllib.request import urlopen

fetched_url = urlopen(final_url).read()
```

```urlopen``` is a part of ```urllib``` package.

Only using ```urlopen()``` gives us a http request which can be used whereas using ```urlopen().read()```
gives us a byte stream of the website. 

Post getting the byte stream , we caste it to BeautifulSoup using ```lxml```
parser.

```python
soup = BeautifulSoup(fetched_url, 'lxml')
```

Now, on inspecting the webpage, we realised that the attribute we are interested in is 
```mctable1``` in the html tag ```table```.

We do this by using the function ```.find()```

```python
table = soup.find('table', attrs={'class':'mctable1'})
```

In case we want a check before fetching this we can use ```.find_all()```.

```python
tags = soup.find_all(attrs={'class':'mctable1'})
```

This gives us a ```resultset``` which we can verify as 

```python
tags.__len()__ == <Number
```

This basic steps help us achieve our use case. 

---








