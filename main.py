"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Václav Špaček
email: gafinos@gmail.com
"""

import sys
import requests
import argparse

# Set input arguments

parser = argparse.ArgumentParser(
    description="Program for scraping 2017 election results"
)
parser.add_argument('odkaz', help='URL volebních výsledků územnáho celku, např. https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103', default='https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103') ## TODO remove default after testing
parser.add_argument('jmeno_vystupu', help='Název výstupního CSV souboru', default='prostejov.csv') ## TODO remove default after testing
args = parser.parse_args()

odkaz = args.odkaz
jmeno_vystupu = args.jmeno_vystupu

print(odkaz + jmeno_vystupu)