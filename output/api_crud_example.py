
import requests

# Data to create an item
data = {"name": "Item 1", "price": 10.99}

response = requests.post("http://localhost:5000/items", json=data)
print(response.json())

# Make a GET request to /items to read all items
response = requests.get("http://localhost:5000/items")
print(response.json())

# Make a GET request to /items/1 to read the item with ID 1
response = requests.get("http://localhost:5000/items/1")
print(response.json())

# Data to update an item
data_update = {"name": "Item 1 updated", "price": 9.99}

# Make a PUT request to /items/1 to update the item with ID 1
response = requests.put("http://localhost:5000/items/1", json=data_update)
print(response.json())

# Make a DELETE request to /items/1 to delete the item with ID 1
response = requests.delete("http://localhost:5000/items/1")
print(response.json())
