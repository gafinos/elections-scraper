"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Václav Špaček
email: gafinos@gmail.com
"""

import sys
import requests
import argparse
from  urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import re

# Set input arguments

# parser = argparse.ArgumentParser(
#     description="Program for scraping 2017 election results"
# )
# parser.add_argument('odkaz', help='URL volebních výsledků územnáho celku, např. https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103')
# parser.add_argument('jmeno_vystupu', help='Název výstupního CSV souboru')
# args = parser.parse_args()

# odkaz = args.odkaz
# jmeno_vystupu = args.jmeno_vystupu

odkaz= 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
jmeno_vystupu = 'prostejov.csv'

# def get okrsky links
okres = requests.get(odkaz).text
okres_parsed = bs(okres, features='html.parser')

obec_urls = [urljoin(odkaz, td.get("href")) for td in okres_parsed.select("td.cislo a")]

# def scrape okrsky
for obec_url in obec_urls:
    obec = requests.get(obec_url).text
    obec_parsed = bs(obec, features='html.parser')
    

    code = re.search(re.compile(r'obec=\d+'), obec_url).group()
    location = obec_parsed.find('h3', string=re.compile(r'Obec\.*')).text
    registered = obec_parsed.find('td', attrs = {'class': 'cislo', 'headers': 'sa2'}).text # remove whitespaces
    envelopes = obec_parsed.find('td', attrs = {'class': 'cislo', 'headers': 'sa5'}).text
    valid = obec_parsed.find('td', attrs = {'class': 'cislo', 'headers': 'sa6'}).text


    table1 = obec_parsed.find('td', {'class': 'overflow_name', 'headers': 't2sa1 t2sb2'}).parent.parent
    table2 = obec_parsed.find('td', {'class': 'overflow_name', 'headers': 't1sa1 t1sb2'}).parent.parent
    table_rows = table1.append(table2).find_all('tr')
    #def extract table data?

    parties = {}
    for tr in table_rows:
        party_name = tr.find('td', {'class': 'overflow_name'})
        party_votes = tr.find('td', {'class': 'cislo', 'headers': re.compile(r't\dsa\d t\dsb3')})
        if party_name is not None and party_votes is not None:
            parties[party_name.text] = party_votes.text






columns = ['code', 'location', 'registered', 'envelopes', 'valid']