<h1 align="center">Web Scrapping</h1>


# Introduction to HTML Parsing and HTTP Requests

This document serves as an introduction to web crawling, covering the basics of making HTTP requests and parsing HTML using Python. We will use the `requests` library to fetch web pages and `BeautifulSoup` to parse the HTML content.

## 📌 What is Web Scraping?

Web scraping involves:
- Sending a request to a website
- Receiving the HTML content of the web page
- Parsing and extracting the required information

## 🎯 Why is Web Scraping Important?
- ✅ Automate data collection from websites  
- ✅ Track changes in websites (price trackers, job listings, etc.)  
- ✅ Gather content for data analysis and machine learning  
- ✅ Competitive analysis in business 
## 🧰 Tools & Libraries in Python

| Library        | Use                                              |
|----------------|--------------------------------------------------|
| `requests`     | Send HTTP requests to web pages                  |
| `BeautifulSoup`| Parse and extract HTML content                   |
| `lxml`         | Fast XML/HTML parsing (alternative to BS)        |
| `Selenium`     | Automate browser (for JS-heavy pages)            |
| `pandas`       | Store and analyze extracted data                 |

## 1. HTTP Requests with `requests`

The `requests` library allows you to send HTTP requests easily. Below is a simple example of fetching a webpage.

```python
import requests

url = "https://example.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Success!")
    html_content = response.text
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
```

### Explanation

- `requests.get(url)`: Sends a GET request to the specified URL.
- `response.status_code`: Checks the HTTP status code.
- `response.text`: Contains the HTML content of the page.
## Please follow the link below to watch the entire video
  [![Watch on YouTube](https://img.youtube.com/vi/wCCC41lvMrU/maxresdefault.jpg)](https://www.youtube.com/watch?v=wCCC41lvMrU)

## 2. HTML Parsing with BeautifulSoup

Once the HTML is retrieved, we can parse and extract data using `BeautifulSoup`.

```python
from bs4 import BeautifulSoup

# Assuming html_content is obtained from the requests response
soup = BeautifulSoup(html_content, 'html.parser')

# Example: Extract the page title
title = soup.title.string
print(f"Page Title: {title}")

# Example: Find all hyperlinks
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

### Explanation

- `BeautifulSoup(html_content, 'html.parser')`: Parses the HTML.
- `soup.title.string`: Gets the content of the `<title>` tag.
- `soup.find_all('a')`: Finds all anchor tags (`<a>`).
- `link.get('href')`: Extracts the URL from each anchor tag.

## Summary

| Tool         | Purpose                            |
|--------------|------------------------------------|
| `requests`   | Send HTTP requests                 |
| `BeautifulSoup` | Parse and extract HTML content |

This forms the foundation of web crawling. The next step will include browser automation using Selenium for dynamic content.

---

> **Note:** Always respect the website's `robots.txt` file and terms of service when crawling.

