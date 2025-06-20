from flask import Flask, jsonify, request
import pandas as pd
import os
import io
import datetime
from geopy.distance import distance

# Define your global DataFrame
traffic_df = None

app = Flask(__name__)

def load_traffic_data():
    global traffic_df
    print("Loading Austin Traffic Data...")
    traffic_df = pd.read_csv("atxtraffic.csv")
    print(f"Loaded {len(traffic_df)} rows into memory.")


@app.route("/head")
def top():
    global traffic_df
    num = int(request.args.get("count"))
    sample = traffic_df.head(num).to_dict(orient='records')
    return jsonify(sample)

@app.route("/shape")
def shape():
    global traffic_df
    rows, cols = traffic_df.shape
    return jsonify({"rows": rows, "columns": cols})

@app.route("/columns")
def columns():
    global traffic_df
    column_names = traffic_df.columns.tolist()
    return jsonify({"columns": column_names})

@app.route("/UniqueValues")
def uniqueValues():
    columnName = request.args.get("name")
    unique_vals = traffic_df[columnName].dropna().unique().tolist()
    response = {
        "Column": columnName,
        "UniqueValues": unique_vals
    }
    return jsonify(response)

@app.route("/info")
def info():
    global traffic_df
    buffer = io.StringIO()
    traffic_df.info(buf=buffer)
    info_str = buffer.getvalue()
    buffer.close()
    return "<pre>" + info_str + "</pre>"

@app.route("/describe")
def describe():
    global traffic_df
    described_data = traffic_df.describe(include='all').fillna('').to_dict()
    return jsonify(described_data)


@app.route("/")
def index():
    global traffic_df
    sample = traffic_df.head(10).to_dict(orient="records")
    return jsonify(sample)



@app.route('/filterByValueYear')
def filter():
    global traffic_df

    #This gets the parameters
    column_name = request.args.get("ColumnName")
    column_value = request.args.get("ColumnValue")
    year = request.args.get("Year")


    try:
        year = int(year)
    except ValueError:
        return jsonify({"error": "Year must be an integer."}), 400

    # Ensure date column exists and is datetime
    if 'Published Date' not in traffic_df.columns:
        return jsonify({"error": "No 'Published Date' column in dataset."}), 400

    # Convert date column to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(traffic_df['Published Date']):
        traffic_df['Published Date'] = pd.to_datetime(traffic_df['Published Date'], errors='coerce')

    # Filter the dataframe
    filtered = traffic_df[
        (traffic_df[column_name] == column_value) &
        (traffic_df['Published Date'].dt.year == year)
    ]

    # Convert to JSON
    result = filtered.to_dict(orient='records')
    return jsonify({
        "match_count": len(result),
        "matches": result
    })


@app.route('/HoursBetween') 
def HoursBetween():
    hour1 = request.args.get('hours1')
    hour2 = request.args.get('hours2')

    hour1 = int(hour1)
    hour2 = int(hour2)

    traffic_df['Published Date'] = pd.to_datetime(traffic_df['Published Date'])
    traffic_df['Hour'] = traffic_df['Published Date'].dt.hour
    filtered = traffic_df[(traffic_df['Hour'] >= hour1) & (traffic_df['Hour'] < hour2)]
    return jsonify({
        "match_count": len(filtered),
        "matches": filtered.drop(columns=['Hour']).to_dict(orient='records')
    })

@app.route('/1kiloSearch')
def kiloSearch():
    global traffic_df
    lat = request.args.get("lat", type=float)
    lon = request.args.get("long", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Latitude and Longitude must be provided."}), 400

    # Clean the data to only include rows with valid lat/lon
    df = traffic_df.copy()
    df = df[pd.to_numeric(df["Latitude"], errors="coerce").notnull()]
    df = df[pd.to_numeric(df["Longitude"], errors="coerce").notnull()]
    df = df[(df["Latitude"] >= -90) & (df["Latitude"] <= 90)]
    df = df[(df["Longitude"] >= -180) & (df["Longitude"] <= 180)]

    from geopy.distance import distance
    df["distance_km"] = df.apply(
        lambda row: distance((lat, lon), (row["Latitude"], row["Longitude"])).km,
        axis=1
    )
    nearby = df[df["distance_km"] <= 1].drop(columns=["distance_km"])

    return jsonify({
        "match_count": len(nearby),
        "matches": nearby.to_dict(orient="records")
    })
if __name__ == "__main__":
    load_traffic_data()  # <- This runs BEFORE the server starts
    app.run(debug=True, host="0.0.0.0", port=8062)
