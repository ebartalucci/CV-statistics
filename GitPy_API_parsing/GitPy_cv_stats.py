#               Author Ettore Bartalucci, 06.08.22 Eschweiler 

# Read data from my Github account and extract informations using Github REST API v3

import requests
import base64
from github import Github
from pprint import pprint

#### If using requests instead of PyGithub ####
# # Github username
# username = "ebartalucci"

# # Url to request
# url = f"https://api.github.com/users/{username}"

# # Make request and return JSON
# user_data = requests.get(url).json()

# # Print JSON data
# pprint(user_data)
################################################

######## FUNCTION SECTION #############
def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass

######## END FUNCTION SECTION #############

# Github username
username = "ebartalucci"
# password = "**********"

# Pygithub object
g = Github()

# Get user
user = g.get_user(username)

# Print all repos
for repo in user.get_repos():
    print_repo(repo)
    print("-"*100)

# Search by programming language
for i, repo in enumerate(g.search_repositories("language:matlab")):
    print_repo(repo)
    print("="*100)
    if i == 9:
        break



 


















