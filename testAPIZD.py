import base64
import os
import requests # You'll need to install this library: pip install requests

# Replace with your actual Zendesk email and API key
email = "leonardo.quinones@unity3d.com"
# It's best practice to store your API token securely, e.g., as an environment variable
# For this example, we'll use a placeholder, but in a real application, use os.getenv()
api_token = os.getenv("ZENDESK_API_KEY")
#api_token = "ZLvf3vfZtgr8LZKU5mF0S3RKUVQsE2wXoJcJI4Yg"
# Construct the combined string
#combined_str = f"{email}/token:{api_token}"
combined_str = f"{email}/token:{api_token}"

# Encode the string in Base64
encoded_bytes = base64.b64encode(combined_str.encode("utf-8"))
zd_base64_encoded_str = encoded_bytes.decode("utf-8")

# Prepare the Authorization header
headers = {
    "Authorization": f"Basic {zd_base64_encoded_str}",
    "Content-Type": "application/json"
}

# Example validation (optional)
if len(zd_base64_encoded_str) == 92:
    print('Zendesk validation OK')
else:
    print('Issues with Zendesk Token Validation')
