import sys
import pandas as pd


def convert_file_to_dataframe(file_name):
    input_dataframe = pd.DataFrame()
    try:
        input_dataframe = pd.read_csv(file_name)
    except FileNotFoundError:
        print("The file {0} is not located in the current working directory".format(file_name))
    return input_dataframe


def calculate_points(input_dataframe, input_points):
    sorted_transactions = transactions.sort_values(by='timestamp', ignore_index=True)

    i = 0
    while input_points > 0:
        if input_dataframe.at[i, 'points'] > input_points:
            input_dataframe.at[i, 'points'] -= input_points
            break
        else:
            input_points -= input_dataframe['points'][i]
            input_dataframe.at[i, 'points'] -= input_dataframe.at[i, 'points']
        i += 1

    final = input_dataframe.groupby('payer').sum('points')
    result = final.reset_index()

    return result


if __name__ == '__main__':
    points_total = int(sys.argv[1])

    transactions = convert_file_to_dataframe("transactions.csv")

    solution = calculate_points(transactions, points_total)

    print(solution)
