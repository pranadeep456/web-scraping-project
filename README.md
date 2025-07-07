# 🕸️ Web Scraping - Indian IT Companies

This Python project scrapes data from [Wikipedia's list of Indian IT companies](https://en.wikipedia.org/wiki/List_of_Indian_IT_companies), extracts the structured table, and saves it as an Excel file.

## 📌 Features
- Scrapes data from a live Wikipedia page
- Extracts company names and related details from a specific table
- Saves the data into an Excel file using `pandas`
- Prints the "Last updated" info from the page footer

## 📊 Output
The data is saved as an Excel file:
C:\Users\LENOVO\Desktop\Indian_IT_companies.xlsx

## 🧰 Libraries Used
- `requests` – for fetching the webpage
- `beautifulsoup4` – for parsing HTML
- `pandas` – for data storage and Excel export

## 🚀 How to Run

### 1. Install dependencies:
```bash
pip install requests beautifulsoup4 pandas openpyxl

openpyxl is required for writing to Excel using to_excel().
