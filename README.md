# 🚦 Austin Traffic Data API

A Flask-based REST API to analyze and search Austin traffic incident data from a CSV dataset.

---

## 🔧 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask pandas geopy
   ```

3. **Add your dataset**:  
   Place the `atxtraffic.csv` file (containing Austin traffic incidents) in the project directory.

4. **Run the server**:
   ```bash
   python app.py
   ```

   The API will be accessible at `http://0.0.0.0:8062`.

---

## 📂 API Routes

### `/HoursBetween`

Returns all traffic incidents that occurred between two hours.

- **Method:** `GET`
- **Query Parameters:**
  - `hours1`: (int) Starting hour (inclusive)
  - `hours2`: (int) Ending hour (exclusive)

- **Example Request:**
  ```
  /HoursBetween?hours1=7&hours2=9
  ```

- **Example Response:**
  ```json
  {
    "match_count": 153,
    "matches": [
      {
        "Published Date": "2022-05-10 07:34:00",
        "Latitude": 30.2672,
        "Longitude": -97.7431,
        ...
      },
      ...
    ]
  }
  ```

---

### `/1kiloSearch`

Finds all incidents within 1 kilometer of a given latitude and longitude.

- **Method:** `GET`
- **Query Parameters:**
  - `lat`: (float) Latitude
  - `long`: (float) Longitude

- **Example Request:**
  ```
  /1kiloSearch?lat=30.2672&long=-97.7431
  ```

- **Example Response:**
  ```json
  {
    "match_count": 22,
    "matches": [
      {
        "Published Date": "2022-06-01 15:20:00",
        "Latitude": 30.2675,
        "Longitude": -97.7420,
        ...
      },
      ...
    ]
  }
  ```

---

## 🧪 Test with curl

```bash
curl "http://localhost:8062/HoursBetween?hours1=15&hours2=17"
curl "http://localhost:8062/1kiloSearch?lat=30.2672&long=-97.7431"
```

---

## 📌 Notes

- This API assumes the dataset contains valid `Latitude`, `Longitude`, and `Published Date` columns.
- The `Published Date` is parsed into hour values to support filtering.
- All data is loaded into memory once at startup for fast access.

---

## 📄 License

This project is licensed under the MIT License.
