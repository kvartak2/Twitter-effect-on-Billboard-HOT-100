#!/usr/bin/env python

import json
import sys
import calendar
from datetime import datetime

filter_hashtag_mention = 'bts'

for line in sys.stdin:
    data = json.loads(line)
    if data.get('hastag_mentions').strip().lower() == filter_hashtag_mention:
        time = data.get('created_at')
        # splitting date to extract the day of the week tweet was made using datetime module
        date = datetime.strptime(time, '%a %b %d %H:%M:%S +0000 %Y')
        # this reuturns day of the week as integers Monday - Sunday [1 - 7], convert to string
        day = calendar.day_name[date.weekday()]
        print '%s\t%s' %(day, 1)
