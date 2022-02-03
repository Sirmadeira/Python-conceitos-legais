
# get HTML from a file
with open(r"C:/__work/Python/tutorial/15 - scraping websites/wyndham.htm") as wyndham_file:

    # store the response
    html_text = wyndham_file.read()

from bs4 import BeautifulSoup

# parse the HTML
soup = BeautifulSoup(html_text,"html.parser")

# show the first hyperlink
# print(soup.body.a)

# print the first hyperlink in the first table cell
# print(soup.td.a)

# print out ...
print(soup.body.table.tr.td.a)
