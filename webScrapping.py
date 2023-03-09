import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import date
import re

regionData = {"PR" : "estado-pr"}

def findData(pages = 5, region = "PR"):
    pageSufix = "?o="
    regionData = {"PR" : "estado-pr"}
    for i in range(1, pages+1):
        urlOLX = "https://www.olx.com.br/autos-e-pecas/motos/"+regionData[region]+pageSufix+str(i)
        print(urlOLX)

findData()