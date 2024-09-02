import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os 
from pathlib import Path 
from datetime import datetime

# Import scripts functions to be used in the main.py
from LoadDF import LoadDF
from Load import Load
from Clear import Clear
from Quit import Quit
from AgeAverage import AgeAverage
from ShowFeatures import ShowFeatures
from NumStat import *
from CatStat import *
from CatGraph import *
from BMI_HD import *
from Age_HDKDSC import *
from CoMatrix import *


def create_results_run_folder() -> Path:
    path = Path.cwd() / "results" / datetime.now().strftime(format="%Y%m%d_%H%M%S")
    try:
        path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder is already there")
    else:
        print("Folder was created")

    return path

# Dataset directory
dataset_directory = Path(r'C:\Users\hugot\OneDrive\Ambiente de Trabalho\Projetos_DataScience\Hands_on_Projects\Processing_Viz_Heart_Disease_Data\EDA_Heart_Disease_Data\dataset/heart_cleaned.csv')

user_input = 0
while True:
    try:
        user_input = int(input("Which command you want to use? \n \
        1- LOAD \n \
        2- LOADF \n"))
    except ValueError:
        print("Only integers are accepted!")
        continue
    if user_input >= 1 and user_input <= 2:
        print(f'\nInserted the command: {user_input}')
        break
    else:
        print('The command must be 1 or 2')

if user_input == 1:
    heart_dataset = Load()
    
elif user_input == 2:
    heart_dataset = LoadDF(dataset_directory)


user_input2 = 0
while True:
    try:
        user_input2 = int(input("Do you want to use any of these commands? \n \
        1- CLEAR \n \
        2- QUIT \n \
        3- Proceed \n"))
    except ValueError:
        print("Only integers are accepted!")
        continue
    if user_input2 >= 1 and user_input2 <= 3:
        print(f'\nInserted the command: {user_input2}')
        break
    else:
        print('The command must be 1, 2 or 3')

if user_input2 == 1:
    heart_dataset = Clear(heart_dataset)
    
elif user_input2 == 2:
    if not heart_dataset.empty:
        del heart_dataset
        sys.exit("DataFrame deleted! Program is over.")
    else:
        sys.exit("Not possible to delete the DataFrame! Program is over.")
    
elif user_input2 == 3:
    heart_dataset = heart_dataset
    pass


user_input3 = 0
# Create folder for store the results of each run
results_folder = create_results_run_folder()
while True:
    try:
        user_input3 = int(input("\nWhich command do you want to use for data processing and visualization? \n \
        5- AGEAVERAGE \n \
        6- SHOWFEATURES \n \
        7- NUMSTAT \n \
        8- CATSTAT \n \
        9- CATGRAPH \n \
        10- BMI-HD \n \
        11- AGE-HDKDSC \n \
        12- COMATRIX \n \
        13- Proceed \n \
        14- None of the previously presented \n"))
        
    except ValueError:
        print("\nOnly integers are accepted! \n")
        continue
    
    if user_input3 >= 5 and user_input3 <= 14:
        print(f'\nInserted the command: {user_input3} \n')
        
        if user_input3 == 5:
            heart_dataset_AgeAverage, Age_Value = AgeAverage(heart_dataset)  
            
        elif user_input3 == 6:
            ShowFeatures(heart_dataset)

        elif user_input3 == 7:
            NumStat(heart_dataset)

        elif user_input3 == 8:
            CatStat(heart_dataset)

        elif user_input3 == 9:
            CatGraph(heart_dataset) 

        elif user_input3 == 10:
            BMI_HD(heart_dataset)

        elif user_input3 == 11:
            Age_HDKDSC(heart_dataset)  

        elif user_input3 == 12:
            CoMatrix(heart_dataset)
            
        elif user_input3 == 13:
            break

        elif user_input3 == 14:
            sys.exit("\nDon't want any data processing and visualization! \n")
    
    else:
        print('\nThe command must be an integer between 5 and 14 \n')


user_input4 = 0
while True:
    try:
        user_input4 = int(input("Do you want to use any of these commands? \n \
                                1- CLEAR \n \
                                2- QUIT \n \
                                3- Finish program \n"))
    except ValueError:
        print("Only integers are accepted!")
        continue
    if user_input4 >= 1 and user_input4 <= 3:
        print(f'\nInserted the command: {user_input4}')
        break
    else:
        print('The command must be 1, 2 or 3')

if user_input4 == 1:
    Clear(heart_dataset)
    
elif user_input4 == 2:
    if not heart_dataset.empty:
        del heart_dataset
        sys.exit("DataFrame deleted! Program is over.")
    else:
        sys.exit("Not possible to delete the DataFrame! Program is over.")
    
elif user_input4 == 3:
    sys.exit('\nProgram finished! \n')
