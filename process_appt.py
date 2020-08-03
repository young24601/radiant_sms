import re
import datetime

d = datetime.datetime.now()

if 5 <= d.hour <= 11:
    time_of_day = "morning"
elif 11 < d.hour <= 16:
    time_of_day = "afternoon"
else:
    time_of_day = "evening"

when_is_appt = "tomorrow"

with open("/Volumes/public/Young/appt/2020_08_01.txt", "r") as f:
    appointments_raw = f.readlines()

message_list = {}

for line in appointments_raw:
    l = line.strip()
    try:
        firstname = re.search('\S+, (?P<firstname>\S+)', l)['firstname']
        appt_time = re.search('(?P<appt_time>\d+:\d+ \w\w)', l)['appt_time']
        phone_regex = re.search('\((\d{3})\)\s?(\d{3})-(\d{4})', l)
        phone_number = phone_regex[1] + phone_regex[2] + phone_regex[3]
    except:
        print(l)
        continue

    if phone_number in message_list:
        print(phone_number)
        print(f'We are also looking forward to taking care of {firstname} at {appt_time}.')

    else:
        message_list[phone_number] = f'Good {time_of_day} {firstname}, this is your dental office with a reminder that you have an appointment {when_is_appt} at {appt_time}. We look forward to taking care of you! 1721 Story Road.'
        print(phone_number)
        print(message_list[phone_number])
    print("------------------------")
