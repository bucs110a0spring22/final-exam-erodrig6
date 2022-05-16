import requests 
import json 

class CatFacts:
  def __init__(self):
    self.api_url = "https://catfact.ninja/fact?max_length=64"
    self.fact = ''

  def get(self):
#  ''' Method that gets different cat facts
#  args: None 
#  return: Cat Fact'''
    response = requests.get(self.api_url)
    fact = response.json()
    return fact 

  def getFact(self):
 #   ''' Gets singular Cat Fact
  #  args: None
  #  return: None '''
    self.fact = self.get()['fact']
    
    