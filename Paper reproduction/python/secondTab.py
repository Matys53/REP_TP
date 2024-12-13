from scipy.stats import wilcoxon
import asyncio
import aiohttp
import numpy as np
import pandas as pd
from understat import Understat

LEAGUES = ["Ligue_1", "La_liga", "EPL", "Bundesliga", "Serie_A", "RFPL"]
SEASONS = [2014, 2015, 2016, 2017, 2018, 2019, 2020]

def getHomeAwayResultPerMatch(result, home, away):
  if result['h'] > result['a']:
    home.append(3)
    away.append(0)
  elif result['h'] < result['a']:
    home.append(0)
    away.append(3)
  else:
    home.append(1)
    away.append(1)

def getGoalsAwayHomePerMatch(result, home, away):
  home.append(result['h'])
  away.append(result['a'])

def getXPointsHomeAwayPerMatch(array, home, away):
  if array['h_a'] == 'h':
    home.append(array['xpts'])
  else :
    away.append(array['xpts'])

def cohen_d(home, away):
  mean_a = np.mean(home)
  mean_b = np.mean(away)
  std_a = np.std(home, ddof=1)
  std_b = np.std(away, ddof=1)

  n_a = len(home)
  n_b = len(away)

  s_p = np.sqrt(((n_a - 1) * std_a**2 + (n_b - 1) * std_b**2) / (n_a + n_b - 2))

  cohen_d = (mean_a - mean_b) / s_p
  return cohen_d

def wilcoxon_test(array, home, away):
  for i in range(len(array)):
    getHomeAwayResultPerMatch(array[i]['goals'], home, away)
  stat, p = wilcoxon(home, away)
  return stat, p

def wilcox_x_test(array, home, away):
  for i in range(len(array)):
    for j in range(len(array[i]["history"])):
      getXPointsHomeAwayPerMatch(array[i]["history"][j], home, away)
  stat, p = wilcoxon(home, away)
  return stat, p

def getGoalsAwayHomePerMatch(result, home, away):
  home.append(float(result['h']))
  away.append(float(result['a']))

def wilcoxon_xgoals_test(array, home, away):
  for i in range(len(array)):
    getGoalsAwayHomePerMatch(array[i]['xG'], home, away)
  stat, p = wilcoxon(home, away)
  return stat, p

async def main():
  async with aiohttp.ClientSession() as session:
    understat = Understat(session)
    final_df = pd.DataFrame(columns=["League", "Season", "wilco-result", "wilco-result-pvalue", "result-cohend"])
    for league in LEAGUES:
      for season in SEASONS:
        home_results = []
        away_results = []
        home_xpoints = []
        away_xpoints = []
        home_xgoals = []
        away_xgoals = []
        fixtures = await understat.get_league_results(league, season)
        fixtures2 = await understat.get_teams(league, season)
        num_array = np.array(fixtures)
        wilco_test = wilcoxon_test(num_array, home_results, away_results)
        cohend_test = cohen_d(home_results, away_results)
        wilco_test_x = wilcox_x_test(fixtures2, home_xpoints, away_xpoints)
        cohend_test_x = cohen_d(home_xpoints, away_xpoints)
        wilco_test_xgoals = wilcoxon_xgoals_test(num_array, home_xgoals, away_xgoals)
        cohend_test_xgoals = cohen_d(home_xgoals, away_xgoals)
        new_row = pd.DataFrame({
            "League": [league],
            "Season": [season],
            "wilco-result": [wilco_test[0]],
            "wilco-result-pvalue": [wilco_test[1]],
            "result-cohend": [cohend_test],
            "wilco-xPoints": [wilco_test_x[0]],
            "wilco-xPoints-pvalue": [wilco_test_x[1]],
            "xPoints-cohend": [cohend_test_x],
            "wilco-xG": [wilco_test_xgoals[0]],
            "wilco-xG-pvalue": [wilco_test_xgoals[1]],
            "xG-cohend": [cohend_test_xgoals],
        })
        final_df = pd.concat([final_df, new_row], ignore_index=True)
    print(final_df)

if __name__ == "__main__":
    asyncio.run(main())
