# Exchange Rate Fetcher

## Overview

This Python script fetches historical exchange rates for Euro (EUR) from the National Bank of Poland API and saves the data to CSV and Excel files. It provides an easy way to retrieve and analyze exchange rate data for a specific time range.

## Features

- Fetches exchange rates for Euro (EUR) from the National Bank of Poland API.
- Saves exchange rate data to both CSV and Excel formats.
- Customizable date range for historical data retrieval.

## Usage

### 1. Clone the repository:

```bash
git clone https://github.com/jedrzej221/NBP-PLN-EUR-exchange-rate-fetcher.git
```
### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Run the script:
```bash
python exchange_rate_fetcher.py
```
## Configuration
You can customize the script by modifying the following variables in exchange_rate_fetcher.py:

`start_date`: Start date for exchange rate retrieval (default: '2023-01-01').

`end_date`: End date for exchange rate retrieval (default: current date).

## Files 

`exchange_rate_fetcher.py`: Main Python script.

`requirements.txt`: List of project dependencies.

`.gitignore`: Git ignore file to exclude unnecessary files and directories.

`README.md`: Project documentation.

## Dependencies

`requests`: Library for making HTTP requests.

`pandas`: Data manipulation library.

## License

This project is licensed under the MIT License.