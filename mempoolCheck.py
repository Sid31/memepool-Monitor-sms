import requests
import time
from datetime import datetime
from twilio.rest import Client

def get_fee_estimates():
    response = requests.get('https://mempool.space/api/v1/fees/recommended')
    if response.status_code == 200:
        fees = response.json()
        return fees
    else:
        raise Exception('Failed to fetch fee estimates from mempool.space')

def send_twilio_message(body):
    # Use your actual Twilio credentials
    account_sid = ''  # Replace with your actual Twilio Account SID
    auth_token = ''    # Replace with your actual Twilio Auth Token
    twilio_number = ''  # Replace with your Twilio phone number
    recipient_number = ''  # Replace with the recipient's phone number

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=twilio_number,
        to=recipient_number
    )
    print(f"Message sent with SID: {message.sid}")


def monitor_fees(threshold):
    while True:
        # Get the current time
        current_time = datetime.now()
        # Check if the current time is between 1 am and 8 am
        if 1 <= current_time.hour < 8:
            print("Current time is between 1 am and 8 am. Skipping check.")
        else:
            try:
                fees = get_fee_estimates()
                print(f"Current half-hour fee estimate: {fees['halfHourFee']} sats/vbyte")
                
                if fees['halfHourFee'] < threshold:
                    print(f"Half-hour fee is below threshold: {fees['halfHourFee']} sats/vbyte")
                    # Here you would add your notification logic, e.g., send a message via Twilio API
                    send_twilio_message(f"Le sat sur la mempool est de : {fees['halfHourFee']} sats/vbyte. Va mint VIIIIIIIITTTE")
                    time.sleep(1800)
                    break
                else:
                    print("")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Wait for 10 minutes before checking again
        time.sleep(30)

# Start monitoring with a threshold of 35 sats/vbyte for half-hour confirmation
monitor_fees(threshold=33)
