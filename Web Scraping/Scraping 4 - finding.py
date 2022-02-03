
# get HTML from a file
with open(r"C:/__work/Python/tutorial/15 - scraping websites/wyndham.htm") as wyndham_file:

    # store the response
    html_text = wyndham_file.read()

from bs4 import BeautifulSoup

# parse the HTML
soup = BeautifulSoup(html_text,"html.parser")

# # finding elements by tag
# links = soup.find_all("a")
# for link in links:

#     url = link.get("href")
#     print(str(url).strip())

# # finding elements by attribute

# # get element with given id
# element = soup.find_all(id="table-box")

# for el in element:
#     print(el.name)

# # show elements with src attribute
# srcs = soup.find_all(src=True)

# for src in srcs:
#     print(src)

# finding elements by class
# classy_links = soup.find_all(class_="link")

# for lk in classy_links:
#     print(lk.string.strip())


# non-recursive finds

# list all the div tags
tags = soup.find_all("div",recursive=True)

for tag in tags:
    print(tag)