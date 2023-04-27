import plotly.figure_factory as ff
import pandas as pd
import datetime

def create_gantt_chart(tasks):
    fig = ff.create_gantt(tasks, index_col='Assignee', show_colorbar=True, group_tasks=True)
    fig.show()

def read_tasks_from_csv(file_path):
    df = pd.read_csv(file_path)
    df['Start'] = pd.to_datetime(df['Start']).dt.strftime('%Y-%m-%d')
    df['Finish'] = pd.to_datetime(df['Finish']).dt.strftime('%Y-%m-%d')
    tasks = df.to_dict('records')
    return tasks

csv_file_path = 'thermal_tasks.csv'  # Replace this with the path to your CSV file
tasks = read_tasks_from_csv(csv_file_path)
create_gantt_chart(tasks)
