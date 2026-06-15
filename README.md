# Earth Observation Data Pipeline

A Python-based data engineering project that retrieves meteorological data from public APIs, processes the data, and stores it for analysis.

## Overview

This project was created to develop practical experience with software engineering, data processing, automation, and infrastructure technologies. The application retrieves weather forecast data from the Open-Meteo API, transforms the returned JSON data into structured datasets using pandas, and exports the results for further analysis.

The project is version controlled using Git and GitHub and has been containerised using Docker to ensure consistent execution across environments.

## Features

* Retrieves weather forecast data from the Open-Meteo API
* Processes JSON responses into structured datasets using pandas
* Stores weather data as CSV files
* Adds metadata including location and retrieval timestamps
* Uses Python virtual environments and dependency management
* Containerised using Docker
* Version controlled using Git and GitHub

## Technologies

* Python
* Pandas
* Requests
* Docker
* Git
* GitHub

## Project Structure

```text
earth-observation-data-pipeline/
├── data/
├── src/
│   └── fetch_weather.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Run locally:

```bash
python src/fetch_weather.py
```

## Running with Docker

Build the Docker image:

```bash
docker build -t earth-observation-pipeline .
```

Run the container:

```bash
docker run --rm earth-observation-pipeline
```

## Future Improvements

* Store processed data in PostgreSQL
* Implement automated scheduling for recurring data collection
* Add data visualisation dashboards
* Deploy to cloud infrastructure
* Integrate additional Earth observation and satellite datasets

## Author

Callum Allton
