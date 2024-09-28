import requests
import json
def getNumDraws(year):
  total = 0
  
   for g in range(0, 11):
     url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' +str(year)+ '&team1goals=' +str(g)+ '&team2goals=' +str(g)+ '&page=1'
     response = requests.request('GET', url, headers={}, data={})
     r = json.loads(response.text.encode('utf8'))
     total += r['total']
   
return total
