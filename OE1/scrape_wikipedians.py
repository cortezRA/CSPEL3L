import requests
import csv
from bs4 import BeautifulSoup

# Send a GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/Wikipedia:List_of_Wikipedians_by_number_of_edits/1–1000"
response = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the user data
table = soup.find("table", class_="wikitable")

if table:
    csv_file = "wikipedians.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "User", "Edit Count", "User Groups"])  # Write header row

        # Iterate over the rows skipping the header row
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) == 4:
                number = cells[0].text.strip()
                user = cells[1].text.strip()
                edit_count = cells[2].text.strip()
                user_groups = cells[3].text.strip()

                writer.writerow([number, user, edit_count, user_groups])

    print("Scraping complete. Data saved in", csv_file)
else:
    print("Table not found. Please check the HTML structure of the page.")
