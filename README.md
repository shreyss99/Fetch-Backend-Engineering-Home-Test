# Fetch-Backend-Engineering-Home-Test

## Points Calculation

#### Background:
     
    * Fetch users have points in their accounts. Users only see a single balance in their accounts. 
    * But for reporting purposes, Fetch actually track their points per payer. 
    * In the system, each transaction record contains: payer (string), points (integer), timestamp (date). 
    * For earning points, it is easy to assign a payer. 
    * Fetch know which actions earned the points. And which partner should be paying for the points. 
    * When a user spends points, they do nott know or care which payer the points come from. 
    
    * But, the accounting team does care how the points are spent. 
      There are two rules for determining what points to "spend" first: 
      1) We want the oldest points to be spent first (based on transaction timestamp, 
         not the order they are received) 
      2) We want no payer's points to go negative.

#### Program Requirements:

    * The user must have Pythom 3.x version installed in their system to be able to run the code.
    * User must have a command line tool like Terminal or Command Prompt to execute the Python script.
    
#### Code Setup Steps:

    * Go to the link https://github.com/shreyss99/Fetch-Backend-Engineering-Home-Test 
    * Click on the green 'Code' button and download the ZIP file.
    * Once downloaded, copy the ZIP file to any specific location and unzip it.
    * The contents will include: 
      1) README.md file (instructions)
      2) Python script with name 'main.py'
      3) Sample data file called 'transactions.csv'
      4) requirements.txt' file.
    * Ensure that the 'transactions.csv' file is in the same directory/path as the Python sript 'main.py'.
    
#### Program Execution:
    
    * Open the Terminal or Command Prompt.
    * Navigate to the directory containing the Python script and the sample data file using the 'cd' command.
    * 
    
