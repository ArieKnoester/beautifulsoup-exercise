# with open("website.html", encoding="utf-8") as site:
#     contents = site.read()
#
# soup = BeautifulSoup(markup=contents, features="html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
#
# print(soup.a)
# links = soup.find_all(name="a")
# print(links)
#
# for link in links:
#     # print(link.getText())
#     print(link.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")  # select first tag for an anchor in a paragraph
# # company_url = soup.select_one(selector="#name")  # select first tag for an id
# # company_url = soup.select(selector=".heading")  # select all tags with a known class
# print(company_url)