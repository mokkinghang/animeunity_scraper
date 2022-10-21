# Animeunity Scraper

Recently I have been learning Italian, so I watched some anime with Italian dub/sub in a site that I came across: https://www.animeunity.tv. I am interested to know which anime has both dub and sub versions, so I can compare the two versions. To achieve this task, I decided to scrape all animes on the Italian anime streaming site using Playwright in Python, and output a csv file so I can know which animes that contain the "(ITA)" keyword (dub version) also have a counterpart without this keyword (sub version). 

To run the code, first install the required packages:
```
pip install -r requirements.txt
```
You also have to install the Playwright browsers:
```
playwright install
```
Then simply run the code by the command
```
python scrape_animeunity.py
```
After about a minute, the scraping will be finished and you will have a csv file containing the information of all animes available on the site. The code should be easily generalizable to all sites that show further search results by scrolling.

An automatic anime downloader should be easy to write, since the download link is directly available for all episodes. I may do it later. 
