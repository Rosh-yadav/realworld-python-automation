import os 
pcount= 0
counts={
   "Running": 0,
   "CrashLoopBackOff" : 0,
   "Pending": 0
   
}
unhealthy_pods = [ ]
name1 = [] 
with open( "pods.txt", "r") as file:
    output= file.readlines()
   
    for line in output[1:]:
        pcount+= 1
        if "Running" in line:
            counts["Running"]+= 1
        if "Pending" in line :
            counts["Pending"]+=  1
        if "CrashLoopBackOff" in line :
            counts["CrashLoopBackOff"]+= 1
        colums= line.split()
        pod_name = colums[1]
        pod_status= colums[3]
        
        if pod_status == "Pending" or pod_status == "CrashLoopBackOff":  
          unhealthy_pods.append(pod_name)
        
    for key, values in counts.items():
       line1= f"{key}: {values}"
       name1.append(line1)
 
    for pod in unhealthy_pods:
        print(pod)   
     

with open("report.txt" , "a")  as  result:  
        result.write("=============================\n")
        result.write ("Kubernetes Health Report\n")
        result.write("================================\n")
        result.write(f"Total Pods :{pcount}\n\n")
        for line3 in name1:
            result.write(line3 + "\n")
        result.write(f"\n")
        result.write("Unhealthy Pods\n ")
        result.write("-----------------\n")
        for pod in unhealthy_pods:
            result.write(pod + "\n")
    
     

    

    

     