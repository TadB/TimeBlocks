from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from urllib.error import HTTPError
import sys

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

    # ustawienia:
    time_zone = 'Europe/Warsaw'
    minutes_between = 10

    start_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    start_time = start_time.replace(hour=8, minute=0)
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
            service.events().insert(calendarId='primary', body=event).execute()
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
