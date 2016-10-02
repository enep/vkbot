import re
import requests
 
def loginVK():
    login = '1@yandex.ru'
    password = '2'
    r = requests.get('https://oauth.vk.com/authorize?client_id=2662481&scope=friends,photos,messagesS&redirect_uri=http://oauth.vk.com/blank.html&display=page&response_type=token')
    t = re.search(r'ip_h=.*&', r.text).group()
 
    ip_h = t[5:-1]
    to = re.search(r'<input type=\"hidden\" name=\"to\" value=\".*\"', r.text).group()
    to = to[38:-1]
    data = {
 
        'ip_h': ip_h, 'origin': 'https://oauth.vk.com',
        'to': to,
        'expire': '0',
        'email': login,
        'pass': password}
    g = requests.post('https://login.vk.com/?act=login&soft=1',cookies= r.cookies, headers= r.headers, data=data)
 
    print g.text
loginVK()
