from flask import Flask, render_template, url_for, Blueprint
import pandas as pd
import numpy as np
import math





def makeSchedule(assignmentList, priorityList, workloadList, dueDatesList, isSorted, happinessIndex):
    """Make a DataFrame and Sorts Based on the User Input"""
    
    dates = []
    for date in dueDatesList:
        proxyTime = date.split('/')
        dueDate = dt.date(int(proxyTime[2]), int(proxyTime[0]), int(proxyTime[1]))
        dates.append(dueDate)

    daysAway = []

    today = dt.datetime.now().date()

    for d in dates:
        untilDue = d - today
        daysAway.append(untilDue.days)

    dates = np.array(daysAway)
    datesSeries = pd.Series(dates, index=np.arange(0, len(dates)))
    

    # Make a default DataFrame
    schedule = pd.DataFrame()
    
    #Variables and Ideas 
    today = dt.datetime.now()
    

    # Converts the provided List Data into Series
    namesArray = np.array(assignmentList)
    priorityArray = np.array(priorityList)
    workloadArray = np.array(workloadList)
    assignmentNamesSeries = pd.Series(namesArray, index=np.arange(0, len(assignmentList)))
    assignmentPrioritySeries = pd.Series(priorityArray, index=np.arange(0, len(priorityList)))
    assignmentWorkloadSeries = pd.Series(workloadArray, index=np.arange(0, len(workloadList)))

    # Boring DataFrame Building and Assignment
    schedule = schedule.assign(Assignments=assignmentNamesSeries)
    schedule = schedule.assign(Workload_For_Assignment=assignmentWorkloadSeries).assign(Priority=assignmentPrioritySeries).assign(Until_Due = daysAway)

    # Series Math to find daily load
    daily = schedule.get('Workload_For_Assignment') / schedule.get('Until_Due')
    
    daily = np.round(daily * 60, 0)
    schedule = schedule.assign(Workload_Per_Day_In_Min=daily)
    schedule = schedule.assign(Workload_Per_Day_In_Min=daily)
    schedule = schedule.replace([np.inf, -np.inf], np.nan).fillna(0)
    # Return the DataFrame Sorted
    if (isSorted == 'Priority'):
        return schedule.sort_values(by='Priority')

    elif (isSorted == 'Workload'):
        return schedule.sort_values(by='Workload_Per_Day_In_Min', ascending=False)
    
    elif (isSorted == 'Until_Due'):
        return schedule.sort_values(by='Until_Due')

    else:
        return schedule
    
def getWorkload(dataFrame):
    workloadInNum = dataFrame.get('Workload_Per_Day_In_Min').sum()
    return workloadInNum

def highPriorityWork(dataFrame):
    workloadInNum = dataFrame[dataFrame.get('Priority') >= 4].get('Workload_Per_Day_In_Min').sum()
    return workloadInNum

#Proxy data to test the functions
assignmentList = ['CSE 12 Homework','CSE 15L Lab','MMW 12 Essay','DSC 40A PA']
dueDates = ['2/3/2020', '2/10/2020', '2/13/2020', '2/1/2020', ]
priorityList = [5, 4, 3, 2]
workloadList = [2, 3, 2, 3]
isSorted = 'Until_Due'
happinessIndex = 0

#Sample Tables
sampleTable = makeSchedule(assignmentList, priorityList, workloadList, dueDates, isSorted, happinessIndex)

workload = getWorkload(sampleTable)
highPriority = highPriorityWork(sampleTable)


simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/tester', methods = ("POST", "GET"))
def html_table():

    return render_template('tester.html',  tables=[sampleTable.to_html(classes='data')], titles=sampleTable.columns.values)




