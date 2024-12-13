import asyncio
import json
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

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        final_df = pd.DataFrame(columns=["League", "Season", "Diff_pts", "Diff_Xpts"])
        for league in LEAGUES:
            for season in SEASONS:
                fixtures_dom = await understat.get_league_table(league, season, h_a = "home")
                fixtures_ext = await understat.get_league_table(league, season, h_a = "away")
                diff_pts = getPoints(fixtures_dom) - getPoints(fixtures_ext)
                diff_xpts = round(getXPoints(fixtures_dom) - getXPoints(fixtures_ext))
                final_df = final_df._append({"League": league, "Season": season, "Diff_pts": diff_pts, "Diff_Xpts": diff_xpts}, ignore_index=True)
                #print(f"différence de points en {league} de la saison {season} : {diff_pts}")
        print(final_df)

if __name__ == "__main__":
    asyncio.run(main())