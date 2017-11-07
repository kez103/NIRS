import requests

r = requests.get('https://p2p.skbbank.ru')
#r.encoding = 'cp1251'
with open('test.html', 'w') as output_file:
    output_file.write(r.text)
print(r.status_code)
print(r.url)
# print(r.text)
