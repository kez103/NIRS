# Подключение библиотек

import requests
import json

# get-запрос на сайт Tinkoff
# Передаем свои значения cardNumber, expiryDate, moneyAmount и toCardNumber

# securityCode, formProcessingTime и sessionId могут принимать любые значения

# Как показала практика, комиссия высчитывается на стороне сервера Tinkoff
# и не зависит от значения поля Comission

url = 'https://www.tinkoff.ru/api/v1/transfer_any_card_to_any_card_new/'\
      '?cardNumber=5559492500157741&expiryDate=07%2F21&securityCode=290'\
      '&formProcessingTime=590&moneyAmount=100.00&moneyCommission=30'\
      '&currency=RUB&sessionid=5UUqwtAAI7OUESILM1CFes5kL7kHJCV0.ds-api08'\
      '&origin=prt&toCardNumber=5211782790637513'

# Посылаем запрос на сайт Tinkoff
# Получаем документ формата JSON с ссылкой на сайт Альфа банка, а также
# значениями PaReq и MD, полученными с использованием данных с карт

r = requests.get(url)

# Парсинг JSON

# ps = json.loads(r.text)
ps = r.json()
ps = ps["confirmationData"]["3DSecure"]
print(ps)
url = ps["url"]  # url Альфы

print(url)

# post-запрос на сайт Альфа банка

r = requests.post(url, data={
                  'PaReq': ps["requestSecretCode"],   # Данные,
                  'TermUrl': 'https%3A%2F%2Fwww.tinkoff.ru%2F3ds-callback%2F',
                  'MD': ps["merchantData"]})   # полученные из JSON

# В ответ получаем html-документ с формой для ввода пароля из смс

S = r.text

# Модификация полученного html:

# Внешние объекты ( скрипты и иконки ), подгружаемые страницей html,
# имеют относительные ссылки на источник.
# Поэтому для успешной их подгрузки в html необходимо вставить базовую ссылку

i = S.find('<meta')

S = S[0:i-1] + '<base href="https://acs.alfabank.ru" />' + S[i:len(S)-1]

# Также для корректного отображения данных необходимо указать кодировку

i = S.find('meta')
S = S[0:i+4] + ' charset="UTF-8" ' + S[i+5:len(S)-1]

# Запись html в файл

print(r.status_code)
with open('alfa.html', 'w', encoding="UTF-8") as f:
    f.write(S)
