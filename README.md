# Fetch-Backend-Engineering-Home-Test

## Points Calculation

#### Background:
     
    * Fetch users have points in their accounts. Users only see a single balance in their accounts. 
    * But for reporting purposes, Fetch actually track their points per payer. 
    * In system, each transaction record contains: payer (string), points (integer), timestamp (date). 
    * For earning points, it is easy to assign a payer. 
    * Fetch know which actions earned the points. And which partner should be paying for the points. 
    * When a user spends points, they do nott know or care which payer the points come from. 
    
    * But, the accounting team does care how the points are spent. 
      There are two rules for determining what points to "spend" first: 
      1) We want the oldest points to be spent first (based on transaction timestamp, 
         not the order they are received) 
      2) We want no payer's points to go negative.

#### Program Requirements:

    * User must have command line tool -- Terminal or Command Prompt to execute the Python script.
    * The user must have Pythom 3.x version installed in their system to be able to run the code.
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
      as the Python sript 'main.py'.
    
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
    
