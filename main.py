import sys
import pandas as pd


class NegativePointsException(Exception):
    """
    Raised when the input value is less than 0
    """
    print("Exception occurred: Points to spend cannot be Negative")


def convert_file_to_dataframe(file_name):
    """
        Returns the dataframe created from the file_name specified

                Parameters:
                        file_name (str): A string storing the file_name

                Returns:
                        input_dataframe (DataFrame): The dataframe created from the file_name

    """

    input_dataframe = pd.DataFrame()
    try:
        input_dataframe = pd.read_csv(file_name)
    except FileNotFoundError:
        print("The file {0} is not located in the current working directory".format(file_name))
    return input_dataframe


def calculate_points(input_dataframe, input_points):
    """
       Returns the dataframe consisting the points remaining grouped by payer after computation
       based on rules:
       1) The oldest points will be spent first
       2) No payer's points will be negative


               Parameters:
                       input_dataframe (DataFrame): The dataframe containing the transactions details
                       input_points (int): An integer containing the points to be spent
               Returns:
                       result (DataFrame): A dataframe consisting the points remaining grouped by payer

    """

    sorted_dataframe = input_dataframe.sort_values(by='timestamp', ignore_index=True)

    i = 0
    while input_points > 0 and i < len(sorted_dataframe):
        if sorted_dataframe.at[i, 'points'] > input_points:
            sorted_dataframe.at[i, 'points'] -= input_points
            break
        else:
            input_points -= sorted_dataframe['points'][i]
            sorted_dataframe.at[i, 'points'] -= sorted_dataframe.at[i, 'points']
        i += 1

    final = sorted_dataframe.groupby('payer').sum('points')
    result = final.reset_index()

    return result


if __name__ == '__main__':

    '''
       Takes command line input when executing the program
       Converts it to an integer as by default command line inputs are read as strings
    '''
    try:
        points_total = int(sys.argv[1])
        if points_total < 0:
            raise NegativePointsException
    except NegativePointsException:
        exit()

    '''
        Store the dataframe to transactions variable by passing 
        file name as input to the convert_file_to_dataframe() function
    '''
    transactions = convert_file_to_dataframe("transactions.csv")

    '''
        Store the result of the computation in solution variable by passing
        the input dataframe and the command line as inputs
    '''
    solution = calculate_points(transactions, points_total)

    '''Display the solution'''
    print(solution)
