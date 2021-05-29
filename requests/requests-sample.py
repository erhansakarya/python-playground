import requests

getRequest = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=5)
print(getRequest)
print(getRequest.text)

# download image
downloadImageRequest = requests.get("https://imgs.xkcd.com/comics/python.png")
# open file in write byte format
with open("comic.png", "wb") as f:
    f.write(downloadImageRequest.content)
    
# create a resource
payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
postRequest = requests.post("https://jsonplaceholder.typicode.com/posts", data=payload)
print(postRequest.json())
rDict = postRequest.json()
print("user id is: " + str(rDict["id"]))