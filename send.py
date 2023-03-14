#This script will allow you send metrics to Datadog

import requests
import time

# Define the endpoint URL
url = "https://api.datadoghq.com/api/v2/series"

# Define the headers to be sent
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "DD-API-KEY": "<Add API here>" #You will need to add your own
}

numOfPoints =  100 #How many points do you want to send
startTime = int(time.time()) #Start time
interval = 60 #Set interval in seconds

#The while loop will keep send metrics into the past, with a specified interval (time)

#Default workflow will start to send 100 points into the past, starting now. 
#Each point sent will be seperated by a 60sec period from the previous

while(numOfPoints > 0):

    #Define the data to be sent
    data = {"series":[
    {
    "metric": "testing.late.metric.<your name>", #set your own metric name
    "type": 1,
    "points":[
        {
            "timestamp": startTime,
            "value": 10 #set your own metric value
        }
    ],
    "tags": ["is_bug_bashing:definitely"]
    }]}

     # Send the POST request with headers and receive the response
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code + " - "  + response.content)
    print() 

    numOfPoints -= 1
    startTime -= interval  
