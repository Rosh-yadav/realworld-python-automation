import os
import shutil


def sort_files_by_vendor(source_folder, destination_folder, vendors):
    os.makedirs(destination_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            for vendor in vendors:
                if vendor.lower() in filename.lower():
                    vendor_folder = os.path.join(destination_folder, vendor)
                    os.makedirs(vendor_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(vendor_folder, filename))
                    print(f"Moved {filename} → {vendor}/")
                    break


if __name__ == "__main__":
    source = "export"
    destination = "sorted"
    vendor_list = ["Apple", "Intel", "Samsung", "Dell"]

    sort_files_by_vendor(source, destination, vendor_list)