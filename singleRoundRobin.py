
import math

def roundRobin(teams):
    """Generates Round Robin scheduling fixtures for provided teams"""

    num_of_teams = len(teams)
    schedule = []

    if num_of_teams%2!=0:
        teams.append("BYE")
        num_of_teams=num_of_teams+1
    
    rounds = num_of_teams-1
        
    
    for i in range(rounds):
        for j in range(num_of_teams//2):
            team1 = teams[j]
            team2 = teams[num_of_teams-1-j]
            if team1=="BYE" or team2=="BYE":
                continue
            schedule.append(f"{team1} vs {team2}")
        
        teams.insert(1,teams.pop())
    
    return schedule

def ncr(n,r):
    return math.comb(n,r)


teams = ["mi","rcb","csk","dc","pk","gt","rr"]
schedule = roundRobin(teams)
for fixture in schedule:
    print(fixture)

if len(schedule)==ncr(7,2):
    print("correct schedule generated !")
else:
    print("incorrect schedule generated! ")