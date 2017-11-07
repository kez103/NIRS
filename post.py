import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2683.0 Safari/537.36'
      }

r = requests.post('http://httpbin.org/post', data={
                  "mimeType": "application/json",
                  "text": "{\"amount\":\"100\",\"currency\":\"RUR\",\"cvc\":\"789\",\"expire_date\":\"0721\",\"src_number\":\"5559492500157741\",\"tgt_number\":\"5211782790637513\"}"})

# r.encoding = 'cp1251'
with open('test.html', 'w') as output_file:
    output_file.write(r.text)
print(r.status_code)
print(r.url)
print(r.text)
