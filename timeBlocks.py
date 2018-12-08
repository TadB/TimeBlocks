from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

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

    # Call the Calendar AP
    # now = datetime.datetime.utcnow().isoformat() + 'Z'
    # insert an default test event
    default_event = {
        'summary': 'event testowy ',
        'description': 'testowanie skryptu w python do automatyzacji \
                        dodawania nowych wydarzeń',
        'start': {
            'dateTime': '2018-12-09T09:00:00',
            'timeZone': 'Europe/Warsaw',
        },
        'end': {
            'dateTime': '2018-12-09T10:00:00',
            'timeZone': 'Europe/Warsaw',

        }
    }

    service.events().insert(calendarId='primary', body=default_event).execute()

    # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    # events_result = service.events().list(
    #     calendarId='primary', timeMin=now,
    #     maxResults=10, singleEvents=True,
    #     orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])


if __name__ == '__main__':
    main()
