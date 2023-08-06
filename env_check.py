import os

twilio_auth = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_sid = os.environ.get('TWILIO_ACCOUNT_SID')

if twilio_auth and twilio_sid:
    print("Environment variables are set correctly.")
else:
    print("Environment variables are not set or inaccessible.")
