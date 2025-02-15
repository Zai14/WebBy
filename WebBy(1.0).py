from bs4 import BeautifulSoup
import requests

# Function to scrape medicine information
def scrape_med_info(medicine_name, data_source):
    # Data source is a text file
    if data_source == "text":
        try:
            with open(r'C:\Users\zaids\Documents\PY\WebScraper\WebBy.txt', 'r') as file:
                for line in file:
                    med_info = line.strip().split(':')
                    if len(med_info) == 3:
                        if med_info[0].lower() == medicine_name.lower():
                            return med_info[1], med_info[2]
                    else:
                        print("Error: Invalid format in 'WebBy.txt'. Please ensure the file follows the format: medicine_name:uses:side_effects")
                        return None, None
        except FileNotFoundError:
            print("Error: 'WebBy.txt' file not found.")
            return None, None
        except Exception as e:
            print("An error occurred:", e)
            return None, None

    # Data source is a website
    elif data_source == "website":
        try:
            url = f"https://www.drugs.com/search.php?searchterm={medicine_name}"
            response = requests.get(url)
            if response.status_code != 200:
                print("Error: Failed to retrieve data from the website. Please check the URL or internet connection.")
                return None, None

            soup = BeautifulSoup(response.text, 'html.parser')
            # Modify this part according to the actual structure of the website
            # Example (pseudo scraping logic, modify as needed):
            uses_section = soup.find('div', {'class': 'uses-section'})
            side_effects_section = soup.find('div', {'class': 'side-effects-section'})

            uses = uses_section.text.strip() if uses_section else "Uses information not found on website"
            side_effects = side_effects_section.text.strip() if side_effects_section else "Side effects information not found on website"

            return uses, side_effects

        except Exception as e:
            print("An error occurred while scraping the website:", e)
            return None, None

    else:
        print("Error: Invalid data source specified.")
        return None, None

# Main function
def main():
    medicine_name = input("Enter the name of the medicine: ")
    data_source = input("Enter the data source (text/website): ").lower()

    # Scrape based on data source
    if data_source == "text":
        uses, side_effects = scrape_med_info(medicine_name, "text")
    elif data_source == "website":
        uses, side_effects = scrape_med_info(medicine_name, "website")
    else:
        print("Invalid data source specified.")
        return

    # Print results
    if uses and side_effects:
        print(f"Uses of {medicine_name}: {uses}")
        print(f"Side effects of {medicine_name}: {side_effects}")
    elif uses is None and side_effects is None:
        print("Medicine information not found.")
    else:
        print("Error: Information could not be retrieved.")

# Run the script
if __name__ == "__main__":
    main()
