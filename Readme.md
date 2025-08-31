# Python Topographic Survey Data Validator

## **Project Overview**
This project generates, processes, and visualizes topographic survey data using Python.  
It works entirely in a **virtual environment (`.venv`)** to isolate dependencies.  

The main functionalities are:  
1. Generate random survey points (`csv_generator.py`).  
2. Calculate true heights based on a reference point (`functions.py`).  
3. Plot the survey data in 2D (`csv_plotter.py`).  

---

## **Setup Instructions**

### 1. Clone the repository
git clone <your-repo-url>
cd python_topographic_survey_data_validator

### 2. Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies
pip install pandas matplotlib


## **Project Structure**
python_topographic_survey_data_validator/
│
├─ .venv/                     # Python virtual environment
├─ csv_generator.py           # Random survey points generator
├─ csv_plotter.py             # CSV plotter for survey data
├─ functions.py               # Core functions: height calculations, averages
├─ main.py                    # Entry point script
├─ points.csv / points_true_height.csv  # Generated CSV files
└─ plot.png # csv_plotter.py output
