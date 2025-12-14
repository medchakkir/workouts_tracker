# Workout Tracker

A Python application that helps you track your workouts and automatically logs them to a Google Sheet. This project uses the Nutritionix API to process natural language exercise inputs and calculate calories burned, then logs the workout data to your Google Sheet via API.

## Features

- Natural language exercise input processing via Nutritionix API
- Automatic calorie calculation based on exercise type and duration
- Real-time workout logging to Google Sheets
- Timestamp tracking for each workout entry
- Support for multiple exercises in a single input
- Environment variable configuration for secure credential management

## Requirements

- Python 3.x
- Nutritionix API account (App ID and API Key)
- Google Sheets API endpoint with authentication token
- Required Python packages (see `requirements.txt`):
  - `python-dotenv` - For loading environment variables
  - `requests` - For making API calls to Nutritionix and Google Sheets

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/workouts_tracker.git
cd workouts_tracker
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:

```env
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
API_TOKEN=your_google_sheets_api_token
SHEET_ENDPOINT=https://api.sheety.co/your_project/your_sheet/workouts
```

**Important:**

- Replace all placeholder values with your actual credentials
- Never commit the `.env` file to version control
- Get your Nutritionix credentials from [Nutritionix API](https://www.nutritionix.com/business/api)
- Set up your Google Sheets API endpoint (e.g., using Sheety or Google Sheets API)

## Usage

To run the script:

```bash
python main.py
```

### How It Works

1. The script loads environment variables from `.env` file
2. Prompts you to enter your exercises in natural language
3. Sends your exercise description to the Nutritionix API
4. Receives processed exercise data including:
   - Exercise name
   - Duration (in minutes)
   - Calories burned
5. Formats the data with current date and time
6. Logs each exercise to your Google Sheet via API
7. Displays the workout data and API response status

### Input Format

Enter your exercises in natural language. The Nutritionix API will parse your input and extract exercise information. For example:

- "I ran 5km and did 30 minutes of yoga"
- "I swam for 45 minutes and did 20 minutes of weight lifting"
- "I cycled 10 miles and ran for 20 minutes"

### Output Format

Each workout entry logged to your Google Sheet includes:

- **Date**: DD/MM/YYYY format
- **Time**: HH:MM:SS format
- **Exercise**: Exercise name (title case)
- **Duration**: Duration in minutes
- **Calories**: Calories burned

The script also prints the workout data and HTTP status code for each API request.

## API Integration

This project integrates with:

- **Nutritionix API**: Processes natural language exercise inputs and calculates calories burned
  - Endpoint: `https://trackapi.nutritionix.com/v2/natural/exercise`
  - Requires: App ID and API Key in request headers
  
- **Google Sheets API**: Logs workout data to your spreadsheet
  - Uses your configured endpoint (e.g., Sheety API or Google Sheets API)
  - Requires: Authorization token in request headers

## Error Handling

**Note:** The current implementation does not include comprehensive error handling. Consider adding error handling for:

- Missing environment variables
- API request failures (network errors, timeouts, HTTP errors)
- JSON parsing errors
- Invalid user input
- Google Sheets API authentication failures
- Unexpected exceptions

## Security Notes

- **Never commit your `.env` file** to version control - it contains sensitive credentials
- Keep your API keys secure and rotate them periodically if compromised
- Use environment variables instead of hardcoding credentials
- Consider using a secrets management service for production deployments
- The `.env` file should be included in `.gitignore` to prevent accidental commits
- Be cautious when sharing your Google Sheets endpoint URL

## Setting Up Google Sheets Integration

To set up your Google Sheet for workout logging:

1. Create a Google Sheet with columns: Date, Time, Exercise, Duration, Calories
2. Set up API access using one of these methods:
   - **Sheety API**: Easy-to-use service that converts Google Sheets to REST API
   - **Google Sheets API**: Official Google API (requires more setup)
3. Configure your endpoint URL and authentication token
4. Test the connection before running the main script

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
