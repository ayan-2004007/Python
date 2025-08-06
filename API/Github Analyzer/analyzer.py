# Built a Github Profile analyzer

import requests
import json


def displayRepos(api):
    try:
        res=requests.get(api+"/repos")
        data=res.json()
        if res.status_code!=200:
            print(f"Internal Server Error : {data['message']} :\nStatus Code : {data['status']}")
            return
        print("="*150)
        print(" "*30,"GITHUB REPOSITORY INFORMATIONS")
        print("="*150)
        for repo in data:
            print(f"{'Repo Name :':<30} {repo['name']}")
            print(f"{'Description :':<30} {repo['description']}")
            print(f"{'Visibility :':<30} {repo['visibility']}")
            print(f"{'Most Used Language :':<30} {repo['language']}")
            print(f"{'Stars :':<30} {repo['stargazers_count']}")
            print(f"{'Watchers :':<30} {repo['watchers']}")
            print(f"{'Created at :':<30} {repo['created_at']}")
            print(f"{'Last Updated :':<30} {repo['updated_at']}")
            print(f"{'URL :':<30} {repo['html_url']}")
            print("-"*100)
    except Exception as e:
        print(f"Something went wrong while fetching data : {e}")

def displayProfile(api):
    try:
        res=requests.get(api)
        data=res.json()
        if res.status_code!=200:
            print(f"Internal Server Error : {data['message']} :\nStatus Code : {data['status']}")
            return
        print("="*150)
        print(" "*30,"GITHUB PROFILE INFORMATIONS")
        print("="*150)
        print(f"{'Username :':<30} {data['login']}")
        print(f"{'Fullname :':<30} {data['name']}")
        print(f"{'About :':<30} {data['bio']}")
        print(f"{'Company :':<30} {data['company']}")
        print(f"{'Blog/Personal Site :':<30} {data['blog']}")
        print(f"{'Location :':<30} {data['location']}")
        print(f"{'Pubic Repositories :':<30} {data['public_repos']}")
        print(f"{'Public Gists :':<30} {data['public_gists']}")
        print(f"{'Following :':<30} {data['following']}")
        print(f"{'Followers :':<30} {data['followers']}")
        print("-"*100)
    except Exception as e:
        print(f"Something went wrong while fetchin data : {e}")

def main():
    api="https://api.github.com/users/"
    username=str(input("Enter your github username : "))
    fullApi=api+username
    trigger=True
    while trigger:
        ch=int(input("What do you want to do ?\nPress 1 for display profile infos\nPress 2 for display Repository infos\nPress 3 for exit\n"))
        match ch:
            case 1:
                displayProfile(fullApi)
            case 2:
                displayRepos(fullApi)
            case 3:
                trigger=False
if __name__=="__main__":
    main()