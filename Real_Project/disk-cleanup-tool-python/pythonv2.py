import os
space_free=0
count= 0
log_file= []
del_file= []
folder= os.listdir("logs")
print(folder)
for file in folder:
   
   logfile= file.endswith(".log")
   
   #print(logfile)
   if logfile ==False:
       continue
   count+= 1
   print(file)
   log_file.append(file)
   full_path=os.path.join("logs", file)
   print(full_path)
   file_size= os.path.getsize(full_path)
   
   print(file_size)
   if file_size > 300:
       print(file)
       space_free=file_size + space_free
       dela = os.remove(full_path)
       del_file.append(dela)
       
       
       
with open("reportv.txt", "w") as report:
    report.write("Disk Cleanup Report\n")
    report.write("==========================================================\n\n") 
    report.write(f"file scanned :{count}\n" )  
    for file in log_file:
     report.write(f"{file}\n")
    for dele in del_file:
     report.write(f"Deleted file: \n {dele}\n")
    report.write(f"space free {space_free}\n")
    