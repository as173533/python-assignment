# import urllib.request, urllib.parse, urllib.error
#
# url = urllib.request.urlopen('https://www.google.com/')
#
# for line in url:
#     print(line.decode().strip())
# ========================================
import requests

# url = 'https://www.karmickinstitute.com/wp-content/uploads/2026/09/IT-Training-Institute-in-Kolkata.webp'
#
# headers = {
#     'user-agent': 'akash',
#
# }
#
# response = requests.get(url = url, headers = headers)
# # print(dir(response))
# pic = response.content
# f = open('pic_dadu.jpg', 'wb')
# f.write(pic)
url = 'https://www.karmickinstitute.com/'



response = requests.get(url = url)
print(response.text)

