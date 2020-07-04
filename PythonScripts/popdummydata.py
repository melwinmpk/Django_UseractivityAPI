import requests
import json

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/users/populateuser/"
post_headers = {
    "Content-Type": "application/json",
}
user_data = {
    "real_name": "TC02",
    "tz": "America/Los_Angeles"
}
user_data = {
    "id": "1"
}
get_method = requests.get(AUTH_ENDPOINT, data=json.dumps(
    user_data), headers=post_headers)
print(json.dumps(get_method.json(), indent=4, sort_keys=True))
