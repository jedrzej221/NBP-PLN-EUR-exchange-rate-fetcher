import os
import requests
import csv
import pandas as pd
from datetime import datetime


def get_exchange_rate(start_date, end_date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/eur/{start_date}/{end_date}/'
    response = requests.get(url)
    data = response.json()
    return data['rates']


def save_to_csv(rates):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = os.path.join(desktop_path, f'exchange_rates_{timestamp}.csv')

    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Effective Date', 'Currency', 'Exchange Rate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for rate in rates:
            writer.writerow({'Effective Date': rate['effectiveDate'], 'Currency': 'EUR', 'Exchange Rate': rate['mid']})

    print(f'Data saved to {csv_filename}')


def save_to_excel(rates):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_filename = os.path.join(desktop_path, f'exchange_rates_{timestamp}.xlsx')

    df = pd.DataFrame(rates, columns=['effectiveDate', 'mid'])
    df.columns = ['Effective Date', 'Exchange Rate EUR/PLN']

    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Exchange Rates', index=False)

    print(f'Data saved to {excel_filename}')


if __name__ == '__main__':
    start_date = '2023-01-01'
    end_date = datetime.now().strftime("%Y-%m-%d")

    exchange_rates = get_exchange_rate(start_date, end_date)

    save_to_csv(exchange_rates)
    save_to_excel(exchange_rates)
