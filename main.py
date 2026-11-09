import requests as req
response = req.get("https://api.github.com")
print(response.status_code)
for i in range(7):
    print("*" * i)