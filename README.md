# WebBy - Medicine Information Scraper

## Project Overview
The **WebBy** web scraper is designed to retrieve information about medicines, including their uses and side effects, from two data sources: a local text file or a website. It offers flexibility in sourcing data and can either extract information from a text file stored locally or scrape data directly from the web using BeautifulSoup.

## Features
- **Data Source Options:**
  - **Text File:** Fetch medicine information from a pre-defined text file (`WebBy.txt`).
  - **Website Scraping:** Scrapes medicine data directly from a website (like drugs.com).
- **Error Handling:** The system is designed to handle missing files, format issues, and connection problems.
- **Flexible Usage:** Choose between a local data source (`WebBy.txt`) or website scraping by specifying the source during runtime.

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:
```bash
 git clone https://github.com/Zai14/WebBy.git
```
2. Navigate to the project directory:
 ```bash
cd WebBy
  ```
3. Install the required dependencies:
 ```bash
pip install -r requirements.txt
  ```
## Make sure you have a file named WebBy.txt in the correct format:
  ```makefile
medicine_name:uses:side_effects
  ```
## Example:
```makefile
Paracetamol:Pain relief:Nausea, drowsiness
```
## Usage
**1) Run the script:**    
```bash
python WebBy.py
```
**2) Input the Medicine Name:** 
```
-Enter the name of the medicine you want information on.
```
**3) Choose the Data Source:**     
```
-Enter text to search from WebBy.txt, or website to scrape information from a website.
```
**4) View Results:**       
```
-Displays the uses and side effects of the medicine from the chosen data source.
```
## Technologies Used
**1) Python:** Main programming language used for building the application.
**2) BeautifulSoup:** For scraping data from websites.
**3) Requests:** To handle HTTP requests to fetch web pages.
## Project Structure
```bash
WebBy/
│
├── WebBy.py                 # Main application script for scraping
├── WebBy.txt                # Local text file containing medicine information (if applicable)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
## Future Enhancements
Implement more robust web scraping capabilities for different medicine information websites.
Add a graphical user interface (GUI) for ease of use.
Expand error handling to improve system reliability.
## License
This project is licensed under the MIT License.
## Contact
For more information, please contact Zai14 through his **Socials:**
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/Za.i.14) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/Za.i.14) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/zai14) [![Pinterest](https://img.shields.io/badge/Pinterest-%23E60023.svg?logo=Pinterest&logoColor=white)](https://pinterest.com/Za.i.14) [![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/Za_i14) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@Za.i.14) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:ZaidShabir67@gmail.com) 
.
