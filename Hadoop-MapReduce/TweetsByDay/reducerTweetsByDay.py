#!/usr/bin/env python

from __future__ import division
import sys
# Reducer function calculates  average tweet count in a year for each day of the week
# and then gets the max from average
tweetCount = 0
totalDays = 52
tweetAvg = {}
day = None

for line in sys.stdin:
    (k, v) = line.strip().split('\t',1)
    if day != k:
        if day:
            tweetAvg[day] = tweetCount/totalDays
            print "Average Tweets on %s :\t%s" % (day, tweetAvg[day])
            tweetCount = 0
    day = k
    try:
        tweetCount += int(v)
    except:
        continue

tweetAvg[day] = tweetCount/totalDays
print "Average Tweets on %s :\t%s" % (day, tweetAvg[day])

print "Day of the week for bts tweets the most : ", max(tweetAvg, key=tweetAvg.get)
