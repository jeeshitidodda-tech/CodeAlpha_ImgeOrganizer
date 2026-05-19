import os
import shutil

# Create Images folder if it does not exist
if not os.path.exists("Images"):
    os.makedirs("Images")

# Get all files from current folder
files = os.listdir()

# Check every file
for file in files:

    # Check if file is a JPG image
    if file.endswith(".jpg"):

        # Move image to Images folder
        shutil.move(file, "Images/" + file)

        print(file + " moved successfully")

print("All images organized!")