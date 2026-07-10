import os
name1=[]
countl=0
file_list=[]
new_lisst=[]
new_size=[]
free_size= 0

size=[]
file= os.listdir("logs")
print(file)
for line in file:
    
    output=line.endswith("log")
    countl+= 1
    if output == False:
        continue
    name1.append(line)
    
 
print("total file :",countl)
name2=len(name1)

print("Files Scanned :",name2)

for line1 in name1:
    path=os.path.join("logs",line1)
    with open(path, "r") as file1:
        output1=file1.readlines()
        file_size=os.path.getsize(path)
        print(file_size)
        size.append(file_size)
        
    
print(size)
final_list= zip(name1 , size)

dele_file= []

        
print(dele_file)
       
with open("report.txt" , "w") as file2 :
    file2.write("=====================================\n")
    file2.write("Disk Cleanup Report\n")
    file2.write("========================================\n\n")
    file2.write(f"Files Scanned : {name2}\n\n")
    
    if name2 > 0:
     file2.write("Reading log file : \n")
     file2.write("file_name     :  size  \n")
     for file0 , size0 in final_list:
        file2.write(f"{file0} :    {size0} \n")
     deleting_file= zip(name1 , size)
     print(deleting_file)
     
    
     for name6, size6  in deleting_file:
        
        if size6 > 300:
          file2.write("File of bigger size which is going to be deleted \n\n")
          file2.write(f"{name6}\n")
          
 
          new_lisst=os.path.join("logs",name6)
          print(new_lisst)
         
          free_size= size6 + free_size
          
          file2.write(f"{free_size}\n")
          os.remove(new_lisst)
          file2.write("status \n")
          file2.write("clean successfully\n")
       
          
    else: 
       file2.write(f"no log file found")
        
  
     
   
      
    
    
      
    
    