# 🚦 Austin Traffic Data API

A Flask-based REST API to explore and analyze Austin traffic incident data from a CSV dataset (`atxtraffic.csv`).

---

## 🔧 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**:
   ```bash
   pip install flask pandas geopy
   ```

3. **Place your dataset**:
   Ensure `atxtraffic.csv` is in the root directory.

4. **Run the app**:
   ```bash
   python app.py
   ```

   The API will be available at `http://0.0.0.0:8062`

---

## 📂 API Routes

### `/`  
**Returns:** First 10 rows of the dataset  
**Method:** `GET`  
**Example:**  
```
http://localhost:8062/
```

---

### `/head`  
**Returns:** First `n` rows  
**Query Param:** `count` (int)  
**Example:**  
```
/head?count=5
```

---

### `/shape`  
**Returns:** Row and column count  
**Method:** `GET`  
**Example:**  
```
/shape
```

---

### `/columns`  
**Returns:** Column names in the dataset  
**Method:** `GET`  
**Example:**  
```
/columns
```

---

### `/UniqueValues`  
**Returns:** Unique values from a specified column  
**Query Param:** `name` (column name)  
**Example:**  
```
/UniqueValues?name=Crash Type
```

---

### `/info`  
**Returns:** Summary info like `df.info()`  
**Method:** `GET`  
**Example:**  
```
/info
```

---

### `/describe`  
**Returns:** Summary statistics using `df.describe()`  
**Method:** `GET`  
**Example:**  
```
/describe
```

---

### `/filterByValueYear`  
**Filters rows by column value and year**  
**Query Params:**  
- `ColumnName`  
- `ColumnValue`  
- `Year`  

**Example:**  
```
/filterByValueYear?ColumnName=Crash Type&ColumnValue=Collision&Year=2022
```

---

### `/HoursBetween`  
**Filters by hour of day range**  
**Query Params:**  
- `hours1`: start hour (inclusive)  
- `hours2`: end hour (exclusive)  

**Example:**  
```
/HoursBetween?hours1=7&hours2=9
```

---

### `/1kiloSearch`  
**Returns rows within 1 km of given lat/lon**  
**Query Params:**  
- `lat`: Latitude  
- `long`: Longitude  

**Example:**  
```
/1kiloSearch?lat=30.2672&long=-97.7431
```

---

## 🧪 Sample curl Requests

```bash
curl "http://localhost:8062/head?count=3"
curl "http://localhost:8062/columns"
curl "http://localhost:8062/UniqueValues?name=Crash Type"
curl "http://localhost:8062/filterByValueYear?ColumnName=Crash Type&ColumnValue=Collision&Year=2022"
curl "http://localhost:8062/1kiloSearch?lat=30.2672&long=-97.7431"
```

---

## 📄 License

This project is licensed under the MIT License.
