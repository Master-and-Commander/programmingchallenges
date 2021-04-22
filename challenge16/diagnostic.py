"""
   test progress in various fields
   log progress
"""
from diagnosticQuestionEvaluationFunctions import runDiagnostic
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import xarray as xr
import numpy as np
from datetime import date
from datetime import datetime

if __name__ == "__main__":
    runDiagnostic(["python", "isaiah", "german", "fish"])
    #runDiagnostic(["fish"])
    # perhaps show total correct for each subject

    """
       Goal is to show progress this week
       progress from beginning
       trend
    """
    subjects = ["python", "isaiah", "german", "fish"]
    basepath = os.path.dirname(__file__)+"/logging/scores/"
    dates = pd.date_range("2021-4-19", date.today().strftime("%Y-%m-%d"))
    var_dict = {}
    print("date")
    print(dates)
    for subject in subjects:
        dfScores = pd.read_csv(basepath+subject+".csv")
        dfScores['date'] = dfScores['date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
        dfScores.set_index("date", inplace=True)
        dfScores = dfScores.reindex(dates, fill_value=0)
        var_dict[subject] = (["date", "attributes"], dfScores.to_numpy())


    attributes = ['correct', 'total', 'count', 'time']
    ds = xr.Dataset(
        data_vars=var_dict,
        coords=dict(date=dates,attributes=attributes)
        )
        # perhaps take top 7


    df = ds.sel(attributes='correct').to_dataframe()
    df = df.drop(['attributes'], axis=1)

    df = df.apply(pd.to_numeric)
    print(df)
    sns.lineplot(data=df, palette="tab10", linewidth=2.5)

    plt.show()
