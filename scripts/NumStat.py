import pandas as pd
from ShowFeatures import ShowFeatures


def NumStat(heart_dataset: pd.DataFrame):
    """ 
    Display statistical summary for numerical variables in the dataset.

    This function retrieves the numerical variables from the given DataFrame 
    using the `ShowFeatures` function and then prints a statistical summary 
    of these variables, rounded to three decimal places.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing the features to be analyzed.

    Returns:
        None: The function does not return any value but prints the statistical summary 
        of the numerical variables.

    Prints:
        - A transposed DataFrame containing descriptive statistics for the numerical variables, 
        rounded to three decimal places.
    """
    
    # Get Numerical Variables returned in ShowFeatures function
    num_vars, _ = ShowFeatures(heart_dataset)
    
    # Statistics of Numerical variables (rounded at 3rd decimal)
    print(round(num_vars.describe(), 3).transpose())