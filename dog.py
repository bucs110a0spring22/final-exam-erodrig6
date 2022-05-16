import requests 
import json 

class DogFacts:
  def __init__(self):
    self.api_url = "http://dog-api.kinduff.com/api/facts"
    self.fact = ''

  def get(self):
#  ''' Method that gets different dog facts ##
#    args: None 
#    return: Dog Fact
# '''
    response = requests.get(self.api_url)
    fact = response.json()
    return fact 

  def getFact(self):
    ''' Gets singular Dog Fact
    args: None
    return: None '''
    self.fact = self.get()['facts']
    
    