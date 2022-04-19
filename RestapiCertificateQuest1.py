



import requests
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    # Write your code here
    goals=0
    pages=int(requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1').json()['total_pages'])
    for k in range(1,pages+1):
        url1=f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={k}'
        data1=requests.get(url1).json()['data']
        for f in data1:
            goals+=int(f['team1goals'])
    
    pages=int(requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1').json()['total_pages'])



    for k in range(1,pages+1):
        url1=f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={k}'
        data1=requests.get(url1).json()['data']
        for f in data1:
            goals+=int(f['team2goals'])
    return goals
    
    
if __name__ == '__main__':
    print(getTotalGoals('Barcelona',2011))