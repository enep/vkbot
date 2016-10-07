#  vkapi.py
#  
#  Copyright 2016 Igor Unixoid Kolonchenko <enepunixoid@gmail.com>
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
#  
import requests
import sys

class vkapi(object):
	
	redirect_url = ''
	scope = 0  '''Разрешение прав доступа'''
	access_token = ''
	client_id = 
	
	"""
	https://oauth.vk.com/authorize?
	client_id=1&display=page&redirect_uri=http://example.com/callback
	&scope=friends&response_type=token&v=5.57&state=123456

 
	"""
	def __init__(self,_ci,_ru,_scope):
		self.redirect_url == _ru
		self.scope = _scope
		self.client_id = _ci
	
	def auth(login,passwd):
		url = "https://oauth.vk.com/authorize"
		params["client_id"] = self.client_id
		params["display"] = "mobile"
		params["redirecct_url"] = self.redirect_url
		params["scope"] = self.scope
		params["response_type"]="token"
		
		try:
			res = requests.get(url,params)
		except requests.
		
		
