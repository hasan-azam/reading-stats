from flask import Flask, jsonify, send_file
import subprocess
import os
from datetime import datetime



#initialize the Flask Server
app = Flask(__name__)

# Define the paths I'll Need
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOKS_DIR = os.path.join(BASE_DIR, "data", "cleaned-data", "books")
COMICS_DIR = os.path.join(BASE_DIR, "data", "cleaned-data", "comics")

#Make sure these paths exist
os.makedirs(BOOKS_DIR, exist_ok=True)
os.makedirs(COMICS_DIR, exist_ok=True)

@app.route('/update-reading-log', methods=['POST'])
def update_reading_log():
    """
    Trigger the 'reading-log-update.py' script to download and clean reading log data.

    """
    try:
        subprocess.run(["python", "reading-log-update.py"], check=True)

        return jsonify({"message": "Reading log update process completed successfully!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)