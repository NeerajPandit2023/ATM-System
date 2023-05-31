# ATM-System
The provided code appears to be a Python script that connects to a MySQL database and implements an ATM-like functionality using SQL queries. Here is a description of the code:

1. The code starts by importing the `mysql.connector` module, which provides the necessary functionality to connect and interact with a MySQL database.

2. It establishes a connection to the MySQL database by calling the `connect()` function with the appropriate connection parameters, such as the host, username, password, and database name.

3. A cursor object (`mycur`) is created to execute SQL queries on the database.

4. The script executes a SELECT query (`SELECT pin FROM cos_data`) to retrieve all the PINs from a table named `cos_data`. The result of the query is stored in the `write` variable as a list of tuples.

5. The code enters a loop that allows for up to 100 attempts to enter the correct PIN.

6. Inside the loop, it displays a welcome message and prompts the user to enter their PIN.

7. The code then iterates over the `write` list to check if the entered PIN matches any of the PINs retrieved from the database.

8. If a match is found, the script executes another SELECT query to retrieve the account information associated with the matched PIN.

9. The account information is displayed to the user, including the account holder's name, partially hidden account number, and available balance.

10. The script enters another loop that allows for up to 5 transactions per session.

11. Inside this loop, the user is prompted to choose a transaction type: withdraw, balance inquiry, fast cash, or credit amount.

12. Based on the user's choice, the script executes different SQL queries and performs the corresponding actions:

    a. For a withdraw transaction (option 1), the user is prompted to enter the withdrawal amount. If the requested amount is available and divisible by 100, the script updates the account balance, displays a success message, and prompts the user if they want to perform more transactions.
    
    b. For a balance inquiry (option 2), the script retrieves the current account balance from the database and displays it to the user. It then prompts if they want to perform more transactions.
    
    c. For a fast cash transaction (option 3), the user is prompted to choose a predefined amount (1-1000, 2-500, 3-2000, 4-5000). If the chosen amount is available, the script updates the account balance accordingly, displays a success message, and prompts if they want to perform more transactions.
    
    d. For a credit amount transaction (option 4), the user is prompted to enter the amount to be credited. The script retrieves the current account balance, adds the credit amount, updates the account balance in the database, displays the credited amount and the new available balance, and prompts if they want to perform more transactions.
    
13. If the user exceeds the maximum allowed transactions (5 in this case), the script breaks out of the inner loop and displays a message indicating that something went wrong and no more transactions can be performed.

14. If the entered PIN does not match any of the retrieved PINs from the database, the script displays a message indicating an incorrect PIN.

15. The outer loop continues until either a correct PIN is entered or the maximum number of attempts (100 in this case) is reached. In the latter case, the script displays a message indicating that the daily transactions are over.

Overall, the code represents a simple ATM-like system that interacts with a MySQL database to perform basic banking transactions such as withdrawals, balance inquiries, and credit transactions.
