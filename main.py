import requests
import sys

name = input('Enter username :')
if(name == ''):
	print("Username not valid ! Try Again")
	sys.exit(0)
wlcm ='''
█▀ █▀█ █▀▀ █ ▄▀█ █     █▀ █▀▀ ▄▀█ █▀█ █▀▀ █░█
▄█ █▄█ █▄▄ █ █▀█ █▄▄   ▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█
'''
print(wlcm)
#--------------------------------------------------
github = requests.get(f'https://github.com/{name}')
st_code = github.status_code

if (st_code == 200):
	print('Github    ✔')
else:
	print('Github    ✖')

#--------------------------------------------------
gitlab = requests.get(f'https://gitlab.com/{name}')
st_code = gitlab.status_code

if(st_code == 200):
	print('Gitlab    ✔')
else:
	print('Gitlab    ✖')

#--------------------------------------------------
dev = requests.get(f'https://dev.to/{name}')
st_code = dev.status_code

if(st_code == 200):
	print('Dev.to    ✔')
else:
	print('Dev.to    ✖')

#--------------------------------------------------
attherate = '@'
medium = requests.get(f'https://medium.com/{attherate}{name}')
st_code = medium.status_code

if(st_code == 200):
	print('Medium    ✔')
else:
	print('Medium    ✖')
 
#--------------------------------------------------
replit = requests.get(f'https://replit.com/@{name}/')
st_code = replit.status_code

if(st_code == 200):
	print('Replit    ✔')
else:
	print('Replit    ✖')


#--------------------------------------------------
quora = requests.get(f'https://www.quora.com/profile/{name}')
st_code = quora.status_code

if(st_code == 200):
	print('Quora     ✔')
else:
	print('Quora     ✖')

#--------------------------------------------------

reddit = requests.get(f'https://www.reddit.com/user/{name}')
st_code = reddit.status_code

if(st_code == 200):
	print('Reddit    ✔')
else:
	print('Reddit    ✖')
 
#--------------------------------------------------
flickr = requests.get(f'https://www.flickr.com/people/{name}')
st_code = flickr.status_code

if(st_code == 200):
	print('Flickr    ✔')
else:
	print('Flickr    ✖')

#--------------------------------------------------
pinterest = requests.get(f'https://in.pinterest.com/{name}/')
st_code = pinterest.status_code

if(st_code == 200):
	print('Pinterest ✔')
else:
	print('Pinterest ✖')


instagram = requests.get(f'https://instagram.com/{name}/')
st_code = instagram.status_code

if(st_code == 200):
	print('Instagram ✔')
else:
	print('Instagram ✖')


#--------------------------------------------------
facebook = requests.get(f'https://www.facebook.com/{name}/')
st_code = facebook.status_code

if(st_code == 200):
	print('Facebook  ✔')
else:
	print('Facebook  ✖')

#--------------------------------------------------
gravatar = requests.get(f'https://en.gravatar.com/{name}')
st_code = gravatar.status_code

if(st_code == 200):
	print('Gravatar  ✔')
else:
	print('Gravatar  ✖')

#--------------------------------------------------
lastfm = requests.get(f'https://www.last.fm/user/{name}')
st_code = lastfm.status_code

if(st_code == 200):
	print('LastFm    ✔')
else:
	print('LastFm    ✖')

