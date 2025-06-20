import re
import numpy as np
import pandas as pd

class SensorDataProcessor:
    def __init__(self):
        pass

    def clean_data(self, data: str) -> str:
        """
        Cleans the input string by removing special characters, 
        converting to lowercase, and replacing digits with "num".
        """
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', data)
        cleaned_string = cleaned_string.lower()
        cleaned_string = re.sub(r'\d+', 'num', cleaned_string)
        return cleaned_string

    def extract_readings(self, data: str) -> dict:
        """
        Extracts temperature, humidity, and pressure readings from the cleaned string.
        """
        readings = {}

        temperature_match = re.search(r'temperature: (\d+)', data)
        if temperature_match:
            readings['temperature'] = int(temperature_match.group(1))
        else:
            readings['temperature'] = None

        humidity_match = re.search(r'humidity: (\d+)', data)
        if humidity_match:
            readings['humidity'] = int(humidity_match.group(1))
        else:
            readings['humidity'] = None

        pressure_match = re.search(r'pressure: (\d+)', data)
        if pressure_match:
            pressure_value = pressure_match.group(1)
            if pressure_value != 'num':
                readings['pressure'] = int(pressure_value)
            else:
                readings['pressure'] = pressure_value
        else:
            readings['pressure'] = None

        return readings

    def process_numeric_data(self, data: list) -> np.ndarray:
        """
        Converts a list to a NumPy array and replaces invalid entries with the mean.
        """
        # 1. Convert to NumPy array, handling "Invalid" strings
        numeric_values = []
        valid_sum = 0
        valid_count = 0
        for item in data:
            if isinstance(item, (int, float)):
                numeric_values.append(item)
                valid_sum += item
                valid_count += 1
            elif isinstance(item, str) and item.lower() != "invalid":
                try:
                    num_val = float(item)
                    numeric_values.append(num_val)
                    valid_sum += num_val
                    valid_count += 1
                except ValueError:
                    pass  # Ignore if it can't be converted
            else:
                numeric_values.append(np.nan)  # Use NaN for "Invalid" or unconvertible

        np_array = np.array(numeric_values, dtype=np.float64)

        # 2. Calculate the average of valid numbers
        valid_numbers = np_array[~np.isnan(np_array)]  # Filter out NaNs
        if valid_numbers.size > 0:
            average = np.mean(valid_numbers)
        else:
            average = 0  # Or np.nan, depending on desired behavior if no valid numbers

        # 3. Replace NaNs (invalid entries) with the average
        np_array = np.nan_to_num(np_array, nan=average)

        return np_array

    def analyze_data(self, readings: dict) -> pd.DataFrame:
        """
        Converts a dictionary of readings to a Pandas DataFrame and calculates the mean.
        """
        # 1. Create the DataFrame
        df = pd.DataFrame(readings)

        # 2. Calculate the mean of each column
        mean_values = df.mean(numeric_only=True)  # Calculate means, skip non-numeric

        # 3. Append the mean as a new row
        mean_df = pd.DataFrame(mean_values, columns=['Mean']).T  # Create a DataFrame from the means
        df = pd.concat([df, mean_df], ignore_index=True)  # Append the mean row

        return df

# --- Example Usage ---
processor = SensorDataProcessor()

# Question 1
data1 = "Sensor_1 recorded: 85 readings on 2023-09-15, at 14:55:01!"
cleaned_data = processor.clean_data(data1)
print("Question 1 - Cleaned Data:", cleaned_data)

# Question 2
data2 = "temperature: 22 humidity: 55 pressure: num"
readings = processor.extract_readings(data2)
print("Question 2 - Extracted Readings:", readings)

# Question 3
data3 = [22.3, 23.1, None, "Invalid", 21.9]
processed_data = processor.process_numeric_data(data3)
print("Question 3 - Processed NumPy Array:", processed_data)

# Question 4
data4 = {
    'temperature': [22.1, 23.0, 21.9],
    'humidity': [55, 60, 57],
    'pressure': [1012, 1010, 1011]
}
analyzed_df = processor.analyze_data(data4)
print("Question 4 - Pandas DataFrame Analysis:\n", analyzed_df)