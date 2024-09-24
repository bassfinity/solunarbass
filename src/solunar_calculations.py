# src/solunar_calculations.py

from datetime import timedelta

def calculate_major_minor_times(solunar_data):
    major_times = []
    minor_times = []

    # Major times occur when the moon is overhead and underfoot
    # Approximate times using moonrise and moonset
    if solunar_data['moonrise'] and solunar_data['moonset']:
        moonrise = solunar_data['moonrise']
        moonset = solunar_data['moonset']

        # Major Periods
        major_times.append({
            'start': moonrise - timedelta(hours=1),
            'end': moonrise + timedelta(hours=1)
        })
        major_times.append({
            'start': moonset - timedelta(hours=1),
            'end': moonset + timedelta(hours=1)
        })

        # Minor Periods occur halfway between major periods
        transit_time = moonrise + (moonset - moonrise) / 2
        minor_times.append({
            'start': transit_time - timedelta(minutes=30),
            'end': transit_time + timedelta(minutes=30)
        })

    return major_times, minor_times
