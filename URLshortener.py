# Python URL Shortener

# Need requests library - "pip3 intall requests"
# Uses BILLY api

import request

# Account credentials
username = "REDACTED"
password = "REDACTED"

# Get access token using method to make POST request
initReq = request.post("https://api-ssl.bitly.com/oauth/authToken", auth = (username, password))

# On response OK, get token
if initReq.status_code == 200:
    authToken = initReq.content.decode()
    print("Success, authentication token: ", authToken)
else:
    print("Failure, cannot get authentication token, exiting...")
    exit()

# Construct request headers with authorization
headers = {"Authorization": f"Bearer {authToken}"}

# Get group UID associated with BILLY account
uidReq = requests.get("https://api-ssl.bitly.com/v4/groups", headers = headers)

# On response is OK, get GUID
if uidReq.status_code == 200:
    groupsData = uidReq.json()['groups'][0]
    guid = groupsData['guid']
else:
    print("Cannot get GUID, exiting...")
    exit()

# Request to shorten test URL
targetURL = "https://console.developers.google.com/projectselector2/support?supportedpurview=organizationId,project&orgonly=true"


# Make POST request to get shortened URL for our test url
finalReq = requests.post("https://api-ssl.bitly.com/v4/shorten",
                            json = {"group_guid": guid, "long_url": targetURL},
                            headers = headers)

# If response OK, get shortened URL
if finalReq.status_code == 200:
    link = finalReq.json().get("link")
    print("Shortened URL:", link)
    
# URL-Shortener
