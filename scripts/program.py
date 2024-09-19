import sys
import logging
# Import scripts functions to be used here
from __init__ import (LoadDF, Load, Clear, Quit,
                      AgeAverage, ShowFeatures, NumStat, 
                      CatStat, CatGraph, BMI_HD, Age_HDKDSC, 
                      CoMatrix, create_results_run_folder)


def eda_heart_disease_data_program(dataset_directory: str):
    user_input = 0
    while True:
        try:
            user_input = int(input("Which command you want to use? \n \
            1- LOAD \n \
            2- LOADF \n"))
        except ValueError:
            logging.error("Only integers are accepted!")
            continue
        if user_input >= 1 and user_input <= 2:
            logging.info(f'\nInserted the command: {user_input}')
            break
        else:
            logging.info('The command must be 1 or 2')

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
            logging.error("Only integers are accepted!")
            continue
        if user_input2 >= 1 and user_input2 <= 3:
            logging.info(f'\nInserted the command: {user_input2}')
            break
        else:
            logging.info('The command must be 1, 2 or 3')

    if user_input2 == 1:
        heart_dataset = Clear(heart_dataset)
        
    elif user_input2 == 2:
        if not heart_dataset.empty:
            del heart_dataset
            logging.info("DataFrame deleted! Program is over.")
            sys.exit()
        else:
            logging.info("Not possible to delete the DataFrame! Program is over.")
            sys.exit()
        
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
            logging.error("\nOnly integers are accepted! \n")
            continue
        
        if user_input3 >= 5 and user_input3 <= 14:
            logging.info(f'\nInserted the command: {user_input3} \n')
            
            if user_input3 == 5:
                heart_dataset_AgeAverage, Age_Value = AgeAverage(heart_dataset)  
                
            elif user_input3 == 6:
                ShowFeatures(heart_dataset)

            elif user_input3 == 7:
                NumStat(heart_dataset)

            elif user_input3 == 8:
                CatStat(heart_dataset)

            elif user_input3 == 9:
                CatGraph(heart_dataset, results_folder) 

            elif user_input3 == 10:
                BMI_HD(heart_dataset, results_folder)

            elif user_input3 == 11:
                Age_HDKDSC(heart_dataset, results_folder)  

            elif user_input3 == 12:
                CoMatrix(heart_dataset, results_folder)
                
            elif user_input3 == 13:
                break

            elif user_input3 == 14:
                logging.info("\nDon't want any data processing and visualization! \n")
                sys.exit()
        
        else:
            logging.info('\nThe command must be an integer between 5 and 14 \n')


    user_input4 = 0
    while True:
        try:
            user_input4 = int(input("Do you want to use any of these commands? \n \
                                    1- CLEAR \n \
                                    2- QUIT \n \
                                    3- Finish program \n"))
        except ValueError:
            logging.error("Only integers are accepted!")
            continue
        if user_input4 >= 1 and user_input4 <= 3:
            logging.info(f'\nInserted the command: {user_input4}')
            break
        else:
            logging.info('The command must be 1, 2 or 3')

    if user_input4 == 1:
        Clear(heart_dataset)
        
    elif user_input4 == 2:
        if not heart_dataset.empty:
            del heart_dataset
            logging.info("DataFrame deleted! Program is over.")
            sys.exit()
        else:
            logging.info("Not possible to delete the DataFrame! Program is over.")
            sys.exit()
        
    elif user_input4 == 3:
        logging.info('\nProgram finished! \n')
        sys.exit()
