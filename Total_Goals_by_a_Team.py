import requests
import json

def getTotalGoals(team, year):
    # URL templates to retrieve goals when team is home or away
    url_home = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page="
    url_away = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page="
    
    # Function to get goals for either home or away matches
    def getGoals(url, team_key):
        total_goals = 0
        page = 1
        
        while True:
            response = requests.get(url + str(page))
            data = response.json()
            
            # Process each match on the current page
            for record in data['data']:
                total_goals += int(record[team_key + 'goals'])
            
            # Check if there are more pages left
            if page >= data['total_pages']:
                break
            
            page += 1

        return total_goals

    # Get goals as home and away team
    goals = getGoals(url_home, 'team1') + getGoals(url_away, 'team2')

    return goals

# Example usage
team = 'Barcelona'
year = 2011
print(getTotalGoals(team, year))
