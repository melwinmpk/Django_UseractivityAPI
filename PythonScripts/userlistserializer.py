import requests
import json

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/users/userlistserializers/"
'''
    User
    -> id (Primary)
    -> real_name (foreignkey)
    -> tz

    ActivityPeriod
    -> userid (foreign key)
    -> start_time
    -> end_time

'''
post_headers = {
    "Content-Type": "application/json",
}    
user_data = {
    "real_name": "TC02",
    "tz": "America/Los_Angeles"
}

post_method = requests.post(
    AUTH_ENDPOINT, data=json.dumps(user_data), headers=post_headers)
print(post_method.json())
user_data = {
    "id": "1"
}
get_method = requests.get(AUTH_ENDPOINT, data=json.dumps(
    user_data), headers=post_headers)
print(json.dumps(get_method.json(), indent=4, sort_keys=True))
