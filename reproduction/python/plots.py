import asyncio
import matplotlib.pyplot as plt
import aiohttp
import numpy as np
import pandas as pd
from understat import Understat

LEAGUES = ["Ligue_1", "La_liga", "EPL", "Bundesliga", "Serie_A", "RFPL"]
SEASONS = [2014, 2015, 2016, 2017, 2018, 2019, 2020]

def getPoints(liste):
    num_array = np.array(liste)
    pandas_array = pd.DataFrame(num_array[1:], columns=num_array[0])
    col_pts = pandas_array['PTS'].astype(int)
    sum_pts = col_pts.sum()
    return sum_pts

def getXPoints(liste):
    num_array = np.array(liste)
    pandas_array = pd.DataFrame(num_array[1:], columns=num_array[0])
    col_pts = pandas_array['xPTS'].astype(float)
    sum_pts = col_pts.sum()
    return sum_pts

def getMeanPerYear(league, liste):
    num_array = np.array(liste)
    pandas_array = pd.DataFrame(num_array[1:], columns=num_array[0])
    totalPoints = getPoints(liste)
    total_team = pandas_array['Team'].count()
    total_matches = int(pandas_array.loc[0, 'M'])
    return totalPoints/(total_matches*total_team)

def getMeanXPointsPerYear(league, liste):
    num_array = np.array(liste)
    pandas_array = pd.DataFrame(num_array[1:], columns=num_array[0])
    totalPoints = getXPoints(liste)
    total_team = pandas_array['Team'].count()
    total_matches = int(pandas_array.loc[0, 'M'])
    return totalPoints/(total_matches*total_team)

to_season = {2014 : "14-15", 2015 : "15-16", 2016 : "16-17", 2017 : "17-18", 2018 : "18-19", 2019 : "19-20", 2020 : "20-21"}

async def main():
  async with aiohttp.ClientSession() as session:
    understat = Understat(session)
    for league in LEAGUES:
      final_df = pd.DataFrame(columns=["Season", "result", "xPoints", "result_away", "xPointsAway"])
      for season in SEASONS:
        fixtures_dom = await understat.get_league_table(league, season, h_a = "home")
        fixtures_ext = await understat.get_league_table(league, season, h_a = "away")
        final_df = final_df._append({"Season": to_season[season], "result": getMeanPerYear(league, fixtures_dom), "xPoints" : getMeanXPointsPerYear(league, fixtures_dom), "result_away" : getMeanPerYear(league, fixtures_ext), "xPointsAway": getMeanXPointsPerYear(league, fixtures_ext)}, ignore_index=True)
      plt.figure()
      plt.plot(final_df['Season'], final_df['result'], marker='o', color="blue")
      plt.plot(final_df['Season'], final_df['result_away'], marker='o', color="green")
      plt.plot(final_df['Season'], final_df['xPoints'], marker='o', color="orange")
      plt.plot(final_df['Season'], final_df['xPointsAway'], marker='o', color="red")
      plt.title(league)
      plt.ylabel("mean gained points per match")
      plt.legend()
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())

