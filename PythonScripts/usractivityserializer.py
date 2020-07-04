import requests
import json

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/users/usractivityserializers/"
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
user_data = {
    "id": "101",
    "userid": "90",
    "start_time": "Feb 15 2020  1:33PM",
	"end_time": "Feb 15 2020 1:54PM"
}

post_method = requests.put(
    AUTH_ENDPOINT, data=json.dumps(user_data), headers=headers)

print(post_method.json())


user_data = {
    "id": "101"
}

delete_method = requests.delete(
    AUTH_ENDPOINT, data=json.dumps(user_data), headers=headers)
print("Status Code for delete =>", delete_method.status_code)
