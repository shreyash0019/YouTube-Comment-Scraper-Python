# YouTube Comment Scraper

This script scrapes comments from a YouTube video using Selenium and saves them to a CSV file.

## Prerequisites

1. [Python](https://www.python.org/) installed on your system.
2. [Selenium](https://selenium-python.readthedocs.io/) library.
3. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) executable matching your Chrome version.
4. A YouTube video URL to scrape comments from.

## Installation

1. Install Selenium:
    ```bash
    pip install selenium
    ```
2. Download the ChromeDriver and place it in a known location.

## Usage

1. Replace the `driver = webdriver.Chrome(r"C:/path/to/chromedriver.exe")` line with the path to your ChromeDriver executable.
2. Replace the `driver.get('https://www.youtube.com/watch?v=iFPMz36std4')` line with the URL of the YouTube video you want to scrape comments from.
3. Run the script:
    ```bash
    python youtube_comment_scraper.py
    ```
4. The comments will be saved to `C:/Users/hp/Desktop/commentlist.csv`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

