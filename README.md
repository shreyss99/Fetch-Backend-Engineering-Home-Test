# Fetch-Backend-Engineering-Home-Test

## Points Calculation

#### Background:
     
    * Fetch users have points in their accounts. Users only see a single balance in their accounts. 
    * But for reporting purposes, Fetch actually track their points per payer. 
    * In system, each transaction record contains: payer (string), points (integer), timestamp (date). 
    * For earning points, it is easy to assign a payer. 
    * Fetch know which actions earned the points. And which partner should be paying for the points. 
    * When a user spends points, they do not know or care which payer the points come from. 
    
    * But, the accounting team does care how the points are spent. 
      There are two rules for determining what points to "spend" first: 
      1) We want the oldest points to be spent first (based on transaction timestamp, 
         not the order they are received) 
      2) We want no payer's points to go negative.

#### Program Requirements:

    * User must have command line tool -- Terminal or Command Prompt to execute the Python script.
    * The user must have Python 3.x version installed in their system to be able to run the code.
      If not refer:
  [Link](https://realpython.com/installing-python/) to download Python based on the OS.

    * Install the python module 'pandas' using the command via command line:
```
pip3 install pandas
```
    
#### Code Setup Steps:
  
    * Go to th below link for repository cloning:
  [Repository](https://github.com/shreyss99/Fetch-Backend-Engineering-Home-Test)
    
    * Click on the green 'Code' button and download the ZIP file.
    * Once downloaded, copy the ZIP file to any specific location and unzip it.
    * The contents will include: 
      1) README.md file (instructions)
      2) Python script with name 'main.py'
      3) Sample data file called 'transactions.csv'
      4) requirements.txt' file.
    * Ensure that the 'transactions.csv' file is in the same directory/path 
      as the Python script 'main.py'.
    
#### Program Execution:
    
    * Open the Terminal or Command Prompt.
    * Navigate to the directory containing Python script and sample data file using 'cd' command.
    * Execute the below line of code by specifying points to be spend in place of <points_to_spend>
```
python3 main.py <points_to_spend>
```
    * The program will execute and the results will be displayed.
    * To re-run the program with new data, the change can be made in the 'transactions.csv' file
      and the same command command can be used to run the program with different data.


## Code Logic

1. **File and Script Location:**

   - The program assumes that the sample `transactions.csv` file and the Python script `main.py` are located in the same directory.

2. **User-Defined Functions and Custom Exception Class:**

   - The code includes two user-defined functions and one custom Exception class.
   
   - `convert_file_to_dataframe(file_name):`
     - This function takes the name of a CSV file as input and returns a Python DataFrame. It reads the file using the `read_csv()` method from the Pandas module.

   - `calculate_points(input_dataframe, input_points):`
     - This function calculates the points spent based on the input DataFrame and the points to be spent.
     - It sorts the DataFrame in ascending order based on timestamp values, ensuring that row numbers remain unchanged using the `ignore_index` parameter.
     - The function iterates through the DataFrame using a `while` loop with the following conditions:
       - `input_points > 0`: Ensure there are points left to spend.
       - `iterator variable < length of input_dataframe`: Avoid index out-of-range errors.
     - If the points to spend are less than the points for a specific payer, it subtracts the input_points from the cell value and exits the loop.
     - If the points to spend are more than the points for a specific payer, it subtracts the cell value from the input_points and sets the points for that payer to 0.
     - After the loop, it groups the points by payer and calculates the total points remaining as the balance for each payer.
     - The result is a DataFrame containing payer names and their total balance points, which is then converted into a dictionary and returned.

   - `NegativePointsException(Exception)`:
     - This custom Exception class is used to check whether the points entered by the user as command-line arguments are greater than 0. It ensures that negative values are not allowed. If a negative value is provided, it raises an Exception with an appropriate error message, and the program terminates.

3. **Program Execution:**

   - The program starts execution from the main function.
   - It accepts the points as input from the command line.
   - The file name 'transactions.csv' is explicitly specified in the code. If the file is not present in the directory, it raises an Exception indicating that the file is not found, and the program terminates.
   - The `convert_file_to_dataframe(file_name)` function is called with the file name as an argument, which returns a DataFrame.
   - Then, the `calculate_points(input_dataframe, input_points)` function is called with the DataFrame and the command-line points as arguments, resulting in a final DataFrame converted to a dictionary for the final output.

## Usage

To run the program:

```bash
python main.py <points_to_spend>
    
