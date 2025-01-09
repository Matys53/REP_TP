import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.stats import shapiro
from scipy.stats import ks_2samp
from scipy.stats import wilcoxon, mannwhitneyu

SEASONS = [2019, 2020, 2021, 2022, 2023]
LEAGUES = {"Championship" : ["10", "101"], "Serie-A" : ["24", "241"], "Primeira-Liga" : ["32", "321"], "Segunda-Division" : ["17", "171"], "Ligue-2" : ["60", "601"]}
to_seasons = {2019 : "2019-2020", 2020 : "2020-2021", 2021 : "2021-2022", 2022 : "2022-2023", 2023 : "2023-2024"}

def getMeanPoints(dataframe):
  sum = dataframe.sum()
  numTeams = len(dataframe)
  numMatches = numTeams * (numTeams - 1)
  mean = sum / numMatches
  return mean

for league in LEAGUES :
  final_df = pd.DataFrame(columns=["Season", "result", "xGoals", "result_away", "xGoalsAway"])
  for season in SEASONS :
    time.sleep(5)
    if(league == "Serie-A"):
      df = pd.read_html(f'https://fbref.com/en/comps/{LEAGUES[league][0]}/{season}/{season}-{league}-Stats', attrs={"id" :  f'results{season}{LEAGUES[league][1]}_home_away'})
    else :
      df = pd.read_html(f'https://fbref.com/en/comps/{LEAGUES[league][0]}/{to_seasons[season]}/{to_seasons[season]}-{league}-Stats', attrs={"id" :  f'results{to_seasons[season]}{LEAGUES[league][1]}_home_away'})
    df_pts_home = df[0].loc[:, ['Home']].loc[:, ('Home', 'Pts')]
    df_pts_away = df[0].loc[:, ['Away']].loc[:, ('Away', 'Pts')]
    df_xG_home = df[0].loc[:, ['Home']].loc[:, ('Home', 'xG')]
    df_xG_away = df[0].loc[:, ['Away']].loc[:, ('Away', 'xG')]
    final_df = final_df._append({"Season": to_seasons[season], "result": getMeanPoints(df_pts_home), "xGoals" : getMeanPoints(df_xG_home), "result_away" : getMeanPoints(df_pts_away), "xGoalsAway": getMeanPoints(df_xG_away)}, ignore_index=True)
  plt.plot(final_df['Season'], final_df['result'], marker='o', color="blue", label="result")
  plt.plot(final_df['Season'], final_df['result_away'], marker='o', color="green", label="result_away")
  plt.plot(final_df['Season'], final_df['xGoals'], marker='o', color="orange", label="xGoals")
  plt.plot(final_df['Season'], final_df['xGoalsAway'], marker='o', color="red", label="xGoalsAway")
  plt.title(league)
  plt.ylabel("mean gained points per match")
  plt.legend()
  plt.show()
