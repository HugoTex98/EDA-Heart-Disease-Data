import logging
import pandas as pd
import wx
from pathlib import Path


def get_path() -> Path:
    """
    Opens a file dialog to allow the user to select a file from the file explorer.
    
    The file dialog is configured to accept only files with `.csv` or `.py` extensions.
    If a file is selected, its path is returned as a `Path` object. If no file is 
    selected (e.g., if the user cancels the dialog), `None` is returned.

    Returns:
        Path: The path to the selected file as a `Path` object, or `None` if no file 
        was selected.
    """
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    # wildcard arg receives the file extension to look for
    dialog = wx.FileDialog(None, 'Open', wildcard= '*.csv;*.py', style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    
    dialog.Destroy()
    return Path(path)


def Load() -> pd.DataFrame:
    """
    Loads a dataset from a selected file and returns it as a pandas DataFrame.
    
    The function utilizes the `get_path` function to open a file dialog, allowing the user
    to choose a file. If the selected file has a `.csv` extension, it is read into a 
    DataFrame. If the file has a different extension or is not found, an empty DataFrame 
    is returned. The function also prints out basic information about the DataFrame, 
    including the first and last 5 records.
    
    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame. If no valid file is 
        selected, returns an empty DataFrame.
    """
        
    # use the `get_path` function to open a file explorer to choose the file to use
    heart_cleaned_dir = get_path()

    if heart_cleaned_dir.suffix == '.csv':
        # read the dataset choosen previously 
        heart_cleaned_file = pd.read_csv(''+ str(heart_cleaned_dir))
        logging.info(heart_cleaned_file.info())
        logging.info('\n First 10 records: \n')
        logging.info (heart_cleaned_file.head(n=10))
        logging.info('\n Last 10 records: \n')
        logging.info (heart_cleaned_file.tail(n=10))
        
    elif heart_cleaned_dir.suffix != '.csv':
        # if the file has an extension not supported, DataFrame remains empty
        heart_cleaned_file = pd.DataFrame({'Empty' : []})
        logging.error("File not found...")

    return heart_cleaned_file
    