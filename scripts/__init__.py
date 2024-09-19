import logging
from pathlib import Path 
from datetime import datetime
# Import scripts functions to be used in the main.py
from LoadDF import LoadDF
from Load import Load
from Clear import Clear
from Quit import Quit
from AgeAverage import AgeAverage
from ShowFeatures import ShowFeatures
from NumStat import NumStat
from CatStat import CatStat
from CatGraph import CatGraph
from BMI_HD import BMI_HD
from Age_HDKDSC import Age_HDKDSC
from CoMatrix import CoMatrix


def create_results_run_folder() -> Path:
    """
    Creates a folder within the current working directory to store results, named with the current timestamp.
    
    The folder is created inside a 'results' directory, and its name is based on the current date and time 
    in the format 'YYYYMMDD_HHMMSS'. If the folder already exists, a message is printed to indicate this.
    
    Returns:
        Path: The path to the newly created folder, or the existing folder if it was already present,
              for the run results.
    
    Raises:
        FileExistsError: If the folder already exists (caught internally and logged).
    """
    path = Path.cwd() / "results" / datetime.now().strftime(format="%Y%m%d_%H%M%S")
    try:
        path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        logging.error("Results folder is already created.")
    else:
        logging.info("Results folder was created!")

    return path

# Dataset directory
dataset_directory = 'https://raw.githubusercontent.com/HugoTex98/EDA-Heart-Disease-Data/main/dataset/heart_cleaned.csv'