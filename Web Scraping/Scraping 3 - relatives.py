
# get HTML from a file
with open(r"C:/__work/Python/tutorial/15 - scraping websites/wyndham.htm") as wyndham_file:

    # store the response
    html_text = wyndham_file.read()

from bs4 import BeautifulSoup

# parse the HTML
soup = BeautifulSoup(html_text,"html.parser")

# refer to the first div tag
first_div = soup.div

# look at immediate children
# for child in first_div.contents:
#     print(child)
    
# look at all descendants
for child in first_div.descendants:
    print(child)