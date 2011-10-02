# -*- coding: utf-8 -*-
import urllib2
import sys
import datetime
import os
import re
from time import sleep, mktime
from distutils import dir_util
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.twitter.models import Tweet
from lxml import etree

def to_datetime(d):
    bits = d.split(' ')
    month = bits[1]
    day = bits[2]
    time = bits[3]
    year = bits[5]
    
    month = month.replace('Jan', '01')
    month = month.replace('Feb', '02')
    month = month.replace('Mar', '03')
    month = month.replace('Apr', '04')
    month = month.replace('May', '05')
    month = month.replace('Jun', '06')
    month = month.replace('Jul', '07')
    month = month.replace('Aug', '08')
    month = month.replace('Sep', '09')
    month = month.replace('Oct', '10')
    month = month.replace('Nov', '11')
    month = month.replace('Dec', '12')
    
    d = '%s-%s-%s %s' % (year,month,day,time)
    
    return d


class Command(BaseCommand):
    #processed = 0
    count = 100
    
    def handle(self, *args, **kwargs):
        #api = twitter.Api(settings.)
        """
        'https://twitter.com/statuses/user_timeline/jamiecurle.xml?count=200'
        'https://twitter.com/statuses/user_timeline/jamiecurle.xml?max_id=107130422126841857'
        """
        hastag_re = re.compile('(\#[a-zA-Z0-9]+)')
        # get the last max_id
        last_id = Tweet.objects.order_by('-created')[0].twitter_id
        #
        url ='https://twitter.com/statuses/user_timeline/jamiecurle.xml?since_id=%s&count=%s' % (last_id, self.count)
        request = urllib2.urlopen(url)
        raw = request.read()
        tweets = etree.fromstring(raw)
        
        for tweet in tweets:
            try:
                t = Tweet.objects.get(twitter_id = tweet[1].text)
            except Tweet.DoesNotExist:
                t = Tweet()
                t.twitter_id = tweet[1].text
                t.created  = to_datetime(tweet[0].text)
                t.body = tweet[2].text
                t.is_favourite = True if tweet[5].text == 'true' else False
                t.reply_to_status_id = tweet[6].text
                t.reply_to_user_id  = tweet[7].text
                t.reply_to_user_name  = tweet[8].text
                t.retweet_count = tweet[9].text
                t.save()
            # process the hashtags
            for match in hastag_re.finditer(t.body):
                hashtag = match.group(0).replace('#', '')
                t.tags.add(hashtag)
            # feedback
            sys.stdout.write('.')
            sys.stdout.flush()
        # sleep for a second

