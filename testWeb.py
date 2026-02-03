import requests

# --- Configuration ---
SUBDOMAIN = "unity3d"
EMAIL = "leonardo.quinones@unity3d.com"
API_TOKEN = "ZLvf3vfZtgr8LZKU5mF0S3RKUVQsE2wXoJcJI4Yg"
TICKET_ID = 2991456

# --- Endpoint ---
url = f"https://{SUBDOMAIN}.zendesk.com/api/v2/tickets/{TICKET_ID}.json"

# --- Authentication ---
auth = (f"{EMAIL}/token", API_TOKEN)

# --- Request ---
response = requests.get(url, auth=auth)

# --- Handle response ---
if response.status_code == 200:
    ticket = response.json()["ticket"]
    print("Ticket ID:", ticket["id"])
    print("Subject:", ticket["subject"])
    print("Status:", ticket["status"])
    print("Requester ID:", ticket["requester_id"])
else:
    print("Error:", response.status_code)
    print(response.text)
