from __init__ import (dataset_directory, datetime, Path, logging)
from program import eda_heart_disease_data_program

# Configure logging
logs_dir = Path.cwd() / 'logs' # Create logs directory if it doesn't exist
logs_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename= logs_dir / f'EDA_Heart_Disease_Data_{datetime.now().strftime(format="%Y%m%d_%H%M%S")}.log',  # The log file where logs will be stored
    level=logging.DEBUG,                                                                                   # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s',                                                    # Log message format
    filemode='a'                                                                                           # 'w' to overwrite the log file every run, 'a' to append to it
)

logging.info("Starting EDA Heart Disease data program! \n")
# Main program execution
if __name__ == "__main__":
    try:
        eda_heart_disease_data_program(dataset_directory)  
        logging.info("\nProgram completed successfully!")
        
    except Exception as e:
        # Log the error in case of an exception
        logging.error("An error occurred \n\n", exc_info=True)
    finally:
        # Ensure logs are flushed to the log file
        logging.shutdown()