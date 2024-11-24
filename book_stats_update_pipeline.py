import subprocess

# Define the scripts to run
download_script = "storygraph-stats-download.py"
cleaning_script = "storygraph-cleaning.py"

try:
    # Run the download script
    print(f"Running {download_script}...")
    subprocess.run(["python", download_script], check=True)
    print(f"{download_script} completed successfully.\n")

    # Run the cleaning script
    print(f"Running {cleaning_script}...")
    subprocess.run(["python", cleaning_script], check=True)
    print(f"{cleaning_script} completed successfully.\n")

    print("Pipeline completed successfully!")

except subprocess.CalledProcessError as e:
    print(f"An error occurred while running the pipeline: {e}")
