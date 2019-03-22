import requests

#为使用socks代理需更新requests为支持socks的版本
#pip install -U requests[socks]

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
url = 'https://www.google.com/'
proxies ={'http':'http:127.0.0.1:9081', 
            'https':'https:127.0.0.1:9081'
        }

#session = requests.session()
#session.proxies = proxies
#response = session.get(url)

response = requests.get(url,headers=header,proxies={'https':'https://127.0.0.1:9081'})

print(response.text)


