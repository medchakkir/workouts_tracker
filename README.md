# Workout Tracker

A Python application that helps you track your workouts and automatically logs them to a Google Sheet. The application uses the Nutritionix API to process natural language exercise inputs and calculate calories burned.

## Features

- Natural language exercise input processing
- Automatic calorie calculation
- Real-time workout logging
- Google Sheets integration
- Timestamp tracking for each workout
- Support for multiple exercises in a single input

## Requirements

- Python 3.x
- Required Python packages (see requirements.txt):
  - requests
  - pandas
  - numpy
  - python-dateutil
  - certifi
  - urllib3

## Environment Variables

The following environment variables need to be set:

- `ENV_APP_ID`: Your Nutritionix API App ID
- `ENV_API_KEY`: Your Nutritionix API Key
- `ENV_API_TOKEN`: Your Google Sheets API Token
- `ENV_SHEET_ENDPOINT`: Your Google Sheet API endpoint

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/workouts_tracker.git
cd workouts_tracker
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your API credentials and endpoints

## Usage

Run the application:

```bash
python main.py
```

### Input Format

Enter your exercises in natural language. For example:

- "I ran 5km and did 30 minutes of yoga"
- "I swam for 45 minutes and did 20 minutes of weight lifting"

The application will:

1. Process your input through the Nutritionix API
2. Calculate calories burned for each exercise
3. Log the workout details to your Google Sheet

### Output Format

Each workout entry includes:

- Date (DD/MM/YYYY)
- Time (HH:MM:SS)
- Exercise name
- Duration (minutes)
- Calories burned

## API Integration

This project integrates with:

- Nutritionix API for exercise processing and calorie calculation
- Google Sheets API for workout logging

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
