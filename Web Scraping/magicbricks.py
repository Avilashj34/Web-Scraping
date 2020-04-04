from bs4 import BeautifulSoup
import requests

search = input("Search for")
param = {"proptype":search}