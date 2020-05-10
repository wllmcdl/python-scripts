import requests

#r = requests.get('https://imgs.xkcd.com/comics/python.png')

# wb means write bytes
# get an image and stores it in our script location since we didn't specify a location
# with open('comic.png', 'wb') as f:
    # f.write(r.content)

# payload = {'page':2, 'count':25}
# r = requests.get('https://httpbin.org/get', params=payload)

#payload = {'username':'Alain', 'password':'testing'}
#r = requests.post('https://httpbin.org/post', data=payload)

# r.json() returns the data in json format
# r_dict = r.json()
#print(r_dict['form'])

# testing login
r = requests.get('https://httpbin.org/basic-auth/william/testing', auth=('william', 'testing'))
print(r.text)
