💳 Credit Card Management System
✨ Project Overview
This project is a Credit Card Management System designed to simulate basic credit card operations using Python. It allows users to create new credit card accounts, log in with their card number and PIN, and perform various transactions and management tasks. All card data, including limits, balances, rewards, and status, is persistently stored in a local text file (cards.txt).

🌟 Features
The system offers the following core functionalities:

Card Creation: Allows a user to create a new card by providing a card number, name, PIN, and credit limit.

Persistent Storage: Card data is saved to and loaded from a local file (cards.txt), ensuring data is preserved between sessions.

Login System: Securely access card features using the card number and PIN.

Transactions:

Purchase: Records a purchase amount. If the purchase exceeds the credit limit, it's rejected, and the credit score is penalized. Successful purchases earn rewards.

Payment: Reduces the current balance and rewards the user with a slight credit score increase.

Card Status Management: Allows users to Block or Unblock their card. Blocked cards cannot be used for purchases.

Interest Calculation: Applies a 3% interest charge to the current balance.

View Details: Displays the card number, name, credit limit, current balance, rewards balance, credit score, and blocked status.

🛠️ Technologies / Tools Used
Language: Python 3.x

Storage: Text File (cards.txt) for simple data persistence.

🚀 Steps to Install & Run the Project
Follow these steps to get the system running on your local machine.

Prerequisites
You must have Python 3.x installed on your system.

Installation and Execution
Save the Code: Save the provided Python code into a file named krishna.py.

Create Data File: The program uses a text file named cards.txt to store card data. Ensure this file exists in the same directory as krishna.py. If it doesn't exist, the program will typically create it upon the first successful card creation.

Run the Program: Open your terminal or command prompt, navigate to the directory where you saved the files, and execute the command
