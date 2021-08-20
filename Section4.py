#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:06:23 2021

@author: chiaweijie
"""

##Display a graph to show the number cases in Singapore over time 
import pandas as pd
import requests

URL = "https://api.covid19api.com/dayone/country/singapore/status/confirmed/live"

response = requests.get("https://api.covid19api.com/dayone/country/singapore/status/confirmed/live")
df= pd.read_json(response.text)

df.plot(x='Date', y='Cases')



