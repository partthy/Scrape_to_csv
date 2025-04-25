# README: Extracting and Saving Headlines from a Text Based Website

## Overview
This script extracts headlines from the Al Jazeera website as an example and saves them to a CSV file named `headline.csv`. The script leverages web scraping techniques using Python libraries: `requests` and `BeautifulSoup`.

---

## Requirements
- Python 3.6 or higher
- Libraries:
  - `requests`: For making HTTP requests
  - `BeautifulSoup` (from `bs4`): For parsing HTML content
  - `csv`: For writing extracted data to a CSV file

---

## Functionality
1. **Fetch HTML Content:**
   - Sends an HTTP GET request to `https://www.aljazeera.com/`.
   - Checks response status code to ensure successful request.

2. **Parse HTML:**
   - Uses `BeautifulSoup` to parse the HTML content.

3. **Extract Headlines:**
   - Finds all `h3` tags with the class `"article-card__title"`.
   - The class tag will change according to the website. Insepet the website and use the appropiate tags and class required.
   - Extracts and cleans text content from these tags.

4. **Save to CSV:**
   - Writes the extracted headlines into a CSV file (`headline.csv`) with a single column (`Headline`).

5. **Output:**
   - Prints the number of headlines extracted and saved.

---

## Usage
1. Clone or copy this script to your local environment.
2. Ensure the required libraries are installed:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the script:
   ```bash
   python script_name.py
   ```
4. Check the `headline.csv` file in the script's directory for the extracted headlines.

---

## Notes
- This script relies on the structure of the website at the time of writing. If the website's HTML structure changes, updates to the code might be necessary.
- Ensure compliance with website terms of use before scraping data.

---
