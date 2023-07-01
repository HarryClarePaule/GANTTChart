# GANTTChart

These programmes help with project/task management.There are two programmes created in this repo:
1. ganttChart.py - creates a GANTT chart from .csv file entires (Task,Start,Finish,Engineer). please see "_example_csv.csv_" for data entry requirements
2. greedyAlgoGantt.py - this programme is a little more clever, it will creaet a Gantt chart as before but it will also automatically assign unassigned tasks to the next available engineer. If there are no available engineers for the give task time period then it will creaet a "New Hire" entry and assign the task to them indicating you will need to recruit or outsource this work. Please see "_example_greedyAlgo.csv_" for data entry requirements. This programme will also output the csv file in start date order, see "_sorted_example_greedyAlgo.csv_" for example.

Both programmes use pandads to create a datframe from the csv file.
