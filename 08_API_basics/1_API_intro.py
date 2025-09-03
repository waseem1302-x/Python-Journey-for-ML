import requests


# test api

url = "https://fake-json-api.mock.beeceptor.com/users"

response = requests.get(url, timeout=5)

if response.status_code == 200:
    user = response.json()

    print("Success! Number of user fetched", len(user))

    first_user = user[0]
    print("\n First User Details:")
    print("ID:", first_user["id"])
    print("Name:", first_user["name"] )
    print("Email:",  first_user["email"])

else:
    print("Request Failed", response.status_code)