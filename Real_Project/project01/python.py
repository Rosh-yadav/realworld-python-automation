import psutil
import os
from datetime import datetime
from colorama import Fore , Style
import subprocess

cpu = psutil.cpu_percent()
memory= psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent
uptime= psutil.boot_time()

current_time= datetime.now()
word = current_time.strftime("%Y-%m-%d %H_%M_%S")
threshold_limit = 80

with open( word , "a") as report:
    report.write("================== System Health Report ==================== \n")
    
    if cpu >= 90 :
          print(Fore.RED + "CRITICAL")
    elif cpu >= 60 and cpu < 90 :
          print(Fore.YELLOW + "wARNING")
    else :
          print(Fore.GREEN + "HEALTHY" + Style.RESET_ALL )
          
    report.write(f"cpu usage is :{cpu}\n")
    report.write(f"memory usage is :{memory}\n")
    report.write(f"disk usage is : {disk} \n ")
    report.write("\n")
    if (cpu  and memory) < threshold_limit:
      report.write(f"status: Healthy \n  ")
    else :
        report.write(f"status : unhelathy \n")
        
    report.write(f"Genearted at  \n {word}")
    
     
result= subprocess.run(
   [ "hostname"],
   capture_output=True,
   text=True
      
)

print(result.stdout)