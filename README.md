Earth Observation Data Pipeline

A Python-based project that retrieves meteorological data from public APIs, processes the data, and stores it for analysis.

Overview

This project was created to develop practical experience with software development, data processing, and infrastructure concepts. The application retrieves weather forecast data from the Open-Meteo API and converts the returned JSON data into a structured format using pandas.

Features
Retrieves weather forecast data from an external API
Processes JSON responses into structured datasets
Stores weather data as CSV files
Uses Python virtual environments and dependency management
Built using a modular Python structure
Technologies
Python
Pandas
Requests
Git
GitHub
Project Structure
earth-observation-data-pipeline/
├── data/
├── src/
│   └── fetch_weather.py
├── requirements.txt
├── README.md
└── .gitignore
Installation
pip install -r requirements.txt
Running the Project
python src/fetch_weather.py
Future Improvements
Store data in PostgreSQL
Add Docker support
Implement automated scheduling
Add data visualisation dashboards
Deploy to cloud infrastructure
Author

Callum Allton