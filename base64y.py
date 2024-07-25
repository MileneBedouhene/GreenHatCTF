import requests
from time import sleep
array=[]
# Making a GET request
with open(r"C:\Users\milen\OneDrive\Desktop\base.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    array.append(line.replace("\n",""))


for ele in array:
    response = requests.get('http://greenhat.microclub.info:5626/'+ele)
    sleep(1)
    print(response.status_code)
    if response.status_code == 200:

        # Check the status code
        print(response.status_code)

        # Print the content of the response
        print(response.text)
        break
