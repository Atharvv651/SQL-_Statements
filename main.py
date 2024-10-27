import sqlite3
import pandas #type: ignore

conn = sqlite3.connect("database.sqlite")

season = input("Enter Season Number: ")
print()

avg_win_margin = pandas.read_sql(f"""SELECT AVG(Win_Margin) From Match WHERE Season_Id == {season}""", conn).to_dict()

avg_win_margin_of_winning_teams = pandas.read_sql(f"""SELECT AVG(Win_Margin), Match_Winner FROM Match WHERE Season_Id == {season} GROUP BY Match_Winner ORDER BY AVG(Win_Margin);""", conn).to_dict()

min_win_margin = pandas.read_sql(f"""SELECT MIN(Win_Margin) From Match WHERE Season_Id == {season}""", conn).to_dict()

max_win_margin = pandas.read_sql(f"""SELECT MAX(Win_Margin) From Match WHERE Season_Id == {season}""", conn).to_dict()

number_of_venues = pandas.read_sql(f"""SELECT COUNT(DISTINCT Venue_Id) FROM MATCH WHERE Season_Id == {season}""", conn).to_dict()

number_of_mans_of_the_match = pandas.read_sql(f"""SELECT COUNT(DISTINCT Man_of_the_Match) From Match WHERE Season_Id == {season}""", conn).to_dict()

print(f"Average Win Margin: {avg_win_margin['AVG(Win_Margin)'][0]}")
print()

print(f"Average Win Margin Of Winning Teams: ")
for winner_index in avg_win_margin_of_winning_teams['Match_Winner']:
    print(f"    Team Id {avg_win_margin_of_winning_teams['Match_Winner'][winner_index]}: {avg_win_margin_of_winning_teams['AVG(Win_Margin)'][winner_index]}")
print()

print(f"Minimum Win Margin: {min_win_margin['MIN(Win_Margin)'][0]}")
print()

print(f"Maximum Win Margin: {max_win_margin['MAX(Win_Margin)'][0]}")
print()

print(f"Number Of Venues: {number_of_venues['COUNT(DISTINCT Venue_Id)'][0]}")
print()

print(f"Number of Mans Of The Match: {number_of_mans_of_the_match['COUNT(DISTINCT Man_of_the_Match)'][0]}")
