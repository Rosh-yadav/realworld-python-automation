from ast import Delete
import os 

def delete_duplicate_files(base_folder , delete= True ):
    """"
    delete duplicate file ending with one if their original version exists 
    """
    for root, dirs , files in os.walk(base_folder ) :
        for filename in files :
            if "(1)" in filename:
                # build full path to duplicate 
                duplicate_path = os.path.join(root , filename)
                
                ## build path to original file (without (1))
                original_name = filename.replace("(1)", "")
                original_path = os.path.join(root , original_name)
                
                ## check if original file exists 
                if os.path.exists(original_path):
                    if delete : # type: ignore
                        os.remove(duplicate_path)
                    print(f"Deleted : {duplicate_path}")
                else :
                    print(f"(Dry-run) would delete  :{duplicate_path}")
                    
            else :
                    print(f"No original file fould for {filename}, skipping...")
                    

if __name__ == "__main__":
    
    base_folder = r"C:\Users\Roshni\Downloads\python_automation\python_automation\duplicate _files_module\test_files"

    delete_duplicate_files(base_folder, delete=True)

            