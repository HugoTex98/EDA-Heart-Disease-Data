import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from ShowFeatures import ShowFeatures


def CoMatrix(heart_dataset: pd.DataFrame, results_folder: Path):
    """ 
    Calculate and visualize the correlation matrix for categorical variables.

    This function computes and displays a heatmap of the correlation matrix for 
    categorical variables in the dataset. Categorical variables are first encoded 
    into numeric values using factorization, and then their correlations are calculated 
    using Spearman's rank correlation coefficient.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing categorical variables for 
                                      which the correlation matrix is calculated.
        results_folder (Path): The path to the newly created folder, or the existing folder if
                               it was already present, to store results.

    Returns:
        None: The function does not return any value but generates and displays a heatmap of the correlation matrix.

    Visual Output:
        - A heatmap showing the Spearman correlation coefficients between the encoded categorical variables.
    """
    
    # Get Categorical variables with ShowFeatures function
    _ , cat_vars = ShowFeatures(heart_dataset)

    # Encoding of categorical variables to numeric (with pd.factorize) and then calculates correlation between them
    corr_cat = cat_vars.apply(lambda x : pd.factorize(x)[0]).corr(method='spearman')

    # Heatmap of the correlation between Categorical variables
    fig, ax1 = plt.subplots()
    sns.heatmap(corr_cat, cmap = "crest", ax = ax1)
    ax1.set_title('Correlation Matrix of Categorical Variables')
    plt.savefig(Path.joinpath(results_folder, "CorrelationMatrix.png"))
    plt.show(block=False)
