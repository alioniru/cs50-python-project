#analyse game statistics of a particular team
import matplotlib.pyplot as plt
import pandas as pd

#read csv file

def read_file(file_path=None):
    try:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".xls") or file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)
        else:
            print("Unsupported file format. Please enter a CSV or Excel file.")
            file_path = None
    except FileNotFoundError:
        print("Error: File not found. Please try again.")
        file_path = None

#cleans the data
def clean_data(data):
    data["Total Yards Gained"] = (data["Rushing Yards"] + data["Passing Yards"]).round().astype(int)
    data["Yards Per Play"] = (data["Total Yards Gained"] / data["Total Plays"]).round().astype(int)
    return data

#makes the plots
def visualise_data(data, metric):
    games = data.index + 1
    if metric not in data.columns:
        print(f"{metric} not in data")
        return
    plt.plot(games, data[metric], marker='o', linestyle='-', label=metric)
    plt.title(f"{metric} Over The Season")  # Use f-string here
    plt.xlabel("Game #")
    plt.ylabel(metric)
    plt.xticks(games)
    plt.grid(True)
    plt.legend()
    plt.savefig(f"{metric}_plot.png", format='png')
    plt.close()

def main():
    file_path = None
    while True:
        if file_path is None:
            file_path = input("What is the name of the file? ").strip()
        data = read_file(file_path)
        if data is not None:
            break
        else:
            file_path = None
    cleaned_data = clean_data(data)
    while True:
            print("Available metrics:", list(cleaned_data.columns))
            metric = input("What metric do you want to plot? ")
            if metric in cleaned_data.columns:
                visualise_data(cleaned_data, metric)
                break
            else:
                print("No data to process.")

if __name__ == "__main__":
    main()
