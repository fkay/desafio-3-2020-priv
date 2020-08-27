import requests
#from lxml import html
import html

r = requests.get('https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972')

#r.encoding = 'utf-8'
print(html.unescape(r.text))
print(r.encoding)

#articleBody