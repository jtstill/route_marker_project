def get_combo_scores(teams, scores):
    # Make combinations
    combinations = list(itertools.combinations(teams, 4))
    # print(combinations)
    # print(len(combinations))

    score_sums = []
    for combo in combinations:
        sum = 0
        for team in combo:
            # print(scores[team])
            sum += scores[team]
        score_sums.append(sum)
    # print(score_sums)

    team_combos = []
    for combo in combinations:
        c = ""
        for team in combo:
            c = c + team + "|"
        team_combos.append(c[:-1])
    # print(team_combos)

    combo_scores = zip(team_combos, score_sums)
    sorted_combos = list(sorted(combo_scores, key=operator.itemgetter(1)))
    # print(sorted_combos)

    return sorted_combos


if __name__ == "__main__":
    import itertools
    import operator
    from bs4 import BeautifulSoup
    import requests
    import re
    import json
    import pandas as pd
    import numpy as np

    '''url = "https://www.cbssports.com/nfl/scoreboard/"
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.prettify())'''

    import nflgame

    games = nflgame.games(2023, week=5)
























    '''
    teams = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU',
             'IND', 'JAC', 'KC', 'LV', 'LAC', 'LAR', 'MIA', 'MIN', 'NE', 'NO', 'NYG', 'NYJ', 'PHI',
             'PIT', 'SF', 'SEA', 'TB', 'TEN', 'WAS']

    scores = {'ARI':20,
              'ATL':21,
              'BAL':10,
              'BUF':20,
              'CAR':24,
              'CHI':40,
              'CIN':34,
              'CLE':3, # bye
              'DAL':10,
              'DEN':21,
              'DET':42,
              'GB':13,
              'HOU':19,
              'IND':23,
              'JAC':25,
              'KC':27,
              'LV':17,
              'LAC':24, # bye
              'LAR':14,
              'MIA':31,
              'MIN':20,
              'NE':0,
              'NO':34,
              'NYG':16,
              'NYJ':31,
              'PHI':23,
              'PIT':17,
              'SF':42,
              'SEA':24, # bye
              'TB':26, # bye
              'TEN':16,
              'WAS':20}

    # Get all combinations and sort them, ascending
    sorted_combos = get_combo_scores(teams, scores)

    # Lowest eight combined team scores
    lowest = sorted_combos[0:8]
    print("LOWEST:", lowest)

    # Highest seventeen combined team scores
    highest = list(reversed(sorted_combos))[0:18]
    print("HIGHEST:", highest)'''



