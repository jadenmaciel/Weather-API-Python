# Simple Weather API in Python

This Python script fetches and displays current weather information for a specified city using the OpenWeatherMap API. It's designed to be a straightforward and easy-to-use tool for getting quick weather updates.

## Problem Statement/Motivation
Many times, developers or individuals need a simple way to access current weather data programmatically. This script provides a basic framework to do just that, requiring minimal setup and allowing users to easily retrieve essential weather information for any location supported by OpenWeatherMap.

## Features Implemented
* Fetches current temperature in Celsius and Fahrenheit.
* Provides the "feels like" temperature.
* Displays the humidity percentage.
* Shows the current wind speed.
* Retrieves and displays the general weather description (e.g., "clear sky", "scattered clouds").
* Calculates and displays the sunrise and sunset times in the local time zone of the specified city.

## Technologies Used
* **Python:** The primary programming language.
* **Requests:** A Python library for making HTTP requests.
* **datetime:** A built-in Python module for working with dates and times.
* **pytz:** A Python library for working with time zones.

## Setup and Installation Instructions
1.  **Obtain an API Key:** Sign up for a free API key at [https://openweathermap.org/api](https://openweathermap.org/api).
2.  **Save the API Key:**
    * Create a new file named `api_key` in the same directory as your Python script.
    * Open the `api_key` file and paste your OpenWeatherMap API key into it.
    * Save and close the file.
3.  **Install Dependencies:** If you don't have the `requests` and `pytz` libraries installed, open your terminal or command prompt and run:
    ```bash
    pip install requests pytz
    ```
4.  **Save the Python Code:** Save the provided Python code as a `.py` file (e.g., `weather_api.py`).

## Usage/Examples
1.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved the files, and run the script using:
    ```bash
    python weather_api.py
    ```
2.  **Change the City:** To get weather information for a different city, open the `weather_api.py` file and modify the `CITY` variable on this line:
    ```python
    CITY = "Los Angeles" # Change "Los Angeles" to your desired city
    ```
    For example, to get the weather for London, change it to:
    ```python
    CITY = "London"
    ```
3.  **Run Again:** After changing the city, save the file and run the script again. It will now display the weather information for the new city.

## Live Demo Link
*(Not applicable for this type of script as it's a command-line tool and not a deployed web application.)*

## Challenges & Learnings
* **Handling Time Zones:** Initially, displaying sunrise and sunset times in the correct local time zone required understanding the time zone data provided by the OpenWeatherMap API and using the `pytz` library effectively. This highlighted the importance of time zone awareness in location-based applications.
* **API Key Security:** While this example reads the API key from a local file for simplicity, a more robust application would involve secure storage of API keys, such as using environment variables, to prevent accidental exposure.
