
# get HTML from a file
with open(r"C:/__work/Python/tutorial/15 - scraping websites/wyndham.htm") as wyndham_file:

    # store the response
    html_text = wyndham_file.read()

from bs4 import BeautifulSoup

# parse the HTML
soup = BeautifulSoup(html_text,"html.parser")


# searching by tag
# for header in soup.select("th"):
#     print(header)

# # searching by class
# for element in soup.select(".link"):
#     print(element.string.strip())

# searching by id
top_div = soup.select_one("#table-box")
print(top_div)



