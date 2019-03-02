from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from urllib.error import HTTPError
import sys
import json

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def main():
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # read settings file:
    with open('settings.json') as f:
        settings = json.load(f)
    time_zone = settings["time_zone"]
    minutes_between = int(settings["minutes_between"])
    h_time = int(settings["start_time"].split(':')[0])
    m_time = int(settings["start_time"].split(':')[1])
    calendar_id = settings["calendar_id"]

    # set insert day
    if settings["day"] is "today":
        start_time = datetime.datetime.utcnow()
        start_time = start_time.replace(hour=h_time, minute=m_time)
    elif settings["day"] is "tomorrow":
        start_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        start_time = start_time.replace(hour=h_time, minute=m_time)
    else:
        return("Insert day is not properly set, please check settings file.")

    try:
        f = open(sys.argv[1], 'r')
        line = f.readline()
        while line:
            line = line.split(';')
            summary = str(line[0])
            end_time = start_time + datetime.timedelta(minutes=int(line[-1]))
            event = {
                'summary': summary,
                'start': {
                    'dateTime': start_time.isoformat(),
                    'timeZone': time_zone,
                },
                'end': {
                    'dateTime': end_time.isoformat(),
                    'timeZone': time_zone,
                }
            }
            start_time = end_time + datetime.timedelta(minutes=minutes_between)
            service.events().insert(
                calendarId=calendar_id, body=event).execute()
            line = f.readline()
    except FileNotFoundError as fnf_er:
        print(fnf_er)
        print('file not found, check input file')
    except HTTPError as http_er:
        print(http_er)
        print('wrong input data')
    finally:
        f.close()


if __name__ == '__main__':
    main()
