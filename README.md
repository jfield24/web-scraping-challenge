# Web Scraping of Mars and NASA Facts & Images

---

## Project Description
The purpose of this project was to scrape multiple websites to gather images and information about NASA and Mars, store it in a MongoDB database, and then using Flask, display it in a website - which the user can press a button to scrape new data.

---

## Sample website

![MissiontoMars](https://raw.githubusercontent.com/jfield24/web-scraping-challenge/main/Missions_to_Mars/Images/Webpage-Part-1.PNG)

![MarsHemispheres](https://raw.githubusercontent.com/jfield24/web-scraping-challenge/main/Missions_to_Mars/Images/Webpage-Part-2.png)


---

## Scraped URLs

- [NASA Mars News (text)](https://mars.nasa.gov/news/)
- [JPL Mars Space Images - Featured Image (image)](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
- [Mars Facts (table)](https://space-facts.com/mars/)
- [Mars Hemispheres (images)](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

---

## Necessary Steps to Run all the Project

1. Install or have installed these libraries in your Git Environment:
        -   pandas
        -   splinter
        -   bs4
        -   urllib.parse
        -   time
        -   flask
        -   flask_pymongo
2. Download or have downloaded the chromedriver.exe in the path "/usr/local/bin/chromedriver" for Mac Users
3. Run the `Mongo daemon`, in one terminal window run `~/mongodb/bin/mongod`. This will start the Mongo server.
4. Run the `\Missions_to_Mars\app.py` file
5. Open your browser and visit the URL: `http://127.0.0.1:5000/`

---
