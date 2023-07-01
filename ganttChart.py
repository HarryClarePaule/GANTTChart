import plotly.figure_factory as ff
import plotly.io as pio
import pandas as pd
import datetime


def create_gantt_chart(tasks, output_file):
    fig = ff.create_gantt(tasks, index_col='Engineer', show_colorbar=True, group_tasks=True)
    pio.write_html(fig, file=output_file)

def read_tasks_from_csv(file_path):
    df = pd.read_csv(file_path)
    df['Start'] = pd.to_datetime(df['Start']).dt.strftime('%Y-%m-%d')
    df['Finish'] = pd.to_datetime(df['Finish']).dt.strftime('%Y-%m-%d')
    tasks = df.to_dict('records')
    return tasks

today = datetime.date.today().strftime('%Y-%m-%d')
csv_file_path = 'example_csv.csv'  # Replace this with the path to CSV file
output_file = f'gantt_chart_{today}.html'  # The name of the output HTML file
tasks = read_tasks_from_csv(csv_file_path)
create_gantt_chart(tasks, output_file)
#