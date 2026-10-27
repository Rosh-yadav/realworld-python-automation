import json
import os
import requests
report_entries= []
with open("services.json", "r") as file:
   #content= file.read()
   data =json.load(file)
   for j in data["services"]:
       name=j["name"]
       url= j["url"]
    
       try :  
         response= requests.get(url, timeout=3)
         if response.status_code== 200:
             status= "HEALTHY"
         else:
             status= "UNHEALTHY"   
        #  print(f"service :{name}")
         
        #  print(f"url : {url}")
        #  print(f"Status Code : {response.status_code}")
        #  print(f"Helath: {status}")
         
         report_entries.append(
             f"service : {name}\n"
             f"URL: {url}\n"
             f"Status_code: {response.status_code}\n"
             f"Health : {status}\n"   
         ) 
       except requests.exceptions.Timeout:
        report_entries.append(
        f"Service: {name}\n"
        f"URL: {url}\n"
        f"Health: TIMEOUT\n"
    )
       except requests.exceptions.RequestException as error:
        report_entries.append(
        f"Service: {name}\n"
        f"URL: {url}\n"
        f"Health: ERROR\n"
        f"Details: {error}\n"
    )  
with open("health.txt" , 'w') as report: 
          report.write("Deployment Health Check\n ")
          report.write("=================================\n")
          for r in report_entries:
              report.write(r + "\n")
