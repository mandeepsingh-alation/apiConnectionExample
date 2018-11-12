
# Alation API Connection Guide


## The following notebook the connection steps to the Alation API.

Manual instructions to generate an API token:
    
    Go to Admin -> Settings → Admin Settings → Misc. There's a button at the bottom that will generate an API token that needs to be saved somewhere so users can reference it.
    
    NOTE: Whenever you generate a new API token, all previous tokens for that user are invalidated.


```python
# import libraries
import requests
import json
from authData import *
from pprint import pprint
```


```python
# username and password data
data = {'username':USERNAME, 'password':PASSWORD}
# set up header with token
headers = {'Token':TOKEN}
# alation instance information
alationInstance = 'https://professionalsvcs.trialalation.com/'
```


```python
# Get token for user
response = requests.get(alationInstance + 'integration/v1/article/', headers=headers)
```


```python
# extract the response text
articles = json.loads(response.text)
```


```python
# print result
pprint(articles[0])
```

    {'attachments': [],
     'author': {'display_name': 'Rose Dore',
                'email': 'ak@alation.com',
                'id': 1,
                'url': '/user/1/',
                'username': 'ak@alation.com'},
     'body': '<p>Check out the <a data-oid="373" data-otype="article" '
             'href="/article/373/">Onboarding New Users</a> to start your journey. '
             'In the article, you will find information on the environment in '
             'general, background on the different datasets, and even a '
             'step-by-step workshop you can follow to get familiar with '
             'Alation.</p><p>Check out the <strong>Quick Start Tour\xa0'
             '</strong>model from the Help drop down menu located at the top right '
             'corner. A great way to learn different workflows.</p><p>If you are '
             'looking to learn about some of the use cases you might want to test '
             'in Alation, take a look at <a data-oid="374" data-otype="article" '
             'href="https://trialupdate2.trialalation.com/article/374/popular-use-cases">Popular '
             'Use Cases</a></p><p>In order to run queries against the two '
             'databases, <a data-oid="3" data-otype="data" '
             'href="/data/3/">Healthcare</a> and <a data-oid="9" data-otype="data" '
             'href="/data/9/">Education</a>, you will need database credentials. '
             'Please talk to your Alation rep for that information.\xa0</p>',
     'children': [{'id': 373,
                   'otype': 'article',
                   'title': 'Onboarding New Users',
                   'url': '/article/373/onboarding-new-users'}],
     'custom_fields': [],
     'custom_templates': [],
     'editors': [{'display_name': 'Steph',
                  'email': 'stephanie.yuen@alation.com',
                  'id': 69,
                  'url': '/user/69/',
                  'username': 'stephanie.yuen@alation.com'},
                 {'display_name': 'Ben Lumbert',
                  'email': 'ben.lumbert@alation.com',
                  'id': 70,
                  'url': '/user/70/',
                  'username': 'ben.lumbert@alation.com'},
                 {'display_name': 'GT Volpe',
                  'email': 'gianthomas.tewksbury@alation.com',
                  'id': 3,
                  'url': '/user/3/',
                  'username': 'gianthomas.tewksbury@alation.c'},
                 {'display_name': 'Rose Dore',
                  'email': 'ak@alation.com',
                  'id': 1,
                  'url': '/user/1/',
                  'username': 'ak@alation.com'}],
     'has_children': True,
     'id': 1,
     'private': False,
     'title': 'Welcome to Alation!',
     'ts_created': '2015-05-25T21:55:19.432085Z',
     'ts_updated': '2018-10-10T23:14:11.873013Z',
     'url': '/article/1/welcome-to-alation'}



```python

```
