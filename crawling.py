from bs4 import BeautifulSoup

html = open('무제.html', encoding='utf-8')
soup = BeautifulSoup(html, "html.parser")

title=soup.find("title")

print(title)
print(title.string)
print(title.text)
print(title.get_text())


p1 = soup.find("p", id = "p1")
print(p1.string)

p = soup.find_all('p')
print(p)

for line in p:
    print(line.string)

li_1 = soup.select("div#selector > ul > li:nth-child(1)")
print(li_1)

li_12 = soup.select("div#selector > ul > li:nth-child(-n+2)")
print(li_12)

li_all = soup.select("div#selector > ul >li")
print(li_all)