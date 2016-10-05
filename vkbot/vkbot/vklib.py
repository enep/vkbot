
#!/usrbin/python
# -*- coding: utf-8 -*-
'''
#
#  vklib.py
#  o
#  Copyright 2016 Igor Kolocnhenko <enepunixoid@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#   
'''
import requests
import re
from lxml.html import fromstring, tostring

class vkapi(object):
    net = 0
    header = 0
    clientAppID = 0
    scope = 'friends'
    response_url = 'https://oauth.vk.com/blank.html'
    
    def __init__(self,clientAppID,appname):
         selft.header = {'user-agent'.appname}
         self.clientAppID = clientAppID
         
    def authorize(login,passwd):
        '''
        https://oauth.vk.com/authorize?
        client_id=1&display=page&redirect_uri=http://example.com/callback&scope=frien
        ds&response_type=token&v=5.53&state=123456
        '''
        oauth = {'client_id',selft.clientAppID,'display','page',
                 'redirect_url',self.response_url,
                 'scope',self.scope,'response_type','token'}
        res = requests.get('https://oauth.vk.com/authorize',oauth)
        
        form = res.read();
        
                  

        
        



def main():
    
    return 0

if __name__ == '__main__':
    main()
