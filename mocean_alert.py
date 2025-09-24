import requests
import json

# Your Mocean API Token
API_TOKEN = "apit-8dsY3YbOsASDLPitJ92vxSjdkU6ZYVAU-YQHRE"

def send_voice_alert(phone_number, message):
    url = "https://rest.moceanapi.com/rest/2/voice"

    # The Voice API requires a "command" JSON
    command = [
        {
            "action": "say",
            "text": message  # Message that will be read in the call
        }
    ]

    payload = {
        "mocean-to": phone_number,
        "mocean-command": json.dumps(command)  # Must be JSON string
    }

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)


# ✅ Test number from trial
send_voice_alert("+918825980971", "⚠️ Parkinson's Alert: Patient may need attention!")
