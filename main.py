
import requests as req
response = req.get("https://api.github.com")
print(response.status_code)

def fetch_github_api():
    for i in range(7):
        print("*" * i)

def fetch_new():
     for j in range(7):
            print("j" * (7 - j))
    
for i in range(14):
    if i < 7:
        fetch_github_api()
        print(fetch_github_api())
    else:
        fetch_new()
        print(fetch_new())
