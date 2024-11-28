import subprocess
# Define the scripts to run
book_update = "book_stats_update_pipeline.py"
comic_update = "comic_stats_update_pipeline.py"

try:
    #Run the book stats update script
    subprocess.run(["python", book_update], check=True)
    print(f"{book_update} completed successfully. \n")

    #Run the comic stats update script
    subprocess.run(["python", comic_update], check=True)
    print(f"{comic_update} completed successfully. \n")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running the pipeline: {e}")