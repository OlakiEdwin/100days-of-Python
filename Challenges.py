def total_goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

goals_in_la_liga = 5
goals_in_copa_del_rey = 10
goals_in_champions_league = 15

total_goals_scored = total_goals(goals_in_la_liga, goals_in_copa_del_rey, goals_in_champions_league)

print(total_goals_scored)