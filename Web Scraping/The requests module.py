
import requests

# go to a website
response = requests.get(r"http://python-scraping.com/")

# test the status returned
if response.status_code == 404:
    print("Not found")
elif response.status_code == 200:
    html_returned = response.text
    print(html_returned)
else:
    print("Status code {0}".format(response.status_code))


    