from playwright.sync_api import sync_playwright
import time
from utils import *

url = 'https://www.animeunity.tv/archivio'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent}

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
    user_agent=user_agent,
    )
    page = context.new_page()
    page.goto(url)
    scroll_page_to_bottom(page)
    html = page.content()
    browser.close()
    
soup = BeautifulSoup(html, 'html.parser')
df = get_anime_query_df(soup)
df.to_csv('animeunity.csv', index=False)
