import pandas as pd
import numpy as np
import math


def makeSchedule(assignmentList, priorityList, workloadList, isSorted, happinessIndex):
    """Make a DataFrame and Sorts Based on the User Input"""

    # Make a default DataFrame
    schedule = pd.DataFrame()

    # Converts the provided List Data into Series
    namesArray = np.array(assignmentList)
    priorityArray = np.array(priorityList)
    workloadArray = np.array(priorityList)
    assignmentNamesSeries = pd.Series(namesArray, index=np.arange(0, len(assignmentList)))
    assignmentPrioritySeries = pd.Series(priorityArray, index=np.arange(0, len(priorityList)))
    assignmentWorkloadSeries = pd.Series(workloadArray, index=np.arange(0, len(workloadList)))

    # Boring DataFrame Building and Assignment
    schedule = schedule.assign(Assignments=assignmentNamesSeries)
    schedule = schedule.assign(Workload_Per_Week=assignmentWorkloadSeries).assign(Priority=assignmentPrioritySeries)

    # Series Math to find daily load
    daily = schedule.get('Workload_Per_Week') / 7
    daily = np.round(daily * 60, 0)
    schedule = schedule.assign(Workload_Per_Day_In_Min=daily)

    # Return the DataFrame Sorted
    if (isSorted == 'Priority'):
        return schedule.sort_values(by='Priority', ascending=False).set_index('Assignments')

    elif (isSorted == 'Workload'):
        return schedule.sort_values(by='Workload_Per_Day_In_Min', ascending=False).set_index('Assignments')

    else:
        return schedule.set_index('Assignments')

#Proxy data to test the functions
assignmentList = ['CSE 12 Homework','CSE 15L Lab','MMW 12 Essay','DSC 40A PA','MGT 12 Homework', "Derek Sux"]
priorityList = [5, 4, 3, 2, 1, 7]
workloadList = [2, 3, 2, 3, 2, 0]
isSorted = 'Priority'
happinessIndex = 0

#Sample Tables
sampleTable = makeSchedule(assignmentList, priorityList, workloadList, isSorted, happinessIndex)
sampleTable
