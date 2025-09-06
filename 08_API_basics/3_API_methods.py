# 3_API_methods.py
# Day 3: POST, PUT, PATCH, DELETE with APIs

import requests

# Fake API endpoint for posts
url = "https://jsonplaceholder.typicode.com/posts"

# Step 1: Create payload (data to send)
payload = {
    "userId": 1,
    "title": "My First API Post",
    "body": "Hello! This is created using Python requests."
}

# Step 2: Send POST request with JSON payload
resp = requests.post(url, json=payload, timeout=6)

print("POST Status:", resp.status_code)
print("Response JSON:", resp.json())

# Update post with id=1 (replace everything)
update_payload = {
    "id": 1,
    "userId": 1,
    "title": "Updated Title",
    "body": "This replaces the old post body."
}

resp = requests.put(f"{url}/1", json=update_payload, timeout=6)
print("\nPUT Status:", resp.status_code)
print("Updated Post:", resp.json())



# Update only one field (title) of post with id=1
patch_payload = {
    "title": "Patched Title Only"
}

resp = requests.patch(f"{url}/1", json=patch_payload, timeout=6)
print("\nPATCH Status:", resp.status_code)
print("Patched Post:", resp.json())



resp = requests.delete(f"{url}/1", timeout=6)
print("\nDELETE Status:", resp.status_code)  # usually 200 or 204
