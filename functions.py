# You got this man, just use what you already know...
#Import libraries:
import pandas as pd
def pandas_working():
    print(pd.__version__)
#Initialize variables:



temp_point_dictionary = {} #Dictionary for information for every point.
# Test list
point_dictionary_list = [] #List of "rows"
processed_point_dictionary_list = []


def get_base_data():
    base_height = float(input("What is the initial reference point of elevation? "))
    base_reading = float(input("What the instrument reading to the reference point? "))
    print(f"You inserted {base_height} as reference and {base_reading} as reading")
    base_height += base_reading
    return base_height

def csv_get_base_data(document_name):
    df = pd.read_csv(document_name)
    point_dictionary_list = df.to_dict(orient="records")
    return point_dictionary_list

def height_calc(base_height):
    point_dictionary_list = csv_get_base_data("points.csv")
    for point in point_dictionary_list:
        point_true_height = base_height - float(point["instrument_reading"])
        temp_point_dictionary = {"point_name" : point["point_name"],
                                "distance_to_next_point": point["distance_to_next_point"],
                                "total_distance": point["total_distance"],
                                "instrument_reading" : point["instrument_reading"],
                                "point_true_height" : point_true_height
                                }
        processed_point_dictionary_list.append(temp_point_dictionary)
    #for i in processed_point_dictionary_list:
        #print(i)
    return processed_point_dictionary_list

def convert_random_cvs_02(list01):
    df = pd.DataFrame(list01)
    df.to_csv("points_true_height.csv", index = False)

def average_calc(sumatory = 0): 
    for i in processed_point_dictionary_list:
        sumatory += i["point_true_height"]
    print(f"The average for the point height is: {sumatory/len(processed_point_dictionary_list)} meters above sea level")
    #return (sumatory/)
