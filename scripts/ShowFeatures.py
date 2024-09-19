import logging
import pandas as pd
import numpy as np
from typing import Tuple
from __init__ import AgeAverage

def ShowFeatures(heart_dataset: pd.DataFrame) -> Tuple[np.array, np.array]:
    """ 
    Display and return the numerical and categorical features in the dataset.

    This function updates the given DataFrame using the `AgeAverage` function 
    to add an "AgeAverage" column. It then identifies and prints the numerical 
    and categorical features in the updated DataFrame. Finally, it returns 
    these features as separate arrays.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing the features to be analyzed.

    Returns:
        Tuple[np.array, np.array]: 
            - An array of numerical features from the DataFrame.
            - An array of categorical features from the DataFrame.

    Prints:
        - A list of numerical feature names.
        - A list of categorical feature names.
    """
    
    # Use "AgeAverage" function to update the DataFrame
    heart_dataset_new, Age_Values = AgeAverage(heart_dataset)
        
    # These will be important in commands 7 and 8, that's why we return them
    num_vars = heart_dataset_new.select_dtypes(include=[np.number])
    cat_vars = heart_dataset_new.select_dtypes(exclude=[np.number])
    
    logging.info('\nNumerical Variables: \n', list(num_vars.columns))
    logging.info('\nCategorical Variables: \n', list(cat_vars.columns))
    print('\n')
    
    return num_vars, cat_vars