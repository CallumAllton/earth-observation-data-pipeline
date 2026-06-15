import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def fetch_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,cloud_cover,precipitation",
        "forecast_days": 3
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    weather_data = response.json()

    df = pd.DataFrame(weather_data["hourly"])

    df["latitude"] = latitude
    df["longitude"] = longitude
    df["fetched_at"] = datetime.utcnow().isoformat()

    return df


def main():

    darmstadt_lat = 49.8728
    darmstadt_lon = 8.6512
    
    df = fetch_weather(darmstadt_lat, darmstadt_lon)

    output_file = DATA_DIR / "darmstadt_weather.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved {len(df)} rows")
    print(df.head())


if __name__ == "__main__":
    main()