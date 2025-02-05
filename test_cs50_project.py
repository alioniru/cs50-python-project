import matplotlib.pyplot as plt
import pandas as pd
import os
from project import read_file, clean_data, visualise_data

def test_read_file():
    result1 = read_file("game.txt")
    assert result1 is None
    result2 = read_file("nonexistant.csv")
    assert result2 is None
    result3 = read_file("game_data.xlsx")
    assert isinstance(result3, pd.DataFrame)

def test_clean_data_TYG():
    data = pd.DataFrame({
        "Rushing Yards": [1, 2, 3],
        "Passing Yards": [4, 5, 6],
        "Total Yards Gained": [3,6,9],
        "Total Plays": [3,3,3]
    })
    clean_data(data)
    assert list(data["Total Yards Gained"]) == [5,7,9]

def test_clean_data_YPP():
    data = pd.DataFrame({
        "Total Yards Gained": [3,6,9],
        "Total Plays": [3,3,3],
        "Rushing Yards": [1, 2, 3],
        "Passing Yards": [4, 5, 6]
    })
    clean_data(data)
    assert list(data["Yards Per Play"]) == [2,2,3]

def test_visualise_data(capsys):
    data = pd.DataFrame({
        "Rushing Yards": [1, 2, 3],
        "Passing Yards": [4, 5, 6]
    })
    metric = "Top Play"
    visualise_data(data,metric)
    assert capsys.readouterr().out.strip() == "Top Play not in data"

def test_visualise_data_png():
    data = pd.DataFrame({
        "Total Yards Gained": [3,6,9],
        "Total Plays": [3,3,3],
        "Rushing Yards": [1, 2, 3],
        "Passing Yards": [4, 5, 6]
    })
    metric = "Total Plays"
    visualise_data(data,metric)
    assert os.path.isfile("Total Plays_plot.png")
