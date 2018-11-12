# # Alation API Connection Guide

# ## The following notebook the connection steps to the Alation API.
 
# Manual instructions to generate an API token:
     
#     Go to Admin -> Settings → Admin Settings → Misc. There's a button at the bottom that will generate an API token that needs to be saved somewhere so users can reference it.
     
#     NOTE: Whenever you generate a new API token, all previous tokens for that user are invalidated.

# import libraries
import requests
import json
from authData import *
from pprint import pprint

# username and password data
# NOTE: to avoid displaying personal information as raw text,
# you can add these data into a .py file (for this code it is authData.py)
data = {'username':USERNAME, 'password':PASSWORD}
# set up header with token
headers = {'Token':TOKEN}
# alation instance information
alationInstance = INSTANCE

# Get token for user
response = requests.get(alationInstance + 'integration/v1/article/', headers=headers)

# extract the response text
articles = json.loads(response.text)

# print result
pprint(articles[0])

