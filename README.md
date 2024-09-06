# Heart Disease Indicators Data Processing and Visualization

## Project Overview

The main objective of this project is to develop a Python program for processing and visualizing data related to key health indicators of patients with heart disease. 

## Dataset

The dataset comprises 319,795 patients and includes 18 variables such as BMI, smoking habits, alcohol consumption, and various health conditions. Here's a brief description of each variable:

- **`HeartDisease`**: Indicates whether the patient has coronary artery disease or has suffered a myocardial infarction (binary: Yes/No).
- **`BMI`**: Body Mass Index, calculated from the height and weight of the patient (numeric).
- **`Smoking`**: Indicates if the patient has smoked at least 100 cigarettes in their lifetime (binary: Yes/No).
- **`AlcoholDrinking`**: Indicates if the patient is a heavy drinker (men: >14 drinks/week, women: >7 drinks/week) (binary: Yes/No).
- **`Stroke`**: Indicates if the patient has ever had a stroke (binary: Yes/No).
- **`PhysicalHealth`**: Number of days in the past 30 days that the patient’s physical health was not good (numeric: 0-30).
- **`MentalHealth`**: Number of days in the past 30 days that the patient’s mental health was not good (numeric: 0-30).
- **`DiffWalking`**: Indicates if the patient has serious difficulty walking or climbing stairs (binary: Yes/No).
- **`Sex`**: The sex of the patient (categorical: Male/Female).
- **`AgeCategory`**: Age category of the patient, divided into 14 groups (categorical).
- **`Race`**: Imputed race of the patient (categorical).
- **`Diabetic`**: Indicates if the patient has diabetes (binary: Yes/No).
- **`PhysicalActivity`**: Indicates if the patient engaged in physical activity or exercise in the past 30 days outside of their regular job (binary: Yes/No).
- **`GenHealth`**: The patient's general health status (categorical).
- **`SleepTime`**: The average number of hours of sleep the patient gets in a 24-hour period (numeric).
- **`Asthma`**: Indicates if the patient currently has or has had asthma (binary: Yes/No).
- **`KidneyDisease`**: Indicates if the patient has kidney disease, excluding kidney stones, bladder infection, or incontinence (binary: Yes/No).
- **`SkinCancer`**: Indicates if the patient has or has had skin cancer (binary: Yes/No).

## Program

The program implements a command-line interface (CLI) with the following functionalities:

### 1. Data Loading
- **`LOAD`**: Prompts the user for a dataset filename and loads it into memory as a DataFrame. Displays summary information including column data types and memory usage.
- **`LOADF`**: Automatically loads the provided dataset (`heart_cleaned.csv`) and displays summary information.

### 2. Data Cleaning
- **`CLEAR`**: Clears the DataFrame from memory and shows the number of discarded records.

### 3. Data Processing
- **`AGEAVERAGE`**: Creates a new continuous variable `AgeAverage` derived from the `AgeCategory` column.
- **`SHOWFEATURES`**: Displays two lists containing categorical and numerical variables in the DataFrame.
- **`NUMSTAT`**: Provides statistical summaries for numerical columns.
- **`CATSTAT`**: Provides summaries for categorical columns.

### 4. Data Visualization
- **`CATGRAPH`**: Generates pie charts to visually represent the distribution of categorical variables using Plotly.
- **`BMI-HD`**: Visualizes the relationship between BMI and heart disease using Seaborn, including box plots and histograms.
- **`AGE-HDKDSC`**: Plots the relationship between age and the incidence of heart disease, kidney disease, and skin cancer using Seaborn.
- **`COMATRIX`**: Computes and visualizes the correlation matrix for categorical variables.

### 5. Program Termination
- **`QUIT`**: Clears the DataFrame and exits the program.

## Project Structure

- **/scripts**: Contains the main script `main.py` that implements the above functionalities.
- **/data**: Directory to store datasets.
- **/results**: Directory to save results for each run, such as visualizations and model outputs.
- **Dockerfile**: Instructions to containerize the application.
- **requirements.txt**: List of Python dependencies.
- **README.md**: This file.

## Requirements

The code is written in Python and requires the following libraries:

- Pandas
- Requests
- NumPy
- Matplotlib
- Seaborn
- Plotly

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/HugoTex98/EDA-Heart-Disease-Data.git
    cd EDA-Heart-Disease-Data
    ```
2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Building and Running the Docker Container

To build and run the Docker container for this project, follow the steps below:

### 1. Build the Docker Image

First, navigate to the root directory of the project (where `Dockerfile` is located) and run the following command to build the Docker image:

```bash
docker build -t eda-heart-disease-data .
```

This command builds the Docker image using the instructions in the Dockerfile and tags it as breast-cancer-prediction.

### 2. Run the Docker Container

Once the image is built, you can run the Docker container using the following command:

```bash
docker run -it --rm eda-heart-disease-data
```

 - **`-it`**: Runs the container in interactive mode, allowing you to interact with the terminal inside the container.
 - **`--rm`**: Automatically removes the container once it stops running, keeping your environment clean.
 - **`eda-heart-disease-data`**: The name of the Docker image you built.

Since the project is not a web application and does not expose any ports, the output from the script will be directly visible in the terminal where the container runs. If the script generates output files, they will be saved in the container's file system.

To stop the container while it’s running, you can do so by pressing Ctrl + C in the terminal where the container is running.

## Usage

Run the program using the command-line interface:

```bash
python main.py
```

Follow the prompts to load data, process it, and visualize various aspects related to heart disease indicators.
