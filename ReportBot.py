'''This bot is designed to remove troll comments on websites that use the Disqus platform by automating the use of multiple flags. In order to set up, create five disqus accounts. Go to the URL https://disqus.com/profile/login/?next=/api/applications/register/ to obtain API Key, Secret Key, and Access Token. When you are there, enter generic names in the fields to complete registration. When registered, click details for the keys and tokens. Now, you are ready to use the bot. Click the time stamp of the comment you wish to remove. The comment will be highlighted. Go to the end of the URL and copy the comment ID. Place this number in the payload, then run the file.'''

import requests
 
 url = "https://disqus.com/api/3.0/posts/report.json"
 payload = {
     "api_key": "INSERT KEY",
     "api secret": "INSERT SECRET KEY",
     "access_token": "INSERT ACCESS TOKEN",
     "post": "INSERT NUMBERS AFTER #",
     "reason": "3"
 }
 response = requests.post(url, data=payload)
 print(response.json())
 
 url = "https://disqus.com/api/3.0/posts/report.json"
 payload = {
     "api_key": "INSERT KEY",
     "api secret": "INSERT SECRET KEY",
     "access_token": "INSERT ACCESS TOKEN",
     "post": "INSERT NUMBERS AFTER #",
     "reason": "3"
 }

url = "https://disqus.com/api/3.0/posts/report.json"
 payload = {
     "api_key": "INSERT KEY",
     "api secret": "INSERT SECRET KEY",
     "access_token": "INSERT ACCESS TOKEN",
     "post": "INSERT NUMBERS AFTER #",
     "reason": "3"
 }
 response = requests.post(url, data=payload)
 print(response.json())

url = "https://disqus.com/api/3.0/posts/report.json"
 payload = {
     "api_key": "INSERT KEY",
     "api secret": "INSERT SECRET KEY",
     "access_token": "INSERT ACCESS TOKEN",
     "post": "INSERT NUMBERS AFTER #",
     "reason": "3"
 }
 response = requests.post(url, data=payload)
 print(response.json())

url = "https://disqus.com/api/3.0/posts/report.json"
 payload = {
     "api_key": "INSERT KEY",
     "api secret": "INSERT SECRET KEY",
     "access_token": "INSERT ACCESS TOKEN",
     "post": "INSERT NUMBERS AFTER #",
     "reason": "3"
 }
 response = requests.post(url, data=payload)
 print(response.json())