import os 
from datetime import datetime
error_log= []
counts={
    
    "INFO" : 0,
    "WARNING": 0,
    "ERROR" : 0,
    "CRITICAL":0
}
total_count=0
error_counts= {}
max_count= 0 
most_error= "NO Error Found"

with open("server.log","r") as log:
    file= log.readlines()
    for logfile in file:
        
        column= logfile.split()
        if len(column)< 3:
            continue
        print(column)
        total_count+=1
        status= column[2]
        if status == "INFO":
         counts["INFO"]+= 1
        elif status== "ERROR" :
            counts["ERROR"]+= 1
            error_msg= " ".join(column[3:])
            error_log.append(error_msg)
        elif status== "WARNING" :
            counts["WARNING"]+= 1
        elif status== "CRITICAL":
            counts["CRITICAL"]+= 1
        else:
            print("No such logs founds ")   
    
print(error_log)
for file_error in error_log:
    if file_error in error_counts:
        error_counts[file_error]+= 1
    else :
        error_counts[file_error]= 1
for key, value in error_counts.items():
         oocured=(f"{key} : {value}")
         if value> max_count:
          max_count= value
          most_error= key
        
   
current_time= datetime.now().strftime("%d-%m-%y %H_%M")
report= current_time + ".txt"
with open(report , "w") as report:
    report.write("================================================================\n")
    report.write("Production Server Log Report\n")
    report.write("==================================================================\n")
    report.write("Generated At\n")
    report.write(f"{current_time}\n")
    report.write("\n")
    report.write(f"Total Logs :{total_count}\n")
    report.write(f"INFO : {counts["INFO"]}\n")
    report.write(f"WARNING : {counts["WARNING"]}\n")
    report.write(f"ERROR : {counts["ERROR"]}\n")
    report.write(f"CRITICAL : {counts['CRITICAL']}\n")
    report.write(f"-----------------------------------------------------------------------\n")
    report.write("Most Frequent Error\n\n")
    report.write(f"{most_error} : {max_count}\n")
    report.write("\n")
    report.write("Status\n")
    if counts["ERROR"]> 0:
       
        report.write("ATTENTION REQUIRED\n")
    else:
        report.write("ALL GOOD")
    
    