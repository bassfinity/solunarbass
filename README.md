# Solunar Bass Forecasting Tool

Welcome to **Solunar Bass**, an open-source project by **Bassfinity** that helps bass fishermen maximize their fishing success using solunar theory, data acquisition, and personalized recommendations. This repository powers a web app that predicts optimal bass fishing times based on solunar data, weather conditions, and location.

The project consists of several key components working together, from data acquisition to recommendations. The hosted version of this tool can be found here: [Solunar Bass App](https://solunarbass-klbya3rzy8fbhed4wj8nhc.streamlit.app).

## Project Overview

This repository contains all the necessary components to run the Solunar Bass web application:

1. **app.py**: The main application file that integrates all functionalities and renders the Streamlit web interface.
2. **data_acquisition.py**: Handles fetching and processing external data (e.g., weather, solunar events) required for accurate predictions.
3. **data_processing.py**: Responsible for cleaning, transforming, and structuring data for analysis and display.
4. **recommendation_engine.py**: Contains the logic to generate personalized fishing recommendations based on solunar data and user input.
5. **solunar_calculations.py**: Provides utility functions for calculating solunar tables, lunar phases, and their impact on fishing activity.

The application is hosted via [Streamlit](https://streamlit.io/), allowing it to be easily deployed and accessed via the web.

## Features

- **Real-time Solunar Calculations**: Uses solunar theory to predict peak times for bass fishing.
- **Location-based Forecasts**: Enter your location and get localized fishing forecasts.
- **User-friendly Interface**: Built using Streamlit for an intuitive and visually appealing user experience.
- **Interactive Map**: Powered by Folium, showing solunar activity and fishing hotspots near your location.

## Getting Started

### Prerequisites

To run this application locally, you'll need:

- Python 3.7 or higher
- The dependencies listed in the `requirements.txt` file (see below)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/bassfinity/solunarbass.git
   cd solunarbass
   ```

2. **Install the required dependencies**:

   You can install the necessary Python libraries with the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install:

   - `streamlit` (for the web interface)
   - `pandas` and `numpy` (for data handling)
   - `requests` (for fetching external data)
   - `pytz` (for timezone-aware operations)
   - `streamlit-js-eval` and `folium` (for the interactive map)
   - `streamlit-folium` (for rendering maps within Streamlit)

   **Requirements list**:
   ```
   streamlit
   pandas
   numpy
   requests
   pytz
   streamlit-js-eval
   folium
   streamlit-folium
   ```

3. **Run the Application**:

   Once the dependencies are installed, you can start the application by running:

   ```bash
   streamlit run app.py
   ```

   This will launch the web app locally, and you can access it in your browser at `http://localhost:8501`.

## Code Overview

### app.py

This is the entry point for the web app. It ties together data acquisition, processing, solunar calculations, and the recommendation engine. The user interface is built with **Streamlit**, providing sliders, maps, and charts to interact with the data.

### data_acquisition.py

This module handles the fetching of data from external APIs (e.g., weather data). It ensures that relevant data points, such as moon phases and weather conditions, are retrieved and prepared for processing.

- **Key Functions**:
  - `fetch_weather_data()`: Fetches weather information for the specified location.
  - `get_solunar_times()`: Retrieves solunar tables and lunar events for the target date and location.

### data_processing.py

This script is responsible for processing the raw data obtained from the data acquisition step. It ensures data is clean, correctly formatted, and ready for analysis.

- **Key Functions**:
  - `clean_data()`: Cleans and formats raw data.
  - `process_for_recommendations()`: Prepares data for use in the recommendation engine.

### recommendation_engine.py

The heart of the application, this module uses solunar theory and weather data to recommend the best times for bass fishing. It applies algorithms that calculate optimal fishing periods based on the moon phases, weather, and other factors.

- **Key Functions**:
  - `generate_recommendations()`: Creates personalized fishing recommendations based on user location and preferences.

### solunar_calculations.py

This utility module contains the logic to compute solunar events, such as lunar phases, major and minor feeding times, and their correlation with fishing activity.

- **Key Functions**:
  - `calculate_solunar_table()`: Generates solunar tables for specific dates and locations.
  - `get_moon_phase()`: Determines the moon phase, which is crucial for solunar predictions.

## Running the App

After setting everything up, you can run the app either locally or host it using a platform like Streamlit Cloud. For now, we’ve already hosted the application for public use:

**Try it out here**: [Solunar Bass App](https://solunarbass-klbya3rzy8fbhed4wj8nhc.streamlit.app)

## Contributing

Contributions are welcome! If you want to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and ensure everything is tested.
4. Open a pull request, and we will review it.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/bassfinity/solunarbass/blob/main/LICENSE) file for details.

## Feedback & Support

For any questions or feedback, feel free to reach out to the **Bassfinity** team. You can also open an issue on the [GitHub repository](https://github.com/bassfinity/solunarbass/issues) or reach them via email at [info@bassfinity.com](mailto:info@bassfinity.com).

## Credits

Special thanks to [Visual Crossing](https://www.visualcrossing.com/weather-api) for providing the weather data used in this application. Their comprehensive and reliable weather API was essential in building the forecasting functionality for this project.

---

Happy Fishing! 🐟
