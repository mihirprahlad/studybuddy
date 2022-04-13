import datetime
from datetime import timedelta
import pytz
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("credentials.json")
scoped_credentials = credentials.with_scopes(["https://www.googleapis.com/auth/calendar"])
CLIENT_SECRET_FILE = "credentials.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

start_datetime = datetime.datetime.now(tz=pytz.utc)
event = service.events().insert(calendarId='<YOUR EMAIL HERE>@gmail.com', body={
'summary': 'Foo',
'description': 'Bar',
'start': {'dateTime': start_datetime.isoformat()},
'end': {'dateTime': (start_datetime + timedelta(minutes=15)).isoformat()},
}).execute()

print(event)
request_body = {
    "summary": "Study Buddy Meetups"
}