import pandas as pd
import numpy as np
import time
from scipy.stats import shapiro
from scipy.stats import ks_2samp
from scipy.stats import wilcoxon, mannwhitneyu

SEASONS = [2019, 2020, 2021, 2022, 2023]
LEAGUES = {"Championship" : ["10", "101"], "Serie-A" : ["24", "241"], "Primeira-Liga" : ["32", "321"], "Segunda-Division" : ["17", "171"], "Ligue-2" : ["60", "601"]}
to_seasons = {2019 : "2019-2020", 2020 : "2020-2021", 2021 : "2021-2022", 2022 : "2022-2023", 2023 : "2023-2024"}

def getDiffPoints(dataframe):
  df_home = dataframe[0].loc[:, ['Home']].loc[:, ('Home', 'Pts')]
  df_away = dataframe[0].loc[:, ['Away']].loc[:, ('Away', 'Pts')]
  diff = df_home.sum() - df_away.sum()
  return diff

def getDiffXGoals(dataframe):
  df_home = dataframe[0].loc[:, ['Home']].loc[:, ('Home', 'xG')]
  df_away = dataframe[0].loc[:, ['Away']].loc[:, ('Away', 'xG')]
  diff = df_home.sum() - df_away.sum()
  return round(diff, 1)

final_df = pd.DataFrame(columns=["League", "Season", "Diff_pts", "Diff_xG"])
for league in LEAGUES.keys():
  for season in SEASONS:
    time.sleep(5)
    if(league == "Serie-A"):
      df = pd.read_html(f'https://fbref.com/en/comps/{LEAGUES[league][0]}/{season}/{season}-{league}-Stats', attrs={"id" :  f'results{season}{LEAGUES[league][1]}_home_away'})
    else :
      df = pd.read_html(f'https://fbref.com/en/comps/{LEAGUES[league][0]}/{to_seasons[season]}/{to_seasons[season]}-{league}-Stats', attrs={"id" :  f'results{to_seasons[season]}{LEAGUES[league][1]}_home_away'})
    diff_pts = getDiffPoints(df)
    diff_xG = getDiffXGoals(df)
    final_df = final_df._append({"League": league, "Season": season, "Diff_pts": diff_pts, "Diff_xG": diff_xG}, ignore_index=True)

print(final_df)