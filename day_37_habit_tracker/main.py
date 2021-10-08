import requests
from datetime import datetime

USERNAME = "btwmendes"
# TOKEN = "zmxncbvv"
pixela_endpoint = "https://pixe.la/v1/users"

# ------------------STEP 1: Create you user account-----------------
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ------------------STEP 2: Create a graph definition-----------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# ------------------STEP 3: Get the graph-----------------
# https://pixe.la/v1/users/btwmendes/graphs/graph1.html

# ------------------STEP 4: Post value to the graph-----------------
pixel_creation_endpoint = f"{graph_endpoint}/graph1"

# today = datetime.now()
today = datetime(year=2021, month=10, day=5)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# ------------------STEP 5: Update a pixel-----------------

update_date = "20211007"
pixel_update_endpoint = f"{pixel_creation_endpoint}/{update_date}"

pixel_update_params = {
    "quantity": "33"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

# ------------------STEP 6: Delete a pixel-----------------
delete_pixel_endpoint = pixel_update_endpoint

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)