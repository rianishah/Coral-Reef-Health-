
csv_file_path = '/mnt/data/coral_reef_data.csv'
with open(csv_file_path, 'w') as file:
    file.write(sample_csv_content)

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process_data(file_path):
    """
    Load coral reef data from a CSV file and process it for analysis.
    """
    data = pd.read_csv(file_path)

    return data

def visualize_coral_health_over_time(data):
    """
    Visualize changes in coral health over time using the processed data.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Coral Cover (%)', data=data, marker='o')
    plt.title('Coral Cover Over Time')
    plt.xlabel('Year')
    plt.ylabel('Coral Cover (%)')
    plt.show()

def main():
    file_path = csv_file_path
    data = load_and_process_data(file_path)
    visualize_coral_health_over_time(data)

