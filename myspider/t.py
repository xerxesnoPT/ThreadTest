import requests
def geturltext(url):
    try:
        r = requests.get(url)
        a = r.raise_for_status()
        b = r.text
        r.encoding = r.apparent_encoding
        return b
    except:
        return 'something wrong'
if __name__=='__main__':
    print(geturltext('http://www.baidu.com'),end='\n')
