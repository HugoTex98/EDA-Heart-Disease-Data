import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from ShowFeatures import ShowFeatures
from AgeAverage import AgeAverage


def Age_HDKDSC(heart_dataset: pd.DataFrame, results_folder: Path):
    """ 
    Visualize the relationship between average age and various diseases.

    This function generates Kernel Density Estimate (KDE) plots to explore how
    the average age (calculated using the `AgeAverage` function) relates to the 
    presence of heart disease, skin cancer, and kidney disease. It creates KDE 
    plots for individuals with each condition to visualize the distribution of 
    average age across these conditions.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing the 'AgeAverage', 
                                    'HeartDisease', 'KidneyDisease', and 'SkinCancer' columns.
        results_folder (Path): The path to the newly created folder, or the existing folder if
                               it was already present, to store results.

    Returns:
        None: The function does not return any value but generates and displays KDE plots.

    Visual Output:
        - KDE plots showing the distribution of average age for individuals with heart disease, 
        skin cancer, and kidney disease.
    """
    
    # Get the DataFrame with the age average calculated with AgeAverage function
    _ , Age_Values = AgeAverage(heart_dataset)

    # Get Categorical variables with ShowFeatures function
    _ , cat_vars = ShowFeatures(heart_dataset)
    
    # Store "HeartDisease", "KidneyDisease", "SkinCancer"  in a DataFrame
    Diseases_Age = cat_vars[['HeartDisease', 'KidneyDisease', 'SkinCancer']]

    # Get the positives cases of each disease
    yes_heart_disease = heart_dataset.loc[heart_dataset['HeartDisease'] == 'Yes']
    yes_skin_cancer = heart_dataset.loc[heart_dataset['SkinCancer'] == 'Yes']
    yes_kidney_disease = heart_dataset.loc[heart_dataset['KidneyDisease'] == 'Yes']

    # Create KDE plots
    fig, ax = plt.subplots()
    sns.kdeplot(data=heart_dataset, x=yes_heart_disease['AgeAverage'], label='HeartDisease', ax=ax)
    sns.kdeplot(data=heart_dataset, x=yes_skin_cancer['AgeAverage'], label='SkinCancer', ax=ax)
    sns.kdeplot(data=heart_dataset, x=yes_kidney_disease['AgeAverage'], label='KidneyDisease', ax=ax)
    fig.legend(labels=['HeartDisease', 'SkinCancer', 'KidneyDisease'])
    ax.legend(title='Condition')

    plt.title('KDE Plot of Average Age by Disease')
    plt.xlabel('Average Age')
    plt.ylabel('Density')
    plt.savefig(Path.joinpath(results_folder, "AverageAge_by_Disease_KDEPlot.png"))
    plt.show(block=False)
