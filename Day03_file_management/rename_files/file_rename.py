import os 
# import shutil


def bulk_rename_files(folder_path, new_name_prefix, file_extension):
    """"
    Renaming mutiple files in a folder  with new extension 
    Args:
    folder_path (str) : path to the folder containing files
    new_name_prefix(str) : new prefix for the renamed files
    file_extension(str) : file extension to the filter  
    """
    ## list all the files inside the folder and sort them so easy naming consistent 
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(file_extension)])
    
    
    for index , filename in enumerate(files , start =1):
        old_path = os.path.join(folder_path , filename)
        new_filename = f"{new_name_prefix}-{index}-{filename}"
        new_path = os.path.join(folder_path , new_filename)
        
        os.rename(old_path , new_path)
        print(f"renamed {filename} -> {new_filename }")
        
        
if __name__ ==  "__main__":
        folder = "images"
        extension= ".jpg"
        prefix =  "holiday"
        
        
        bulk_rename_files(folder , prefix , extension)
        
        
    
        