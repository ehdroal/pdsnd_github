# Bikeshare Analysis Project

## Overview
This project provides an interactive tool for analyzing bikeshare data from Chicago, New York City, and Washington. Users can filter the data by months, days of the week, and view peak usage hours with visualizations. The updated version includes enhanced analysis features and visual outputs.

## Features
1. **Data Loading**:
   - Load bikeshare data for Chicago, New York City, and Washington.
   - Automatically skip missing files and notify the user.

2. **Data Filtering**:
   - Filter the dataset by:
     - Specific month (e.g., January, February, etc.).
     - Specific day of the week (e.g., Monday, Tuesday, etc.).
   - Display peak usage hours (new feature).

3. **Statistical Analysis**:
   - Total trip duration.
   - Average trip duration.
   - User types distribution.
   - Gender distribution (if available).
   - Birth year statistics (if available):
     - Earliest, most recent, and most common birth years.

4. **Visualizations**:
   - Bar chart showing peak hours for trips.

## How to Use
1. Run the Python script.
2. When prompted, enter the city name (Chicago, New York City, Washington).
3. Select filters:
   - Enter a month name or "all" to skip month filtering.
   - Enter a day name or "all" to skip day filtering.
4. View analysis:
   - Key statistics (total trip duration, user demographics, etc.).
   - Visualizations (peak hours).
5. Follow the on-screen prompts for further actions.

## Requirements
- Python 3.x
- `pandas` library
- `matplotlib` library

## Example Run
