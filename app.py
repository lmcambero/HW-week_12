#!/usr/bin/env python
# coding: utf-8

# ### Dependencies

# In[11]:


from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars


# In[12]:


app = Flask(__name__)


# In[13]:


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# In[14]:


@app.route("/")
def home():

    nasa_mars = mongo.db.collection.find_one()

    return render_template("index.html", nasa_mars = nasa_mars)


# In[15]:


@app.route("/scrape")
def scrape():

    nasa_mars = mongo.db.collection
    mars_data = scrape_mars.scrape1()
    mars_data = scrape_mars.scrape2()
    mars_data = scrape_mars.scrape3()
    mars_data = scrape_mars.scrape4()
    mars_data = scrape_mars.scrape5()
    nasa_mars.update({}, mars_data, upsert=True)
    mongo.db.collection.update({}, mars_info, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




