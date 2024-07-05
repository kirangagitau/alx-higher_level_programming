# 0x11. Python - Network #1
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Introduction
urllib.request is a Python module for fetching URLs (Uniform Resource Locators). 
It offers a very simple interface, in the form of the urlopen function. 
This is capable of fetching URLs using a variety of different protocols. 
It also offers a slightly more complex interface for handling common situations - 
like basic authentication, cookies, proxies and so on. These are provided by 
objects called handlers and openers.

### Simplest way to use urllib

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
