#!/usr/bin/env python
# coding: utf-8

# ### Dependencies

# In[14]:

from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
from pprint import pprint

# In[15]:

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    nasa_mars = {}

# ### NASA Mars News

# In[16]:

def scrape1_info():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

# In[17]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

# In[18]:

    latest_title = soup.find("li", class_="slide").find("div", class_="content_title").text
    #latest_title

# In[19]:

    latest_p = soup.find("li", class_="slide").find("div", class_="article_teaser_body").text
    #print(latest_p)

    nasa_mars['latest_title'] = latest_title
    nasa_mars['latest_paragraph'] = latest_p

    return nasa_mars

    browser.quit()

# ### JPL Mars Space Images - Featured Image

# In[20]:

def scrape2_info():
    browser = init_browser()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)

# In[21]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

# In[22]:

    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    #featured_image_url

# In[23]:

    jpl_url = 'https://www.jpl.nasa.gov'
    featured_image_url = jpl_url + featured_image_url
    featured_image_url

    nasa_mars['featured_image_url'] = featured_image_url

    return nasa_mars

    browser.quit()

# ### Mars Weather

# In[24]:

def scrape3_info():
    browser = init_browser()

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(1)

# In[25]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

# In[26]:

    latest_tweet = soup .find('ol', class_='stream-items')
    mars_weather = latest_tweet.find('p', class_="TweetTextSize").text
    #print(mars_weather)

    nasa_mars['mars_weather'] = mars_weather

    return nasa_mars

    browser.quit()

# ### Mars Facts

# In[27]:

def scrape4_info():
    browser = init_browser()

    url = 'https://space-facts.com/mars/'

    time.sleep(1)

    table = pd.read_html(url)
    mars_df = table[1]
    mars_df.columns = ['description', 'value']
    mars_df.set_index('description', inplace = True)
    #mars_df

# In[28]:

    mars_html = mars_df.to_html()

    nasa_mars['mars_facts'] = mars_html

    return nasa_mars

    browser.quit()

# ### Mars Hemispheres

# In[29]:
def scrape5_info():
    browser = init_browser()

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(1)

# In[30]:

    image_urls = []

# In[31]:

    link = browser.find_by_css("a.product-item h3")
    for x in range(len(link)):
        hemisphere = {}
        
        browser.find_by_css("a.product-item h3")[x].click()
        
        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
        
        hemisphere["title"] = browser.find_by_css("h2.title").text
        
        image_urls.append(hemisphere)
        
        browser.back()

# In[32]:

    #print(image_urls)
    nasa_mars['hemispheres'] = image_urls
    
    return nasa_mars

    browser.quit()

# In[ ]:




