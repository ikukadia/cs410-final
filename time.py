import datetime
import io
import json
from utils import get_participants, get_messages

def time_range_analysis(data, start, end):
    num_messages = {}
    for user in get_participants(data):
        num_messages[user] = 0
        for message in get_messages(data, user):
            hour = datetime.datetime.fromtimestamp(message["timestamp_ms"]/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f').split()[1].split(":")[0]
            if int(hour) >= start and int(hour) <= (end - 1):
                num_messages[user] += 1
    return num_messages

def init():
    with open('dont_commit.json') as file:
        data = json.load(file)
    return data


print(time_range_analysis(init(), 0, 5))



