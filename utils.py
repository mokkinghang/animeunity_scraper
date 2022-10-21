from bs4 import BeautifulSoup
import requests, time
import pandas as pd
import numpy as np

def get_titles(soup):
    labels = soup.find_all("strong", class_="title")
    titles = [label.get_text().strip() for label in labels]
    return titles

def get_company_and_year(soup):
    labels = soup.find_all("div", class_="info-node-1")
    results = [label.get_text().strip() for label in labels]
    return results

def get_info(soup):
    labels = soup.find_all("div", class_="info-node-2")
    results = [label.get_text().strip() for label in labels]
    return results

def get_plot(soup):
    labels = soup.select("div[class*=\"plot\"]")
    results = [label.get_text().strip() for label in labels]
    return results

def get_genres(soup):
    labels = soup.select("div[class*=\"generi\"]")
    results_raw = [label.get_text().strip().split(',') for label in labels]
    results = [','.join([genre.strip() for genre in result]) for result in results_raw]
    return results

def get_links(soup):
    url_raw = 'https://www.animeunity.tv'
    anime_items = soup.select("div[class*=\"anime-item\"]")
    links = [url_raw+anime_item.find('a').get('href') for anime_item in anime_items]
    return links

def separate_company_and_year(string):
    split_string = string.split('•')
    if len(split_string) == 2:
        company = split_string[0]
        year = split_string[1]
    else:
        company = np.nan
        year = string
    return company, year

def separate_form_and_episodes(string):
    split_string = string.split('•')
    if len(split_string) == 2:
        form = split_string[0]
        episodes = split_string[1].strip('episodi').strip()
    else:
        form = np.nan
        episodes = string.strip('episodi').strip()
    return form, episodes

def get_anime_query_df(soup):
    anime_dict = dict()
    columns = ['Title', 'Year', 'Company', 'Form', 'Episodes', 'Genres', 'Link']
    for key in columns:
        anime_dict[key] = []
    anime_dict['Title'] = get_titles(soup)
    company_year_list = [separate_company_and_year(string) for string in get_company_and_year(soup)]
    companies, years = zip(*company_year_list)
    anime_dict['Company'] = companies
    anime_dict['Year'] = years
    form_episodes_list = [separate_form_and_episodes(string) for string in get_info(soup)]
    forms, episodes = zip(*form_episodes_list)
    anime_dict['Form'] = forms
    anime_dict['Episodes'] = episodes
    anime_dict['Genres'] = get_genres(soup)
    anime_dict['Link'] = get_links(soup)
    df = pd.DataFrame.from_dict(anime_dict)
    return df

def scroll_page_to_bottom(page, time_interval=1.5):
    page.evaluate(
    """
    var intervalID = setInterval(function () {
        var scrollingElement = (document.scrollingElement || document.body);
        scrollingElement.scrollTop = scrollingElement.scrollHeight;
    }, 200);

    """
    )
    prev_height = None
    scroll_count = 0
    while True:
        curr_height = page.evaluate('(window.innerHeight + window.scrollY)')
        if not prev_height:
            prev_height = curr_height
            time.sleep(time_interval)
        elif prev_height == curr_height:
            page.evaluate('clearInterval(intervalID)')
            break
        else:
            prev_height = curr_height
            time.sleep(time_interval)
        scroll_count += 1
        print("Scroll counts: {}".format(scroll_count))