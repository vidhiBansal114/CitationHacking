import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions()
b = webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver", chrome_options=options)
data = pd.read_csv("D:/dissertation/data/author id First 10.csv")
for i in range(len(data)) :
  print(data.iloc[i, 0], data.iloc[i, 1])