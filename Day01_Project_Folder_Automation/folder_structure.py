
# Reference Links:
# 1. Python  Docs: https://pyquesthub.com/automating-project-folder-creation-with-python-a-step-by-step-guide
import os
import argparse

# Function to create project folders

def create_project_folders(base_path, project_name):
    project_path = os.path.join(base_path, project_name)
    try:
        # Create the project root folder
        os.makedirs(project_path)
        print(f'Project folder created at: {project_path}')

        # Define subdirectories
        subfolders = ['src', 'assets', 'tests', 'docs']
        for folder in subfolders:
            os.makedirs(os.path.join(project_path, folder))
            print(f'{folder} folder created.')

        # Create README.md file
        readme_path = os.path.join(project_path, 'README.md')
        with open(readme_path, 'w') as readme_file:
            readme_file.write(f'# {project_name}\nProject Created Successfully.')
        print(f'ReADME.md file created.')

    except FileExistsError:
        print('Project folder already exists.')
    except Exception as e:
        print(f'Error occurred: {e}')

# Main function to handle command line arguments

def main():
    parser = argparse.ArgumentParser(description='Automate Project Folder Creation')
    parser.add_argument('base_path', type=str, help='Base path where the project folder will be created')
    parser.add_argument('project_name', type=str, help='Name of the project for the folder structure')
    args = parser.parse_args()

    create_project_folders(args.base_path, args.project_name)

if __name__ == '__main__':
    main()