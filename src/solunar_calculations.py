from datetime import timedelta
import math


def calculate_major_minor_times(solunar_data):
    major_times = []
    minor_times = []

    if not solunar_data:
        return major_times, minor_times

    # Try to use moonrise and moonset data first
    if solunar_data.get('moonrise') and solunar_data.get('moonset'):
        moonrise = solunar_data['moonrise']
        moonset = solunar_data['moonset']

        # Major periods: moon overhead (moonrise) & underfoot (moonset)
        major_times.append({
            'start': moonrise - timedelta(hours=1),
            'end': moonrise + timedelta(hours=1)
        })
        major_times.append({
            'start': moonset - timedelta(hours=1),
            'end': moonset + timedelta(hours=1)
        })

        # Calculate minor periods (halfway between major periods)
        # First minor: between moonset and next moonrise
        if moonset < moonrise:
            transit_time = moonset + (moonrise - moonset) / 2
        else:
            # If moonrise is before moonset, calculate for next day's cycle
            transit_time = moonrise + timedelta(hours=6)

        minor_times.append({
            'start': transit_time - timedelta(minutes=30),
            'end': transit_time + timedelta(minutes=30)
        })

        # Second minor: between moonrise and moonset
        if moonset > moonrise:
            transit_time2 = moonrise + (moonset - moonrise) / 2
        else:
            transit_time2 = moonset + timedelta(hours=6)
        minor_times.append({
            'start': transit_time2 - timedelta(minutes=30),
            'end': transit_time2 + timedelta(minutes=30)
        })

    else:
        # Fallback calculation when moonrise/moonset data is not available
        # Use standard solunar theory approximations based on moon phase
        moon_phase = solunar_data.get('moon_phase', 0.5)
        sunrise = solunar_data.get('sunrise')
        sunset = solunar_data.get('sunset')

        if sunrise and sunset:
            # Calculate approximate moon overhead times based on moon phase
            # Full moon (0.5) rises at sunset and sets at sunrise
            # New moon (0.0 or 1.0) rises at sunrise and sets at sunset

            # Calculate approximate moonrise time based on phase
            # This is a simplified calculation
            moonrise_offset = 12 * moon_phase  # hours after sunrise
            approx_moonrise = sunrise + timedelta(hours=moonrise_offset)

            # Moon overhead is approximately 6 hours after moonrise
            moon_overhead = approx_moonrise + timedelta(hours=6)
            # Moon underfoot is 12 hours after overhead
            moon_underfoot = moon_overhead + timedelta(hours=12)

            # Adjust times to be within the day
            if moon_overhead.date() == sunrise.date():
                major_times.append({
                    'start': moon_overhead - timedelta(hours=1),
                    'end': moon_overhead + timedelta(hours=1)
                })

            if moon_underfoot.date() == sunrise.date():
                major_times.append({
                    'start': moon_underfoot - timedelta(hours=1),
                    'end': moon_underfoot + timedelta(hours=1)
                })

            # Calculate minor periods as midpoints
            if len(major_times) >= 1:
                # First minor is 6 hours before first major
                minor1 = major_times[0]['start'] - timedelta(hours=5)
                if minor1.date() == sunrise.date() and minor1 > sunrise:
                    minor_times.append({
                        'start': minor1 - timedelta(minutes=30),
                        'end': minor1 + timedelta(minutes=30)
                    })

                # Second minor is 6 hours after first major
                minor2 = major_times[0]['end'] + timedelta(hours=5)
                sunset_plus_2 = sunset + timedelta(hours=2)
                if (minor2.date() == sunrise.date() and
                        minor2 < sunset_plus_2):
                    minor_times.append({
                        'start': minor2 - timedelta(minutes=30),
                        'end': minor2 + timedelta(minutes=30)
                    })

    # Sort all times by start time
    major_times.sort(key=lambda x: x['start'])
    minor_times.sort(key=lambda x: x['start'])

    return major_times, minor_times
