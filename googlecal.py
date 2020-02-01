from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import datefinder
import datetime
import pprint as pp 

scopes = ['https://www.googleapis.com/auth/calendar']

flow=InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()

pickle.dump(credentials, open("token.pkl", "wb")) 
credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
print(result)
calendar_id = result['items'][0]['id']
print()
print(result['items'][0])


def create_event(start_time_str, summary, duration=1,attendees=None, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + datetime.timedelta(hours=duration)
                
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': datetime.timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': datetime.timezone,
        },
        'attendees': [
        {'email':attendees },
    ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    pp.pprint('''*** %r event added: 
    With: %s
    Start: %s
    End:   %s''' % (summary.encode('utf-8'),
        attendees,start_time, end_time))
        
    return service.events().insert(calendarId='primary', body=event,sendNotifications=True).execute()

create_event('24 Jul 12.30pm', "Test Meeting using CreateFunction Method",0.5,"mhcalendarscheduling@gmail.com","Test Description","Mentone, VIC,Australia")