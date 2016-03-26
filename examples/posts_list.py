#!/usr/bin/env python

"""
Mezzanine Client Example: List most recently published blog posts

See: https://github.com/gcushen/mezzanine-client-python

Notes:
- We assume OAuth app id and secret are provided via environment variables MN_ID and MN_SECRET.
- Alternatively, include them in a tuple below like: Mezzanine(('my_app_id', 'my_app_secret')).

Copyright (C) 2016 George Cushen.
License: https://github.com/gcushen/mezzanine-client-python/blob/master/LICENSE
"""

from mezzanine_client import Mezzanine
from mezzanine_client.utils import str_header, str_blue


# Initialise Mezzanine API client
api = Mezzanine()
published_posts = api.get_posts(page=1)

# Display results
print(str_header("The most recent blog posts are:"))
for post in published_posts:
    print(str_blue('{} (ID: {})'.format(post['title'], post['id'])))
