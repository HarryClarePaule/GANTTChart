# GANTTChart

These programs help with project/task management. There are two programs created in this repo:
1. ganttChart.py - creates a GANTT chart from .csv file entries (Task,Start,Finish,Engineer). please see "_example_csv.csv_" for data entry requirements
2. greedyAlgoGantt.py - this program is a little more clever, it will create a Gantt chart as before but it will also automatically assign unassigned tasks to the next available engineer. If there are no available engineers for the given task time period then it will create a "New Hire" entry and assign the task to them indicating you will need to recruit or outsource this work. Please see "_example_greedyAlgo.csv_" for data entry requirements. This program will also output the csv file in start date order, see "_sorted_example_greedyAlgo.csv_" for example.

Both programmes use pandas to create a dataframe from the csv file.
