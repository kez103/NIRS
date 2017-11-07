import requests
import json

url = 'https://www.tinkoff.ru/api/v1/transfer_any_card_to_any_card_new/'\
      '?cardNumber=5559492500157741&expiryDate=07%2F21&securityCode=290'\
      '&formProcessingTime=590&moneyAmount=100.00&moneyCommission=30'\
      '&currency=RUB&sessionid=5UUqwtAAI7OUESILM1CFes5kL7kHJCV0.ds-api08'\
      '&origin=prt&toCardNumber=5211782790637513'

r = requests.get(url)
ps = json.loads(r.text)
ps = ps["confirmationData"]["3DSecure"]

print(r.status_code)
print(r.text)

url = 'https://www.tinkoff.ru/3ds-send/'\
      '?TermUrl=https%3A%2F%2Fwww.tinkoff.ru%2F3ds-callback%2F'\
      '&MD=' + ps["merchantData"] + '&acsUrl=' + ps["url"] + \
      '&PaReq=' + ps["requestSecretCode"]


r = requests.get(url)

print(r.status_code)
print(r.text)
