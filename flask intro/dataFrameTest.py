from flask import Flask, render_template, url_for, Blueprint, request, jsonify
import quickstart
import requests
import pandas as pd
import numpy as np
import datetime as dt
import math

assignmentList = []
dueDates = []
priorityList = []
workloadList = []
isSorted = ''
happinessIndex = 0
emotionalState = ''
nightTime = []

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

def addAssignmentName(name):
    assignmentList.append(name)

def addPriority(priority):
    priorityList.append(priority)

def addWorkLoad(workload):
    workloadList.append(workload)

def addDate(date):
    dueDates.append(date)

def setHappiness(index):
    happinessIndex = index

def setEmotions(emotions):
    emotionalState = emotions

def setNightTime(weekday, weekend):
    nightTime.append(weekday)
    nightTime.append(weekend)

#Sample Tables
sampleTable = makeSchedule(assignmentList, priorityList, workloadList, dueDates, isSorted, happinessIndex)
#workload = getWorkload(sampleTable)
#highPriority = highPriorityWork(sampleTable)


# Algorithm: Calculate priorities(on our own) based on dueDates and workload.dueDate
# Assignments with more workload but same due date should be higher priority
#Large workloads should be distributed
#Less work depending on mental happines/emotions, or plan mental changing events
#def planEvents():

simple_page = Blueprint('simple_page', __name__, template_folder='templates')
#@simple_page.route('/calendar', methods = ("POST","GET"))
def html_table():
    evDict = {}
    events = quickstart.getEvents()
    for e in events:
        if "dateTime" in e["start"]:
            hour = e['start'].get('dateTime')
            evDict[e["summary"]]=hour

    return evDict





