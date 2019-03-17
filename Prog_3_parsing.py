# -*- coding: utf-8 -*-
"""
Program to work with parsing the data 

PARSING:
--------
Parse
Analyse (a string or text) into logical syntactic components.

[----I don’t like the above Oxford dictionary definition. So, here is my alternate definition----]

Parse
Convert data in a certain format into a more usable format.
Usually, real-time data is huge and identify specific type of data looking for is a difficult task. 
In this test case, we use pandas, numpy and RE to seperate string data or combined data to seperate lists for easy understanding and manipulating

Author: Kriyative Edge

"""
#NOTE: Refer the below website for any type of real time datasets for understanding data, parsing data and understand real-time standards of 
# analytics and machine learning
"""
https://archive.ics.uci.edu/ml/datasets.html
"""

########################################################
#The dataset is some school students information with data in comma seperated format.
#But theinformation is combined such that seperating list among the set is a major task
#For this task, we use Regular Expressions library to parse the data

########################################################

#Intial test to observe the data set
with open('school.txt') as file:
    file_contents = file.read()
    print(file_contents)


#Working with RE
import re
import pandas as pd

# set up regular expressions
# use https://regexper.com to visualise these if required
rx_dict = {
    'school': re.compile(r'School = (?P<school>.*)\n'),
    'grade': re.compile(r'Grade = (?P<grade>\d+)\n'),
    'name_score': re.compile(r'(?P<name_score>Name|Score)'),
}

def _parse_line(line):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex

    """

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    # if there are no matches
    return None, None

def parse_file(filepath):
    """
    Parse text at given filepath

    Parameters
    ----------
    filepath : str
        Filepath for file_object to be parsed

    Returns
    -------
    data : pd.DataFrame
        Parsed data

    """

    data = []  # create an empty list to collect the data
    # open the file and read through it line by line
    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        while line:
            # at each line check for a match with a regex
            key, match = _parse_line(line)

            # extract school name
            if key == 'school':
                school = match.group('school')

            # extract grade
            if key == 'grade':
                grade = match.group('grade')
                grade = int(grade)

            # identify a table header 
            if key == 'name_score':
                # extract type of table, i.e., Name or Score
                value_type = match.group('name_score')
                line = file_object.readline()
                # read each line of the table until a blank line
                while line.strip():
                    # extract number and value
                    number, value = line.strip().split(',')
                    value = value.strip()
                    # create a dictionary containing this row of data
                    row = {
                        'School': school,
                        'Grade': grade,
                        'Student number': number,
                        value_type: value
                    }
                    # append the dictionary to the data list
                    data.append(row)
                    line = file_object.readline()

            line = file_object.readline()

        # create a pandas DataFrame from the list of dicts
        data = pd.DataFrame(data)
        # set the School, Grade, and Student number as the index
        data.set_index(['School', 'Grade', 'Student number'], inplace=True)
        # consolidate df to remove nans
        data = data.groupby(level=data.index.names).first()
        # upgrade Score from float to integer
        data = data.apply(pd.to_numeric, errors='ignore')
    return data

if __name__ == '__main__':
    filepath = 'school.txt'
    data = parse_file(filepath)
    print(data)















