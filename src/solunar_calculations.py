# src/solunar_calculations.py

from datetime import timedelta

def calculate_major_minor_times(solunar_data):
    major_times = []
    minor_times = []

    if not solunar_data:
        return major_times, minor_times

    # Major times occur when the moon is overhead and underfoot
    # Approximate times using moonrise and moonset
    if solunar_data['moonrise']:
        moonrise = solunar_data['moonrise']
        major_times.append({
            'start': moonrise - timedelta(hours=1),
            'end': moonrise + timedelta(hours=1)
        })

    if solunar_data['moonset']:
        moonset = solunar_data['moonset']
        major_times.append({
            'start': moonset - timedelta(hours=1),
            'end': moonset + timedelta(hours=1)
        })

    # Minor Periods occur halfway between major periods
    if len(major_times) == 2:
        transit_time = major_times[0]['end'] + (major_times[1]['start'] - major_times[0]['end']) / 2
        minor_times.append({
            'start': transit_time - timedelta(minutes=30),
            'end': transit_time + timedelta(minutes=30)
        })

    return major_times, minor_times
