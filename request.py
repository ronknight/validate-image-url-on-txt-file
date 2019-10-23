import requests

with open('images.txt','r') as urls:
    for url in urls.readlines():
        req = url.strip()
        print(req)
        page=requests.get(req)
        print(page.status_code)