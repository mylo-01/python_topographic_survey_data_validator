import pandas as pd
import matplotlib.pyplot as plt

def plotter_main(file_name):
    df = pd.read_csv(file_name)
    #Terrain
    plt.plot(df["total_distance"], df["point_true_height"], marker="o", linestyle=":", color="brown")
    #Average
    average_height = df["point_true_height"].mean()
    plt.axhline(y=average_height, color='orange', linestyle='-') # label=f'Average Height = {average_height:.2f}')
    
    plt.title("2D map")
    plt.xlabel("Distance in meters")
    plt.ylabel("Height")
    plt.grid(True)
    #plt.show()#it doesnt work, i am missing software
    #save to:
    plt.savefig("plot.png")

