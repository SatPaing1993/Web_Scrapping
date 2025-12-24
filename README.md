

🛒 CityMall Product Scraper (Python)

This project is a Python web scraping script that collects product names and product prices from the CityMall Myanmar website, scrapes data from multiple pages, and exports the results into an Excel file.

📌 Features

Scrapes product names and prices from CityMall

Automatically handles pagination (Next pages)

Detects discounted prices and regular prices

Includes retry logic for network errors

Saves scraped data into an Excel file

🛠️ Technologies Used

Python 3

requests

BeautifulSoup (bs4)

pandas

urllib3 (Retry mechanism)

html5lib

📦 Required Libraries

Install the required libraries using:

pip install requests beautifulsoup4 pandas html5lib

🌐 Target Website
https://www.citymall.com.mm/citymall/my/c/id05011

📁 Output File

After running the script, the following file will be created:

CityMall Products List.xlsx


The Excel file contains:

Product Name

Product Prices

⚙️ How the Script Works
1️⃣ Session & Retry Configuration

Uses a custom User-Agent to avoid blocking

Automatically retries failed requests (HTTP 429, 500, 502, 503, 504)

2️⃣ Product Data Extraction

Product Name

extract_name()


Product Price (Sale / Normal)

extract_sale_price()


The script checks whether a product has a discounted price.
If not, it uses the normal price.

3️⃣ Pagination Handling

Detects the Next Page button

Continues scraping until no more pages are found

Adds a 2-second delay between requests to avoid overloading the server

4️⃣ Data Cleaning

Removes:

Ks

commas ,

Converts price values to float for analysis

5️⃣ Export to Excel

Stores data in a pandas DataFrame

Exports the result to an Excel file using:

df.to_excel("CityMall Products List.xlsx", index=False)

▶️ How to Run the Script
python your_script_name.py


If the process is successful, you will see:

Completed

⚠️ Notes

Website HTML structure may change; class names might need updates

Always respect the website’s Terms & Conditions

Use scraping responsibly

👨‍💻 Author

Beginner-friendly Python Web Scraping Project

Useful for learning:

Web Scraping

Data Collection

Data Analysis preparation
