import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = "https://www.colorhexa.com/color-names"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that contains the color data
table = soup.find("table")

# Create a CSV file and write the table data to it
with open("color_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the column names to the CSV file
    columns = ["Color name", "Hex", "Red", "Green", "Blue", "Hue", "Saturation", "Lightness"]
    writer.writerow(columns)

    # Iterate through each row in the table and extract the cell values
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) > 1:
            # Extract the desired columns' values
            color_name = cells[0].text.strip()
            hex_code = cells[1].text.strip()
            rgb_values = [cell.text.strip() for cell in cells[2:5]]
            hue = cells[5].text.strip().replace("°", " (degrees)")
            saturation = cells[6].text.strip()
            lightness = cells[7].text.strip()

            # Write the row data to the CSV file
            writer.writerow([color_name, hex_code] + rgb_values + [hue, saturation, lightness])

print("Table data has been scraped and saved in color_data.csv.")
