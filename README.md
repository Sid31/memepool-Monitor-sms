# memepool-Monitor-sms

## Overview
This script monitors the Bitcoin mempool and sends an SMS alert when the fee estimate for half-hour confirmation falls below a specified threshold. It uses the mempool.space API to fetch fee estimates and the Twilio API for sending SMS alerts.

## Features
- **Mempool Fee Monitoring**: Retrieves the current fee estimates for Bitcoin transactions.
- **Threshold-Based Alerts**: Sends an SMS when the half-hour fee estimate is below the user-defined threshold.
- **Time-based Monitoring**: Skips monitoring between 1 am and 8 am to avoid unnecessary checks during low-traffic hours.
- **Twilio SMS Integration**: Uses Twilio for reliable SMS notifications.

## Prerequisites
- Python 3.x
- `requests` library for API requests.
- `twilio` library for sending SMS messages.
- An account and API key from mempool.space.
- A Twilio account with an SID, Auth Token, and a Twilio phone number.

## Installation
1. Clone the repository: `git clone [repository-url]`.
2. Install required Python libraries: `pip install requests twilio`.

## Configuration
- Enter your Twilio credentials (`account_sid`, `auth_token`, `twilio_number`) and the recipient's phone number (`recipient_number`) in the script.
- Set the threshold for fee alerts in the script.

## Usage
Run the script with the command: `python mempool_monitor.py`.
The script will continuously monitor the mempool and send an SMS alert when conditions are met.

## Customization
- Adjust the time window for skipping checks as per your requirements.
- Modify the SMS message format and threshold in the script.
