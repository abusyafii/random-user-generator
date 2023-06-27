import requests

#Fetching data
r = requests.get("https://randomuser.me/api/")

#Accessing data
first_name = r.json()["results"][0]["name"]["first"]
last_name = r.json()["results"][0]["name"]["last"]
gender = r.json()["results"][0]["gender"]
dob = r.json()["results"][0]["dob"]["age"]
country = r.json()["results"][0]["location"]["country"]

#Printing the results
print(f"Name: {first_name} {last_name}")
print(f"Gender: {gender}")
print(f"Age: {dob}")
print(f"Country: {country}")