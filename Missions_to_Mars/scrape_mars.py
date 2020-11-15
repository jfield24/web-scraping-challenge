from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # NASA Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    slides = soup.find_all('li', class_='slide')
    news_title = slides[0].find('div', class_='content_title').text
    news_p = slides[0].find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    get_style = soup.find('article', class_='carousel_item')['style']
    break_url=get_style.split(':')
    break_url=break_url[1]
    break_url=break_url.split("'")
    image_url=break_url[1]

    base_url = "https://www.jpl.nasa.gov"
    featured_image_url = base_url + image_url

    # Mars Facts
    url = "https://space-facts.com/mars/"

    tables = pd.read_html(url)

    mars_facts_df = tables[0]
    mars_facts_df.columns = ['Description', 'Mars']
    mars_facts_df.set_index('Description', inplace=True)

    html_table = mars_facts_df.to_html()


    # Mars Hemispheres
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    base_url = "https://astrogeology.usgs.gov"
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    items = soup.find_all('div', class_='item')

    urls = []
    titles = []
    for item in items:
        urls.append(base_url + item.find('a')['href'])
        titles.append(item.find('h3').text)
    
    browser.visit(urls[0])
    html = browser.html
    soup = bs(html, 'html.parser')
    img_url = base_url+soup.find('img',class_='wide-image')['src']

    img_urls = []
    for img_url in urls:
        browser.visit(img_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = base_url+soup.find('img', class_='wide-image')['src']
        img_urls.append(img_url)
    
    hemisphere_image_urls = []
    for x in range(len(titles)):
        hemisphere_image_urls.append({'title':titles[x], 'img_url':img_urls[x]})

    # Creating the dictionary to hold all the scraped data
    mars = {}
    mars["news_title"] = news_title
    mars["news_p"] = news_p
    mars["featured_image_url"] = featured_image_url
    mars["mars_facts"] = html_table
    mars["hemisphere_image_urls"] = hemisphere_image_urls

    # Close the browser after scraping
    browser.quit()

    return mars

