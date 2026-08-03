import requests
import json 
from datetime import datetime

count= 0
total_stars= 0
name = input("\n Enter GitHub Username: ")
url= f"https://api.github.com/users/{name}"
response= requests.get(url)

if response.status_code == 200:
    print("GitHub user found.")
    repo=response.json()
    print(json.dumps(repo , indent= 4))
    url_ref=f"https://api.github.com/users/{name}/repos"
    response_r=requests.get(url_ref)
    repo_r= response_r.json()
    current_time= datetime.now().strftime("%d-%m-%y %H-%M-%S")
    github_report= current_time + ".txt"

    with open(github_report, "w") as file:
        file.write("GitHub User Report \n")
        file.write("===============================================================\n")
        file.write(f"Username :{repo['login']}\n")
        file.write(f"Name :{repo['name']}\n")
        file.write(f"Public Repositories :{repo['public_repos']}\n")
        file.write(f"Followers :{repo['followers']}\n")
        file.write(f"Following :{repo['following']}\n")
        file.write(f"Account Created :{repo['created_at']}\n")
        file.write(f"Profile URL :{repo['html_url']}\n")
        file.write("\n\n")
        file.write(f" Repository Name          Stars \n")
        file.write("------------------------------------------\n")
        for repofile in repo_r:
            count+= 1
            total_stars= total_stars + repofile['stargazers_count']
            file.write(f"{repofile['name']:<35}     {repofile['stargazers_count']:<4}\n")
        file.write("\n")
        file.write(f"Total repo: {count}\n")
        file.write(f"Total star_repo : {total_stars}")
else:
    print("Invalid GitHub username.")
