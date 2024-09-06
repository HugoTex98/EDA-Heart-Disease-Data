import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from pathlib import Path
from plotly.subplots import make_subplots
from ShowFeatures import ShowFeatures


def CatGraph(heart_dataset: pd.DataFrame, results_folder: Path):
    """ 
    Display graphical summaries for categorical variables in the dataset.

    This function retrieves the categorical variables from the given DataFrame 
    using the `ShowFeatures` function and generates pie charts for each of these 
    variables, visually representing their composition.

    Parameters:
        heart_dataset (pd.DataFrame): The input DataFrame containing the features to be visualized.
        results_folder (Path): The path to the newly created folder, or the existing folder if it was already present, to store results.

    Returns:
        None: The function does not return any value but generates and displays pie charts 
        for the categorical variables.

    Visual Output:
        - Pie charts are generated and displayed for each categorical variable in the DataFrame.
    """
    
    # Get Categorical Variables
    _ , cat_vars = ShowFeatures(heart_dataset)
    
    # Graphs in ".png"
    # pio.renderers.default = 'png'
    pio.renderers.default = 'browser'
    
    # loop through categorical DataFrame columns to plot 
    for (index, colname) in enumerate(cat_vars):
        # separate labels for each variable
        labels = cat_vars[colname].value_counts().index
        # labels count for each variable
        values = cat_vars[colname].value_counts().values
        
        fig = go.Figure()
        fig.add_trace(go.Pie(labels = labels, values = values, hole = 0.3))
        fig.update_layout(title='{}'.format(colname))
        fig.write_image(Path.joinpath(results_folder, f"{colname}_PieChart.png"))
        fig.show()
