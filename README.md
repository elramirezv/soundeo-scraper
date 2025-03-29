# Soundeo Scraper

A Python-based scraper for downloading music from your Soundeo account.

## Requirements

- Python 3.12+
- Chrome browser

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/elramirezv/soundeo-scraper
   cd soundeo-scraper
   ```

2. Create and activate a virtual environment:
   ```
   python -m virtualenv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.py` file to set the download directory:

```python
DOWNLOAD_DIR = "/path/to/your/download/directory"
```

## Authentication Setup

Before running the scraper, you need to authenticate with Soundeo:

1. Run the authentication script:
   ```
   python soundeo_auth.py
   ```

2. The script will open a Chrome browser window. It will automatically:
   - Navigate to Soundeo
   - Click on the login link
   - Enter the credentials
   - Save your session cookies to `soundeo_cookies.pkl`

3. Once the login is complete, the browser will close automatically.

## Running the Scraper

After setting up authentication, you can run the scraper:

```
python main.py
```

The script will:
1. Load your saved cookies from `soundeo_cookies.pkl`
2. Navigate to your downloads page on Soundeo
3. Download all your purchased AIFF files
4. Skip files that have already been downloaded

## Note

- The scraper is configured to download AIFF files.
- It will automatically navigate through all pages of your downloads.
- Files that already exist in your download directory will be skipped.
