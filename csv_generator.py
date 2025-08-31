import random
import pandas as pd

mega_listionary = []


def random_numbers_gen():
    n_rows = int(input("how many rows do you want to generate? "))
    total_dist = 0  
    for i in range(0, n_rows):
        distance_to_next_point = round(random.uniform(0,10), 2)
        temp_dict = {
                    "point_name" : str(i+1) + "P",
                    "distance_to_next_point" : distance_to_next_point,
                    "total_distance" : distance_to_next_point + total_dist,
                    "instrument_reading": round(random.uniform(0,2), 2)
                    }
        total_dist += temp_dict["distance_to_next_point"]
        mega_listionary.append(temp_dict)
    return mega_listionary

def convert_random_cvs(list01):
    df = pd.DataFrame(list01)
    df.to_csv("points.csv", index = False)

def csv_generator_main():
    convert_random_cvs(random_numbers_gen())

#csv_generator_main()