# api_request.py_task-12
📌 Public API Demo using Python requests
📄 Project Title

Public API Demo using Requests Library

🧠 Project Description

This project demonstrates how to use the Python requests library to consume a free public API, handle HTTP responses, parse data, manage network errors, and display clean output using PowerShell / VS Code.

The project uses a reliable public API to avoid network restrictions commonly faced in college or hostel networks.

🛠️ Technologies Used

Python 3.14

requests library

Windows PowerShell

Visual Studio Code

📁 Project Structure
api_requests_demo.py   (folder)
└── api_requests_demo.py   (python file)
README.md

🌐 Public API Used

GitHub Zen API

URL:

https://api.github.com/zen


Method: GET

Authentication: ❌ Not required

Response Type: Plain text

✨ Features

Uses requests.get() to fetch data from API

Checks HTTP status codes

Handles network-related errors gracefully

Uses try–except for robustness

Displays clean, formatted output

Runs successfully in VS Code & PowerShell

▶️ How to Run (PowerShell)
🔹 Step 1: Open PowerShell

Start Menu → Windows PowerShell

OR VS Code → Ctrl + `

🔹 Step 2: Navigate to project folder
cd C:\Users\manoj\OneDrive\Desktop\api_requests_demo.py

🔹 Step 3: Install requests (run once)
python -m pip install requests

🔹 Step 4: Run the program
python api_requests_demo.py

▶️ How to Run (VS Code)

Open VS Code

Click File → Open Folder

Select api_requests_demo.py

Open terminal (Ctrl + `)

Run:

python api_requests_demo.py

🧪 Sample Output
=== Public API Demo using requests ===

📜 Zen Quote
----------------------------------------
Approachable is better than simple.

⚠️ Error Handling

The program handles:

Network connection errors

Timeouts

API unavailability

Unexpected request failures

Example:

❌ Network error or API blocked

🎯 Learning Outcomes

Installing and using third-party Python libraries

Sending HTTP GET requests

Understanding API status codes

Handling real-world network issues

Running Python programs via PowerShell

Using VS Code as a Python IDE

🧠 Exam / Viva One-Liners

requests is used to send HTTP requests in Python.

APIs return data that can be processed programmatically.

Exception handling is required for network reliability.

PowerShell is used to execute Python programs in Windows.

👨‍💻 Author

Manoj

🚀 Future Enhancements

Weather API integration

Random User API

Menu-driven program

Logging API responses

Unit testing with unittest
