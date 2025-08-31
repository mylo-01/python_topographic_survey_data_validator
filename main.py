from functions import *
from csv_generator import *
from csv_plotter import *


if __name__ == "__main__":
    csv_generator_main()
    convert_random_cvs_02(height_calc(get_base_data()))
    average_calc()
    plotter_main("points_true_height.csv")
