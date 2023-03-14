import requests
import time

# Define the endpoint URL
url = "https://api.datadoghq.com/api/v2/series"

# Define the headers to be sent
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "DD-API-KEY": "<Add API here>" 
}

counter =  100
timenow = int(time.time())


while(counter > 0):

    #Define the data to be sent
    data = {"series":[
    {
    "metric": "mitheysh.ldi.testing.again",
    "type": 1,
    "points":[
        {
            "timestamp": timenow,
            "value": 10
        }
    ],
    "tags": ["is_joke:definitely"]
    }]}

     # Send the POST request with headers and receive the response
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.content) 

    counter -= 1
    timenow -= 60  
