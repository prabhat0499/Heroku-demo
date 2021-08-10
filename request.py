# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:14:56 2021

@author: Prabhat Dangi
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2,'interview_score':6})

print(r.json())