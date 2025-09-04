import requests
import json

url = "https://fake-json-api.mock.beeceptor.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    user_data = response.json()
    
    print("Success! Number of users fetched:", len(user_data))
    
    if len(user_data) >= 10:
        first_ten_users = user_data[:10]
        print("\nFirst 3 User Details:")
        for user in first_ten_users:
            print(json.dumps(user, indent=4))
    elif user_data:
        print("\nNot enough users returned to display the first 10. Showing all returned users:")
        print(json.dumps(user_data, indent=4))
    else:
        print("No users found in the response.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")