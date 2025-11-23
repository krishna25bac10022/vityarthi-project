

Problem Statement

Managing credit card activities such as payments, purchases, rewards, interest calculation, and credit score updates can be difficult and error-prone when done manually. Users often lack a simple system to track their spending, outstanding balance, credit utilization, and card status (blocked/unblocked).
There is a need for a lightweight software tool that helps users efficiently manage their credit card operations in a structured and transparent manner.


---

Scope of the Project

The Smart Credit Card Management System is a console-based Python application designed to simulate essential credit card functionalities.
The scope includes:

Creating and storing credit card records

Secure login using card number and PIN

Performing transactions (purchase & payment)

Viewing card details such as balance, rewards, limit, and credit score

Blocking and unblocking cards

Automatic interest calculation

Storing all card data in a persistent text file (cards.txt)


The project focuses on core card operations and does not include multi-user networks, GUI, or online integration.


---

Target Users

This system is designed for:

Students learning file handling, functions, and basic application logic

Individuals wanting a simple tool to track card usage

Educators who want to demonstrate real-world financial system logic

Beginner developers practicing modular programming and menu-based systems



---

 High-Level Features

Card Creation
Allows users to set up a credit card with name, PIN, limit, and initial score.

User Authentication
Login using card number and PIN for secure access.

Purchase Module
Validates limit, updates balance, and awards reward points.

Payment Module
Processes payments, reduces balance, and increases credit score.

Interest Calculation
Applies 3% monthly interest to outstanding balance.

Card Blocking/Unblocking
Prevents transactions when the card is marked as blocked.

Card Information Display
Shows card number, name, balance, limit, rewards, score, and block status.

Persistent Storage
Saves and loads all records using a text file (cards.txt).
