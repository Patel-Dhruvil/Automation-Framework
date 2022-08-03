
import logging
import pytest

from apptest.TestData.ReadCsvData import CsvLookup
from collections import namedtuple
from apptest.PageObject.LoginPage import LoginPageTest
from harness.Driver.DriverClass import Driver

def getCsvData(csvPath):
    """
    Function will read all the rows and return the CSV data into list of tuple for all the rows of CSV.
    :param        csvPath(str): File name of the CSV.
    :return:
         csvData(list): List of the tuples as each rows of csv sheet.
    """
    csv = CsvLookup(csvPath)

    rawData = csv.getData()
    colName = csv.getColName()
    # print("Column names are : {}".format(colName))
    # Re-arrange the row values of the column from csv
    Data = [rawData[j][colName[i]] for i in range(len(colName)) for j in range(len(rawData))
            if colName[i] == list(rawData[j].keys())[i]]
    Data1 = [Data[j] for i in range(len(rawData)) for j in range(i, len(Data), len(rawData))]
    csvData = [tuple(Data1[i:i+len(colName)]) for i in range(0,len(Data1), len(colName))]

    logging.info("The Data Received from csv is...")
    return csvData


def get_csv_data_named_tuple(filename):
    """
    This function convert the data retrieved from CSV file into namedtuple.
    :return:
        csv_namedtuple_list(list): List of row data in namedtuple format.
    """
    csv = CsvLookup(filename)
    col_name = csv.getColName()
    csv_data = getCsvData(filename)

    Person = namedtuple("csv_dataclass", col_name)

    csv_namedtuple_list = [Person._make(i) for i in csv_data]
    # print(csv_namedtuple_list)
    return csv_namedtuple_list

# if __name__ == "__main__":
#
#     c = getCsvData("C:\\Users\\PycharmProjects\\Appium\\Appium_Automation_Framework\\apptest\\TestData\\sample_check.csv")
#
#     print("{}\n".format(c))

@pytest.mark.parametrize("email, password", getCsvData("enter your csv path here"))#path to CSV
def test_credentials(email, password):
    print(email, password)












