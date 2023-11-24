import requests

class ransomware_live_api_wrapper:
	def __init__(self):
		self.base = "https://api.ransomware.live"

	def country(self,country_id):
		response = requests.get(self.base+'/country/{0}'.format(country_id))
		return response.json()

	def group(self,group_name):
		response = requests.get(self.base+'/group/{0}'.format(group_name))
		return response.json() 

	def groups(self):
		response = requests.get(self.base+'/groups')
		return response.json()

	def groupvictims(self,group_names):
		response = requests.get(self.base+'/groupvictims/{0}'.format(group_names))
		return response.json()

	def recentcyberattacks(self):
		response = requests.get(self.base+'/recentcyberattacks')
		return response.json()

	def recentvictims(self):
		response = requests.get(self.base+'/recentvictims')
		return response.json()

	def victims(self,year,month):
		response = requests.get(self.base+'/victims/{0}/{1}'.format(year,month))
		return response.json()
