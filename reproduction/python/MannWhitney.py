import asyncio
import aiohttp
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon, mannwhitneyu
from understat import Understat

SEASONS = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
LEAGUES = ["Ligue_1", "La_liga", "EPL", "Bundesliga", "Serie_A", "RFPL"]
tableaux = {}
for league in LEAGUES:
    tableaux[league] = pd.DataFrame(index=SEASONS, columns=SEASONS)

def getXPointsHomeAwayPerMatch(array, home):
    if array['h_a'] == 'h':
        home.append(array['xpts'])


def mannwhitneyutest(season1, season2):
    stat, p_value = mannwhitneyu(season1, season2, alternative="greater")
    return stat, p_value

def getMeanPerYear(league, liste):
    num_array = np.array(liste)
    pandas_array = pd.DataFrame(num_array[1:], columns=num_array[0])

def color_red_if_below(value):
    if value == '':
      return 'color: white'
    color = 'red' if value < 0.05 else 'white'
    return f'color: {color}'

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        for league in LEAGUES:
            season = 2014
            while season <= 2020:
                season1 = []
                fixtures = await understat.get_teams(league, season)
                num_array = np.array(fixtures)
                for i in range(len(num_array)):
                    for j in range(len(num_array[i]["history"])):
                        getXPointsHomeAwayPerMatch(num_array[i]["history"][j], season1)
                other_season = season + 1
                while other_season <= 2020:
                    season2 = []
                    fixtures2 = await understat.get_teams(league, other_season)
                    num_array2 = np.array(fixtures2)
                    for i in range(len(num_array2)):
                        for j in range(len(num_array2[i]["history"])):
                            getXPointsHomeAwayPerMatch(num_array2[i]["history"][j], season2)
                    _, p = mannwhitneyutest(season1, season2)
                    tableaux[league].loc[other_season, season] = float(p)
                    other_season += 1
                season += 1
            tableau = tableaux[league].fillna('')
            #tableau_styled = tableau.style.applymap(color_red_if_below)
            print(f'{league} xPoints change significance with mann')
            print(tableau)

if __name__ == "__main__":
    asyncio.run(main())