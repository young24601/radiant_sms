import re

time_of_day = "morning"
when_is_appt = "today"

with open("/Volumes/public/Young/appt/2020_07_10.txt", "r") as f:
    appointments_raw = f.readlines()

message_list = {}

for line in appointments_raw:
    l = line.strip()
    firstname = re.search('\S+, (?P<firstname>\S+)', l)['firstname']
    appt_time = re.search('(?P<appt_time>\d+:\d+ \w\w)', l)['appt_time']
    phone_regex = re.search('\((\d{3})\)\s?(\d{3})-(\d{4})', l)
    phone_number = phone_regex[1] + phone_regex[2] + phone_regex[3]

    if phone_number in message_list:
        print(phone_number)
        print(f'We are also looking forward to taking care of {firstname} at {appt_time}.')

    else:
        message_list[phone_number] = f'Good {time_of_day} {firstname}, this is your dental office with a reminder that you have an appointment {when_is_appt} at {appt_time}. We look forward to taking care of you! 1721 Story Road.'
        print(phone_number)
        print(message_list[phone_number])
    print("------------------------")