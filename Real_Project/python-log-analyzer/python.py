import os
tcounts= 0
counts= {
    "INFO" : 0,
    "WARNING": 0,
    "ERROR": 0
}
name1=[]
name3=[]
with open("application.log" , "r") as file:
    output= file.readlines()
    print(output)
    for line in output:
        tcounts+= 1
        print(line)
    for data in output:
          print(repr(data))
          if data.strip() == "":
              continue
          column= data.split()
          status= column[2]
          if status =="INFO":
              counts["INFO"]+= 1
          if status == "ERROR":
              counts["ERROR"]+= 1
              #line4= f"{data}"
              #column1= line4.split()
              name2=" ".join(column[2:])
              name3.append(name2)   
          if status == "WARNING":
              counts["WARNING"]+= 1
    for key,values in counts.items():
        line1=f"{key} : {values}"
        name1.append(line1)   
with open("result.txt", "w") as file:
    file.write("=============================================\n")
    file.write("Log Analysis Report\n")
    file.write("===============================================\n")
    file.write(f"Total Log Entries: {tcounts}\n")
    for line3 in name1:
        file.write(f"{line3}\n")
    file.write("\n")
    if counts["ERROR"] > 0 :
        file.write("Errors Found\n\n")
        for line6 in name3:
         file.write(f"{line6} \n")
        file.write("\n")
        file.write("Status : ATTENTION REQUIRED")
         
         
        
    
    
    
   
    

        
    
        
    
    
    
    
    
    
    
    
    