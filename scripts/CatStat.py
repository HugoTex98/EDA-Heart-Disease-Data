import logging
import pandas as pd
from __init__ import ShowFeatures


def CatStat(heart_dataset: pd.DataFrame):
    """ 
    Display statistics for categorical variables in the dataset.

    This function retrieves the categorical variables from the given DataFrame 
    using the `ShowFeatures` function and then prints a statistical summary 
    for these variables.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing the features to be analyzed.

    Returns:
        None: The function does not return any value but prints the statistical summary 
        of the categorical variables.

    Prints:
        - A transposed DataFrame containing descriptive statistics for the categorical variables.
    """
    
    # Get Categorical Variables returned in ShowFeatures function
    _ , cat_vars = ShowFeatures(heart_dataset)
    # Get statistics of the categorical variables
    logging.info(cat_vars.describe().transpose())