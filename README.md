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
```
Enter city name (Chicago, New York City, Washington): Chicago
Do you want to filter by month? Enter month name or 'all': March
Do you want to filter by day? Enter day name or 'all': all

Trip Duration Statistics
Total Duration: 20,972,420.00 seconds
Average Duration: 707.60 seconds

User Type Distribution
Subscriber    19345
Customer       4294

Peak Hours
8: 2500
17: 2400
18: 2300
12: 2200
16: 2100

A bar chart will display showing the peak hours.
```

## Notes
- Ensure the CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) are in the same directory as the script.
- If any file is missing, the program will skip that city and notify the user.

## References
- [Python Official Documentation](https://docs.python.org/3/)
- [pandas Documentation](https://pandas.pydata.org/)
- [matplotlib Documentation](https://matplotlib.org/)
