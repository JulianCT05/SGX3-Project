### SGX3 Coding repo
## Traffic Data API
<p> A Flask-based REST API for querying and filtering traffic incident data from CSV files.
Description
This API provides endpoints to search and filter traffic incident data based on various criteria including location, time, severity, and geographic proximity.
Installation</p>

## Clone the repository
# Install required dependencies:
<p>bashpip install flask pandas geopy</p>

<p>Ensure your CSV traffic data files are in the project directory
Run the application:</p>
'''
python app.py
'''

<p>The server will start at http://0.0.0.0:8062</p>

## API Endpoints
# GET /search
<p> Search for traffic incidents by location.
Parameters:
location (string): Location keyword to search for</p>
  
**Example:**
> GET /search?location=downtown


# GET /HoursBetween
Get incidents that occurred between specific hours.
Parameters:

hours1 (integer): Start hour (0-23)
hours2 (integer): End hour (0-23)

Example:
GET /HoursBetween?hours1=8&hours2=18
GET /1kiloSearch
Find incidents within 1km of specified coordinates.
Parameters:

lat (float): Latitude coordinate
long (float): Longitude coordinate

Example:
GET /1kiloSearch?lat=40.7128&long=-74.0060
Response Format
All endpoints return JSON responses with:
json{
  "match_count": number,
  "matches": [array of matching records]
}
Data Requirements
The API expects CSV files containing traffic data with columns including:

Location
Severity
Published Date
Latitude
Longitude

Usage
All endpoints return JSON with the following structure:
json{
  "match_count": number,
  "matches": [array of matching records]
}
Contributing

Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request

License
This project is licensed under the MIT License.
