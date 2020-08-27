import requests
#from lxml import html
import html

r = requests.get('https://www.startse.com/noticia/startups/mobtech/deep-learning-o-cerebro-dos-carros-autonomos')

#r.encoding = 'utf-8'
print(html.unescape(r.text))
print(r.encoding)

#articleBody