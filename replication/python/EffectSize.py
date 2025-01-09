import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.stats import shapiro
from scipy.stats import ks_2samp
from scipy.stats import wilcoxon, mannwhitneyu

def decomposeScore(score, home, away):
  goals = score.split(chr(8211))
  if goals[0] > goals[1]:
    home.append(3)
    away.append(0)
  elif goals[0] == goals[1]:
    away.append(1)
    home.append(1)
  else:
    away.append(3)
    home.append(0)
  return home, away

def decomposeXg(dataframe, home, away):
  home.append(dataframe[0])
  away.append(dataframe[1])

def calculate_effect_size(home, away, stat):
  n = len(home)
  z = stat
  return z / np.sqrt(n)

SEASONS = [2019, 2020, 2021, 2022, 2023]
LEAGUES = {"Championship" : ["10", "101"], "Serie-A" : ["24", "241"], "Primeira-Liga" : ["32", "321"], "Segunda-Division" : ["17", "171"], "Ligue-2" : ["60", "601"]}
to_seasons = {2019 : "2019-2020", 2020 : "2020-2021", 2021 : "2021-2022", 2022 : "2022-2023", 2023 : "2023-2024"}

final_df = pd.DataFrame(columns=["League", "Season", "Wilcoxon-result", "Wilcoxon-pvalue", "Effect-size", "Wilcoxon-xG", "Wilcoxon-xG-pvalue", "Effect_size_xG"])

for league in LEAGUES:
  for season in SEASONS:
    time.sleep(5)
    if(league == "Serie-A"):
      df = pd.read_html(f'https://fbref.com/en/comps/{LEAGUES[league][0]}/{season}/schedule/{season}-{league}-Scores-and-Fixtures', attrs={"id" :  f"sched_{season}_{LEAGUES[league][0]}_1"})
    else :
      df = pd.read_html(f'https://fbref.com/en/comps/{LEAGUES[league][0]}/{to_seasons[season]}/schedule/{to_seasons[season]}-{league}-Scores-and-Fixtures', attrs={"id" :  f"sched_{to_seasons[season]}_{LEAGUES[league][0]}_1"})
    df = df[0].drop(['Attendance', 'Notes'], axis=1).dropna()
    data_pts = df.loc[:, ['Score']]
    data_xG = df.loc[:, ['xG', 'xG.1']]
    home_pts = []
    away_pts = []
    home_xG = []
    away_xG = []
    for i in range(len(data_pts)):
      score = data_pts.iloc[i, 0]
      xG = data_xG.iloc[i, :]
      if type(score) == str:
        decomposeScore(score, home_pts, away_pts)
      decomposeXg(xG, home_xG, away_xG)
    wilco_test = wilcoxon(home_pts, away_pts)
    effect_size = calculate_effect_size(home_pts, away_pts, wilco_test.statistic)
    wilco_xG_test = wilcoxon(home_xG, away_xG)
    effect_size_xG = calculate_effect_size(home_xG, away_xG, wilco_xG_test.statistic)
    new_row = pd.DataFrame({
            "League": league,
            "Season": [season],
            "Wilcoxon-result": [wilco_test.statistic],
            "Wilcoxon-pvalue": [wilco_test.pvalue],
            "Effect-size" : [effect_size],
            "Wilcoxon-xG": [wilco_xG_test.statistic],
            "Wilcoxon-xG-pvalue": [wilco_xG_test.pvalue],
            "Effect_size_xG" : [effect_size_xG]
        })
    final_df = pd.concat([final_df, new_row], ignore_index=True)

final_df