#
import requests as req
response = req.get("https://api.github.com")
print(response.status_code)
for i in range(7):
    print("*" * i)


for j in range(7):
        print("j" * (7 - j))