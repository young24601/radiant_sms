import re
import datetime
import os
import glob

d = datetime.datetime.now()

if 5 <= d.hour <= 11:
    time_of_day = "morning"
elif 11 < d.hour <= 16:
    time_of_day = "afternoon"
else:
    time_of_day = "evening"

root = os.path.dirname(os.path.realpath(__file__)) + "/"
with open(root + "vars", "r") as vars:
    path_variable = vars.readline().strip()
    if path_variable.split()[0] == "latest":
        list_of_files = glob.glob(path_variable.split()[1] + "*") # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        path = latest_file
    else:
        path = path_variable
    when_is_appt = vars.readline().strip()

with open(path, "r") as f:
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
        message_list[phone_number] = f'Good {time_of_day} {firstname}, this is your dental office with a reminder that you have an appointment {when_is_appt} at {appt_time}. We look forward to taking care of you! We are located at 1721 Story Road.  Our phone number is 408-929-9977.'
        print(phone_number)
        print(message_list[phone_number])
    print("------------------------")
