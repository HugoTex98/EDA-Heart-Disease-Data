import logging
import sys
import pandas as pd


def Quit(heart_dataset: pd.DataFrame):
    """ 
    Quit the program by deleting the provided DataFrame.

    This function deletes the provided DataFrame and then terminates the program. 
    If the DataFrame is already `None`, it will terminate the program with a message 
    indicating that deletion was not possible.

    Parameters:
        heart_dataset (pd.DataFrame): The DataFrame to be deleted. If None, no deletion occurs.

    Returns:
        None: The function does not return anything, as it terminates the program.

    Raises:
        SystemExit: Exits the program after attempting to delete the DataFrame, with 
        an appropriate message.
    """
    
    if heart_dataset is not None:
        del heart_dataset
        logging.info("DataFrame deleted! Program is over.")
        sys.exit()

    else:
        logging.error("Not possible to delete the DataFrame! Program is over.\n")
        sys.exit()

