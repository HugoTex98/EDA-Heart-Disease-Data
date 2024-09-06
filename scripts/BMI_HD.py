import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from pathlib import Path
from ShowFeatures import ShowFeatures


def BMI_HD(heart_dataset: pd.DataFrame, results_folder: Path):
    """ 
    Visualize the relationship between BMI and heart disease.

    This function generates visualizations to explore how Body Mass Index (BMI) 
    relates to the presence of heart disease in the dataset. It creates:
    - Box plots of BMI distributions for individuals with and without heart disease.
    - A histogram with a Kernel Density Estimate (KDE) to compare BMI distributions between those with and without heart disease.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing 'BMI' and 'HeartDisease' columns.
        results_folder (Path): The path to the newly created folder, or the existing folder if it was already present, to store results.

    Returns:
        None: The function does not return any value but generates and displays plots.

    Visual Output:
        - Two box plots showing the BMI distribution for individuals with and without heart disease.
        - A histogram with KDE overlay to compare BMI distributions between the two groups.
    """
    
    sns.set_style("darkgrid")
    # Get Numerical and Categorical variables with ShowFeatures function
    num_vars, cat_vars = ShowFeatures(heart_dataset)
    yes_disease = heart_dataset.loc[heart_dataset['HeartDisease'] == 'Yes']
    no_disease = heart_dataset.loc[heart_dataset['HeartDisease'] == 'No']

    # Store BMI and HeartDisease values in other vars
    Bmi = num_vars['BMI'].to_frame()
    Heart_Disease = cat_vars['HeartDisease'].to_frame()
    
    # Binary encoding of 'HeartDisease' classes 
    Heart_Disease['HeartDisease'] = Heart_Disease['HeartDisease'].apply(lambda x: 0 if x=='No' else 1) 

    # Concat Bmi and HeartDisease for the histplot
    Bmi_HeartDisease = pd.concat([Bmi, Heart_Disease], axis = 1, join = 'inner')

    # Subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10, 15))

    sns.boxplot(x = no_disease['BMI'], orient = "h", ax = ax2)
    ax2.set_title('BMI Distribution - No Heart Disease')    
    sns.boxplot(x = yes_disease['BMI'], orient = "h", ax = ax1)
    ax1.set_title('BMI Distribution - With Heart Disease')
    sns.histplot(data = Bmi_HeartDisease, x = 'BMI', hue = "HeartDisease", kde = True, ax = ax3)
    ax3.set_title('BMI Distribution with Heart Disease')

    plt.tight_layout()
    plt.savefig(Path.joinpath(results_folder, "BMI_Distribution_vs_Heart_Disease.png"))
    plt.show(block=False)
