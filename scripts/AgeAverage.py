import pandas as pd 
from typing import Tuple


def AgeAverage(heart_dataset: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """ 
    Calculate the average age based on age categories in the dataset.

    This function creates a new variable based on the "AgeCategory" column, 
    calculating the average age for the defined intervals within this variable 
    and returning these values as continuous data.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing the "AgeCategory" column.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: 
            - The original DataFrame with an added "AgeAverage" column.
            - A DataFrame containing the calculated age averages for each age category.

    Raises:
        KeyError: If the "AgeCategory" column is not present in the DataFrame.
    """

    # Store AgeCategory in a variable
    if 'AgeCategory' not in heart_dataset.columns:
        raise KeyError("'AgeCategory' column not found in the DataFrame.")
    
    Age_Category = heart_dataset['AgeCategory'].to_frame()
    
    # Convert "80 or older" from AgeCategory to "80"
    Age_Category['AgeCategory'] = Age_Category['AgeCategory'].apply(lambda x: 80 if x == "80 or older" else x)  
    
    # Split the age intervals into separate columns 
    Age_Values = Age_Category.copy()
    Age_Values[['LowerLimit', 'UpperLimit']] = Age_Values['AgeCategory'].str.split('-', expand = True)
    Age_Values = Age_Values.fillna(80) # all NaN's are filled with 80 because we already corrected these cases above

    Age_Values['LowerLimit'] = pd.to_numeric(Age_Values['LowerLimit'])
    Age_Values['UpperLimit'] = pd.to_numeric(Age_Values['UpperLimit'])
    
    # Average of the values in the lower and upper age limits for each row
    Age_Values['AgeAverage'] = Age_Values[['LowerLimit', 'UpperLimit']].mean(axis=1)
    print(Age_Values['AgeAverage'])
    
    # Add Age_Average to the original DataFrame `hear_dataset`
    heart_dataset['AgeAverage'] = Age_Values['AgeAverage']

    return heart_dataset, Age_Values
    