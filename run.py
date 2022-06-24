import argparse
import pandas as pd
from colorama import init, Fore
from time import sleep
import numpy as np


init()

# how to run the file with command-line arguments
arg_parser = argparse.ArgumentParser(
    description="Read and analyze data from a dataset", epilog="Enjoy the program 😊"
)

arg_parser.add_argument(
    "path",
    metavar="path",
    type=str,
    help="Path to CSV file",
)
arg_parser.add_argument(
    "output_file",
    metavar="output_file",
    type=str,
    help="A text file to export all insights",
)


args = arg_parser.parse_args()

input_path = args.path

output_file = args.output_file


def append_data_to_file(data):
    with open(output_file, "a+") as output_file_object:
        # put cursor to beginning of file
        output_file_object.seek(0)
        # file not empty? append a new line.

        data_in_file = output_file_object.read(100)

        if len(data_in_file) > 0:
            output_file_object.write("\n")

        output_file_object.write(data)


def read_input_path(input_path):
    """
    This function reads the input path and returns the nature of the data
    """
    # prints thge name of the survey data
    print(f"READING {input_path} ...")

    append_data_to_file(f"READING {input_path} ...")

    data_frame = pd.read_csv(input_path, low_memory=False)

    count = 0
    # which columns are present in the dataset
    for column in data_frame:
        count += 1

    print(f"\n {Fore.BLUE} FOUND {count} columns in the dataset.")
    append_data_to_file(f"\nFOUND {count} columns in the dataset.")

    # which rows are present
    print(f"\n {Fore.BLUE} FOUND {data_frame.shape[0]} rows in dataset")
    print("Done")

    return data_frame


def analyze_data(data_frame):
    """
    This function analyzes data to check for various insights
    """

    # this keeps track of each columns values

    data_setA = data_frame.iloc[:, 0:21]

    # understanding who took part in the survey
    job_title_counts = data_setA["Job Title"].value_counts()

    print(f"\n{Fore.WHITE} Which people took part in this survey?")
    print(f"===============================================")
    print(job_title_counts)

    append_data_to_file("\nWhich people took part in this survey?")
    append_data_to_file(str(job_title_counts))

    # understanding the most recommended to learn in 2021
    print(f"\nWhat is the most recommended programming language?")
    recommended_langauge_value_counts = data_setA["Recommended"].value_counts()

    append_data_to_file("\nWhat is the most recommended programming language?")
    append_data_to_file(str(recommended_langauge_value_counts))

    # understanding the programming language each participant is using currently
    print(f"\nWhat Programming language is each user using currenty?")

    Python = data_setA["Python"].count()
    R = data_setA["R"].count()
    SQL = data_setA["SQL"].count()
    C = data_setA["C"].count()
    C_plus = data_setA["C++"].count()
    Java = data_setA["Java"].count()
    Javascript = data_setA["Javascript"].count()
    Julia = data_setA["Julia"].count()
    Swift = data_setA["Swift"].count()
    Bash = data_setA["Bash"].count()
    MATLAB = data_setA["MATLAB"].count()
    none = data_setA["None"].count()
    Other = data_setA["Other"].count()

    labels = [
        "Python",
        "R",
        "SQL",
        "C",
        "C++",
        "Java",
        "Javascript",
        "Julia",
        "Swift",
        "Bash",
        "MATLAB",
        "None",
        "Other",
    ]

    values = [
        Python,
        R,
        SQL,
        C,
        C_plus,
        Java,
        Javascript,
        Julia,
        Swift,
        Bash,
        MATLAB,
        none,
        Other,
    ]

    code_language = pd.DataFrame(labels)
    code_language = code_language.rename(columns={0: "Coding language"})
    code_language.insert(1, column="frequency", value=values)
    print(code_language)

    append_data_to_file(
        "\nWhich programming language is each participant currently using?"
    )
    append_data_to_file(str(code_language))

    print(f"Where are the participants from?")
    # convert value counts to data_setA
    cols = ["Country"]
    user_count = pd.DataFrame(data_setA[cols].value_counts())
    df_usercount = user_count.reset_index()
    df_usercount.columns = ["Country", "User_count"]

    print(df_usercount)

    # classifying participants according to gender
    print(f"\nHow many genders took part in the survey?")
    print(data_setA["Gender"].value_counts())

    print("Done")


def rename_columns(data_frame):
    """
    Rename Columns for easy reading of columns.
    """
    data_frame.drop([0], inplace=True)
    data = data_frame.rename(
        columns={
            "Time from Start to Finish (seconds)": "Duration",
            "Q1": "Age",
            "Q2": "Gender",
            "Q3": "Country",
            "Q4": "Education",
            "Q5": "Job Title",
            "Q6": "Experience Years",
            "Q7_Part_1": "Python",
            "Q7_Part_2": "R",
            "Q7_Part_3": "SQL",
            "Q7_Part_4": "C",
            "Q7_Part_5": "C++",
            "Q7_Part_6": "Java",
            "Q7_Part_7": "Javascript",
            "Q7_Part_8": "Julia",
            "Q7_Part_9": "Swift",
            "Q7_Part_10": "Bash",
            "Q7_Part_11": "MATLAB",
            "Q7_Part_12": "None",
            "Q7_OTHER": "Other",
            "Q8": "Recommended",
        }
    )

    return data


if input_path is not None:
    data = read_input_path(input_path)
    sleep(2)
    data_frame = rename_columns(data)
    sleep(2)
    analyze_data(data_frame)
    sleep(2)

else:
    print("Please provide a valid input file.")
