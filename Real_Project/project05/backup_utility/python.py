import os
import shutil
from datetime import datetime
import json

total_size= 0
file = []
file_backup= []
counts=0


print("==========================")
print(     "Backup Utility")
print("==========================")

print("1. Create Backup")
print("2. Restore Backup")
print("3. Exit")

choice=int(input("Enter your choice :\n"))
with open("config.json",'r') as file:
  data=json.load(file)
if choice==1:

  if os.path.isdir(data["source_folder"]):
    print("folder exist")
    try:
        files=os.listdir(data["source_folder"])
        for filename in files:
           counts+= 1
           file_backup.append(filename)
           full_path= os.path.join(data["source_folder"], filename)
           size=os.path.getsize(full_path)
           total_size+= os.path.getsize(full_path)
           print(total_size)
        if not os.path.exists(data["backup_folder"]):
             os.mkdir(data["backup_folder"])
        time= datetime.now().strftime("%d-%m-%Y %H_%M_%S") 
        backup_file= data["backup_folder"] + time
        backup_folder= os.path.join(
        data["backup_folder"],
        backup_file
        )
        shutil.copytree(data["source_folder"], backup_folder)   
        zip_file= shutil.make_archive(
        backup_folder,
        "zip",
        backup_folder
        )

        zip_size = os.path.getsize(zip_file) / 1024 
        zip_name= os.path.basename(zip_file)
        if os.path.exists(zip_file):
         shutil.rmtree(backup_folder)
        b_folder= os.listdir(data["backup_folder"])
        b_folder.sort()
        print(b_folder)
        l= len(b_folder)
        print(l)
        
        if l > 7:
          del_file= l - 7
          print(del_file)
          for f in b_folder[:del_file]:
              path= os.path.join(data["backup_folder"] , f)
              print(path)
              os.remove(path)
        line= "-" * 60    

        with open("backup-report.txt" , 'w') as file:
            file.write(f"{line}\n")
            file.write(f"Backup Report\n")
            file.write(line +"\n")
            file.write("\n")
            file.write(f"Backup Name \n")
            file.write(f"{line}\n")
            file.write(f"{zip_name}\n")
            file.write(f"Source Folder\n")
            file.write(f"{line}\n")
            file.write(f"{data['source_folder']}\n")
            file.write(line +"\n")
            file.write(f"Destination Folder\n")
            file.write(f"{line}\n")
            file.write(f"{data['backup_folder']}\n\n")
            file.write(f"Total Files Backed Up\n")
            file.write(f"{line}\n")
            file.write(f"{counts}\n")    
            file.write(f"Files Included \n")
            file.write(f"{line}\n")
            for fi in file_backup:
             file.write(f"{fi}\n")
            file.write(f"\n")
            file.write(f"Backup Size\n")
            file.write(f"{line}\n")
            file.write(f"{zip_size:.2f} KB\n")
            file.write(f"Backup Time\n")
            file.write(f"{line}\n")
            file.write(f"{time}\n")
            file.write(f"Status\n")
            file.write(f"{line}\n")
            file.write(f"SUCCESS\n")
    except Exception as e :
        print(e) 
  else:
     print("folder not exist")      
elif choice==2:
      print("Restoring the backup...")
      print("please select from the available backup:")
      if not os.path.exists("Restore"):
            os.mkdir("Restore")
      folder= os.listdir(data["backup_folder"])
      for backfile in folder:
         print(backfile)
      choice02=input("enter the name of backup file which u wanted to restore :\n")
      if choice02 in folder:
            zip_path= os.path.join(
              data["backup_folder"],
              choice02
            )
            unzip=shutil.unpack_archive(
              zip_path,
              "Restore"
            )
            
            print("Backup restored successfully.")
            print(f"Restored location: {os.path.abspath('Restore')}")         
elif choice ==3:
    print("Exist succesfully")
else:
    print("enter a valid input")


