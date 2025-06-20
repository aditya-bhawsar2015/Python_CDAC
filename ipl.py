import re
import numpy as np
import pandas as pd

class IPLDataProcessor:
    def __init__(self):
        pass

    def clean_data(self, data: str) -> str:
        """
        Cleans the input string by removing special characters, 
        converting to lowercase, and replacing digit sequences with "NUM".

        Args:
            data (str): The input string to be cleaned.

        Returns:
            str: The cleaned string.
        """
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', data)  # Remove special characters
        cleaned_string = cleaned_string.lower()  # Convert to lowercase
        cleaned_string = re.sub(r'\d+', 'NUM', cleaned_string)  # Replace digits with "NUM"
        return cleaned_string

    def extract_player_stats(self, data: str) -> dict:
        """
        Extracts player statistics (runs, wickets, strike rate) from the cleaned string.

        Args:
            data (str): The cleaned input string.

        Returns:
            dict: A dictionary containing the extracted statistics.
                 Values are either the statistic (as a number) or None if not found.
        """

        stats = {}
        runs_match = re.search(r'runs (\d+)', data)  # Search for "runs" followed by digits
        if runs_match:
            stats['runs'] = int(runs_match.group(1))
        else:
            stats['runs'] = None

        wickets_match = re.search(r'wickets (\d+)', data)  # Search for "wickets" followed by digits
        if wickets_match:
            stats['wickets'] = int(wickets_match.group(1))
        else:
            stats['wickets'] = None

        strike_rate_match = re.search(r'strike rate (\d+\.?\d*)', data)  # Search for "strike rate" followed by number
        if strike_rate_match:
            stats['strike_rate'] = float(strike_rate_match.group(1))
        else:
            stats['strike_rate'] = None

        return stats

    def process_numeric_data(self, data: list) -> np.ndarray:
        """
        Converts a list to a NumPy array and replaces invalid entries with the average.

        Args:
            data (list): A list of numeric data (can contain invalid entries).

        Returns:
            np.ndarray: A NumPy array with invalid entries replaced by the average.
        """

        numeric_values = []
        valid_sum = 0
        valid_count = 0

        for item in data:
            if isinstance(item, (int, float)):
                numeric_values.append(item)
                valid_sum += item
                valid_count += 1
            else:
                try:
                    num_val = float(item)
                    numeric_values.append(num_val)
                    valid_sum += num_val
                    valid_count += 1
                except (ValueError, TypeError):
                    numeric_values.append(np.nan)

        np_array = np.array(numeric_values, dtype=np.float64)

        valid_numbers = np_array[~np.isnan(np_array)]
        average = np.mean(valid_numbers) if valid_numbers.size > 0 else 0

        np_array = np.nan_to_num(np_array, nan=average)
        return np_array

    def analyze_player_performance(self, stats: dict) -> pd.DataFrame:
        """
        Converts a dictionary of player stats to a Pandas DataFrame and calculates the mean.

        Args:
            stats (dict): A dictionary where keys are stat names and values are lists of stats.

        Returns:
            pd.DataFrame: A Pandas DataFrame with the stats and a row for the mean.
        """

        df = pd.DataFrame(stats)
        mean_values = df.mean(numeric_only=True)
        mean_df = pd.DataFrame(mean_values, columns=['Mean']).T
        df = pd.concat([df, mean_df], ignore_index=True)
        return df

# --- Example Usage ---
processor = IPLDataProcessor()

# Question 1
data1 = "Virat Kohli scored 97 runs off 58 balls in the match on 2024-09-15!"
cleaned_data = processor.clean_data(data1)
print("Q1 - Cleaned Data:", cleaned_data)

# Question 2
data2 = "Virat Kohli scored 97 runs with a strike rate of 158.67"
player_stats = processor.extract_player_stats(data2)
print("Q2 - Player Stats:", player_stats)

# Question 3
data3 = [150.5, 78.1, None, "error", 64.2]
processed_data = processor.process_numeric_data(data3)
print("Q3 - Processed Numeric Data:", processed_data)

# Question 4
data4 = {
    'runs': [50, 78, 64],
    'wickets': [2, 1, 3],
    'strike_rate': [140.5, 150.2, 135.6]
}
performance_df = processor.analyze_player_performance(data4)
print("Q4 - Player Performance Analysis:\n", performance_df)