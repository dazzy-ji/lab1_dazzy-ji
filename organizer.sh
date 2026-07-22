#!/bin/bash

# Create archive directory if it doesn't exist
mkdir -p archive 


TIMESTAMP=$(date +%Y%m%d_%H%M%S) # Generate a timestamp for the archived file
ORIGINAL="grades.csv" # Define the original file name
ARCHIVED="grades_${TIMESTAMP}.csv" # Define the archived file name with timestamp

# Check if the original file exists
if [ ! -f "$ORIGINAL" ]; then
    echo "Error: $ORIGINAL does not exist. Nothing to archive."
    exit 1
fi

# Move the original file to the archive directory with a timestamped name
mv "$ORIGINAL" "archive/$ARCHIVED"
# Create a new empty original file
touch "$ORIGINAL"

# Log the action with a timestamp
echo "[$TIMESTAMP] Archived $ORIGINAL to archive/$ARCHIVED and created a new empty $ORIGINAL." >> organizer.log
echo "Done: $ORIGINAL has been archived and a new empty file has been created."