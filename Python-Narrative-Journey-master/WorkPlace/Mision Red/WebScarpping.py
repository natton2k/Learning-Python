import requests
import bs4
res = requests.get('https://www.thegoldbugs.com/blog')
soup = bs4.BeautifulSoup(res.text, 'lxml')
word_list = soup.select('pre')[0].text.split('-----')
result = ''
print(word_list)
for word in word_list:
    try:
        result +=word[0]
    except:
        pass
print(result)

