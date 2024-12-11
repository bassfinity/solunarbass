def generate_recommendations(major_times, minor_times):
    recommendations = []

    for period in major_times:
        recommendations.append({
            'type': 'Major',
            'start': period['start'],
            'end': period['end']
        })

    for period in minor_times:
        recommendations.append({
            'type': 'Minor',
            'start': period['start'],
            'end': period['end']
        })

    # Sort recommendations by start time
    recommendations.sort(key=lambda x: x['start'])

    return recommendations
