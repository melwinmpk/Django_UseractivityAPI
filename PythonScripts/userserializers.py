import requests
import json

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
headers = {
    "Content-Type": "application/json",
}



AUTH_ENDPOINT = "http://127.0.0.1:8000/api/users/userserializers/"

user_data = {
    "id":"8",
    "real_name": "TC0212345678",
    "tz": "America/Los_Angeles"
}

put_method = requests.put(
    AUTH_ENDPOINT, data=json.dumps(user_data), headers=headers)
print(put_method.json())


user_data = {
    "id": "8",
    "real_name": "TC0212345678",
    "tz": "America/Los_Angeles"
}

delete_method = requests.delete(
    AUTH_ENDPOINT, data=json.dumps(user_data), headers=headers)
print("Status Code for delete =>", delete_method.status_code)
