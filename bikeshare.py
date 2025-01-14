import pandas as pd
import os
import matplotlib.pyplot as plt

def load_data():
    """
    Load bikeshare data for Chicago, New York City, and Washington.

    Returns:
        dict: A dictionary with city names as keys and DataFrames as values.
    """
    files = {
        "chicago": 'chicago.csv',
        "new york city": 'new_york_city.csv',
        "washington": 'washington.csv'
    }
    data = {}
    for city, path in files.items():
        try:
            if os.path.exists(path):
                data[city] = pd.read_csv(path)
            else:
                print(f"Warning: File {path} not found. Skipping {city}.")
        except Exception as e:
            print(f"Error loading file {path}: {e}")
    return data

def filter_data(data, city):
    """
    Filter data based on month and day of the week.

    Args:
        data (dict): Dictionary containing city data.
        city (str): City name.

    Returns:
        DataFrame: Filtered data.
    """
    city_data = data[city]
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'], errors='coerce')
    city_data = city_data.dropna(subset=['Start Time'])
    city_data['Month'] = city_data['Start Time'].dt.month
    city_data['Day of Week'] = city_data['Start Time'].dt.day_name()
    city_data['Hour'] = city_data['Start Time'].dt.hour

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    try:
        filter_month = input("\nDo you want to filter by month? Enter month name or 'all': ").strip().lower()
        if filter_month != 'all' and filter_month in months:
            month_index = months.index(filter_month) + 1
            city_data = city_data[city_data['Month'] == month_index]
        elif filter_month != 'all':
            print("Invalid month. Showing all data.")
    except Exception as e:
        print(f"Error processing month filter: {e}")

    try:
        filter_day = input("\nDo you want to filter by day? Enter day name or 'all': ").strip().lower()
        if filter_day != 'all' and filter_day in days:
            city_data = city_data[city_data['Day of Week'].str.lower() == filter_day]
        elif filter_day != 'all':
            print("Invalid day. Showing all data.")
    except Exception as e:
        print(f"Error processing day filter: {e}")

    return city_data

def display_statistics(data):
    """
    Display detailed statistics.

    Args:
        data (DataFrame): Filtered data.
    """
    print("\nTrip Duration Statistics")
    print(f"Total Duration: {data['Trip Duration'].sum():,.2f} seconds")
    print(f"Average Duration: {data['Trip Duration'].mean():.2f} seconds")

    print("\nUser Type Distribution")
    print(data['User Type'].value_counts())

    if 'Gender' in data.columns:
        print("\nGender Distribution")
        print(data['Gender'].value_counts())

    if 'Birth Year' in data.columns:
        print("\nBirth Year Information")
        print(f"Earliest Year: {data['Birth Year'].min():.0f}")
        print(f"Most Recent Year: {data['Birth Year'].max():.0f}")
        print(f"Most Common Year: {data['Birth Year'].mode()[0]:.0f}")

    print("\nPeak Hours")
    print(data['Hour'].value_counts().head(5))

def plot_statistics(data, city):
    """
    Generate visualizations for better insights.

    Args:
        data (DataFrame): Filtered data.
        city (str): City name.
    """
    plt.figure(figsize=(10, 6))

    # Plot peak start hours
    plt.bar(data['Hour'].value_counts().index, data['Hour'].value_counts().values)
    plt.title(f"Peak Hours for {city.title()}")
    plt.xlabel("Hour")
    plt.ylabel("Number of Rides")
    plt.xticks(range(0, 24))
    plt.grid()
    plt.show()

def main():
    """
    Main function to run the bikeshare analysis tool.
    """
    data = load_data()
    if not data:
        print("No valid data files were found. Exiting the program.")
        return

    while True:
        city = input("\nEnter city name (Chicago, New York City, Washington): ").strip().lower()
        if city in data:
            city_data = filter_data(data, city)
            display_statistics(city_data)
            plot_statistics(city_data, city)
        else:
            print("\nInvalid city. Please choose from Chicago, New York City, or Washington.")

        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").strip().lower()
        if restart != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
