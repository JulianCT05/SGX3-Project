from flask import Flask, jsonify, request
import pandas as pd
import os
import io

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

if __name__ == "__main__":
    load_traffic_data()  # <- This runs BEFORE the server starts
    app.run(debug=True, host="0.0.0.0", port=8062)
