📚 Amazon Books Scraper using Selenium

This project is a Python automation script that uses Selenium WebDriver to scrape book titles and prices from Amazon. The script navigates through Google, opens Amazon, searches for books, extracts product information, and saves the data into an Excel file using OpenPyXL.

🚀 Features

Automated browser control using Selenium

Searches Amazon Books automatically

Extracts Book Titles and Prices

Saves the data to an Excel (.xlsx) file

Demonstrates basic web scraping and automation

🛠️ Technologies Used

Python

Selenium

OpenPyXL

Chrome WebDriver

📂 Project Workflow

Open Google using Selenium.

Search for Amazon.

Click the Amazon website link.

Search for Books on Amazon.

Extract:

Book Titles

Book Prices

Save the extracted data to Excel file.

📦 Installation

1️⃣ Clone the repository
git clone : https://github.com/Mohamed-Shahid8668/Web-Scraping.git

2️⃣ Install dependencies
pip install -r requirements.txt

📄 Requirements

Create a requirements.txt file with:

selenium
openpyxl

▶️ Run the Script
python Scraping.py


After execution, an Excel file will be created:

books with prices.xlsx

📊 Example Output

Book Name	Price
Python Programming	₹450
Data Science Handbook	₹799

⚠️ Note

Amazon frequently updates its HTML structure. If elements are not detected, the CSS selectors or XPath may need to be updated.

Author

Mohamed Sahid M
