import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import datetime
from collections import defaultdict

csv_file_path = 'example_greedyAlgo.csv'

# Read the CSV file, change to suitable csv
df = pd.read_csv(csv_file_path)

# Convert the 'Start' and 'End' columns to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Sort the tasks based on the task name
df = df.sort_values(by='Start')

# Initialize the availability of each engineer
availability = defaultdict(lambda: datetime.min)

new_hire_counter = 1
for i, task in df.iterrows():
    if pd.isna(task['Engineer']):  # Only assign unassigned tasks
        # Find the engineer who is available the earliest
        available_engineer = min(availability, key=availability.get) if availability else f'New Hire {new_hire_counter}'
        # If all engineers are busy or there are no engineers, hire a new engineer
        if not availability or availability[available_engineer] > task['Start']:
            available_engineer = f'New Hire {new_hire_counter}'
            new_hire_counter += 1
        df.at[i, 'Engineer'] = available_engineer
        # Update the availability of the engineer
        availability[available_engineer] = max(availability[available_engineer], task['Finish'])

# Save the dataframe back to the CSV file
df.to_csv(f'sorted_{csv_file_path}', index=False)

# Plot a Gantt chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Engineer", hover_data={'Task':True, 'Start':':%Y-%m-%d', 'Finish':':%Y-%m-%d'})
fig.update_yaxes(autorange="reversed")  # Reverse the y-axis

# Export the Gantt chart to a local HTML file
today = datetime.today().strftime('%Y-%m-%d')
pio.write_html(fig, f'gantt_chart_{today}_greedy.html')
