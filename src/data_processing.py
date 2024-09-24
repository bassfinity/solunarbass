# src/data_processing.py

from datetime import datetime

def process_solunar_data(data, date_str):
    # Extract necessary data
    try:
        day_data = data['days'][0]
        sunrise = day_data['sunrise']
        sunset = day_data['sunset']
        moonrise = day_data.get('moonrise')
        moonset = day_data.get('moonset')
        moon_phase = day_data['moonphase']

        # Define formats
        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'
        datetime_format = f'{date_format} {time_format}'

        # Combine date and time
        sunrise_dt = datetime.strptime(f"{date_str} {sunrise}", datetime_format)
        sunset_dt = datetime.strptime(f"{date_str} {sunset}", datetime_format)

        if moonrise:
            moonrise_dt = datetime.strptime(f"{date_str} {moonrise}", datetime_format)
        else:
            moonrise_dt = None

        if moonset:
            moonset_dt = datetime.strptime(f"{date_str} {moonset}", datetime_format)
        else:
            moonset_dt = None

        return {
            'sunrise': sunrise_dt,
            'sunset': sunset_dt,
            'moonrise': moonrise_dt,
            'moonset': moonset_dt,
            'moon_phase': moon_phase,
        }
    except Exception as e:
        print(f"Error processing solunar data: {e}")
        return None
