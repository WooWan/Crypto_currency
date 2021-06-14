import time,json

from django.shortcuts import render
from pymongo import MongoClient
import datetime

class setimentalResult(object):
    def __init__(self):
        client = MongoClient("117.17.189.6", 27017)
        self.db = client['tweet']
        self.collection = self.db.kafka_tweet_2

    def get_users_from_collection(self):
        doc=self.collection.find({})
        return doc


def home(request):
    sentiment= setimentalResult()
    results= sentiment.get_users_from_collection()
    dateformat = "%Y-%m-%d %H:%M:%S"
    start_time = "2021-06-" + results[0]['created_at'][8:10] + " " + results[0]['created_at'][11:19]

    startTimestamp = time.mktime(datetime.datetime.strptime(start_time, dateformat).timetuple())
    count = 0
    result = []
    date=[]
    str_datetime = "2021-06-" + results[0]['created_at'][8:10] + " " + results[0]['created_at'][11:19]
    convert = datetime.datetime.strptime(str_datetime, dateformat)

    for tweet in results:
        str_datetime = "2021-06-" + tweet['created_at'][8:10] + " " + tweet['created_at'][11:19]
        convert = datetime.datetime.strptime(str_datetime, dateformat)
        if tweet['sent_result'] == 1.0:
            count += 1
        if convert >= datetime.datetime.fromtimestamp(startTimestamp + 900):
            # date.append(datetime.datetime.fromtimestamp(startTimestamp))
            # date.append(datetime.datetime.fromtimestamp(startTimestamp))
            date.append(startTimestamp)
            # datetime.datetime.fromtimestamp(startTimestamp)
            result.append(count)
            startTimestamp += 900
            count = 0
    return render(request, 'index.html', { "date" :date, "result": result})
#
#
# sentiment= setimentalResult()
# results= sentiment.get_users_from_collection()
# dateformat = "%Y-%m-%d %H:%M:%S"
# start_time = "2021-06-" + results[0]['created_at'][8:10] + " " + results[0]['created_at'][11:19]
# startTimestamp = time.mktime(datetime.datetime.strptime(start_time, dateformat).timetuple())
# count = 0
# result = []
# date=[]
# print(start_time)
# for tweet in results:
#     str_datetime = "2021-06-" + tweet['created_at'][8:10] + " " + tweet['created_at'][11:19]
#     convert = datetime.datetime.strptime(str_datetime, dateformat)
#     if tweet['sent_result'] == 1.0:
#         count += 1
#     if convert >= datetime.datetime.fromtimestamp(startTimestamp + 900):
#         date.append(startTimestamp)
#         result.append(count)
#         startTimestamp += 900
#         count = 0
# print(date[0])
# print(datetime.datetime.fromtimestamp(date[0]))
print(datetime.datetime.fromtimestamp(1623612625))
1623614425000
print(datetime.datetime.fromtimestamp(1623617125))
