import bs4 as bs
import urllib.request

link = input("copy your link here: ")
source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source,'lxml')
print(soup)
print(soup.title)
print(soup.title.name)
print(soup.title.text)
print(soup.title.string)
print(soup.find_all('p'))
for paragraph in soup.find_all('p'):
    print(paragraph.text)

print(soup.get_text())

nav = soup.nav
for url in soup.find_all('a'):
    print(url.get('href'))
    