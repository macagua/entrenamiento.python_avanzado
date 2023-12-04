from bs4 import BeautifulSoup
import urllib.request

def main():
    webUrl = urllib.request.urlopen("https://www.python.org/")
    print("result : " + str(webUrl.getcode()))
    data = webUrl.read()
    #print(data)
    soup = BeautifulSoup(data, 'html.parser')
    print(soup.prettify())
    print(soup.title)
    print(soup.title.string, type(soup.title.string))
    unicode_string = str(soup.title.string)
    print(unicode_string, type(unicode_string))
    #print(soup.find_all('a'))
    #for link in soup.find_all('a'):
    #    print(link.get('href'))

if __name__ == "__main__":
    main()
