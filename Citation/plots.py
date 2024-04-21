import json

import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import ast
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from pyparsing import anyOpenTag, anyCloseTag
from xml.sax.saxutils import unescape as unescape
import string
import pandas as pd
import matplotlib.pyplot as plot
#print(unescape_xml_entities(stripper.transformString(source)))
df = pd.read_csv(r"D:\\dissertation\\data\\profile_data_self_citations.csv",encoding='ISO-8859-1')
#df.plot(kind = 'scatter',		x = 'paper title',		y = '%',		color = 'red')
#df.plot.scatter(x='paper title',                      y='%',                      c='DarkBlue')
#plot.show(block=True);
#plot.xlim([0, 10])
#plot.savefig(r"D:\\dissertation\\data\\self_cit.png")
# set the title
#plt.title('ScatterPlot')

c=0
for i in range(len(df)):
    a = df.loc[i, '%age of self citations ']
    c=c+1
    try:
      if int(a)>100:
        print(c)
    except Exception: continue
# Import libraries using import keyword
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# plot the x and y using plot function
l = plt.plot(df.loc[i, 'total citations'],df.loc[i, '%age of self citations '])
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

fig,ax=plt.subplots(figsize=(10,6))

x=np.arange(1,38)

y=df.loc[i, 'total citations']
x=np.random.rand(len(y))
N=20

def bar(pos):
    pos = int(pos)
    ax.clear()
    if pos+N > len(x):
        n=len(x)-pos
    else:
        n=N
    X=x[pos:pos+n]
    Y=y[pos:pos+n]
    ax.bar(X,Y,width=0.7,align='edge',color='green',ecolor='black')

    for i,txt in enumerate(X):
       ax.annotate(txt, (X[i],Y[i]))

    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])

barpos = plt.axes([0.18, 0.05, 0.55, 0.03], facecolor="skyblue")
slider = Slider(barpos, 'Barpos', 0, len(x)-N, valinit=0)
slider.on_changed(bar)

bar(0)

plt.show()
# show the plot
#plt.show()
