import numpy as np
import pulp as pu
from itertools import *
BLANK=1 #The number of columns that come before slots or events

SLOTS=4
EVENTS=3

filename=input("File Name (.csv) >>")
with open(filename) as file:
    raw_file=file.readlines()
raw_file=[line.rstrip("\n") for line in raw_file]
#the first line contains column names, the rest contain data
column_names,raw_file=raw_file[0],raw_file[1:]

#splits up a big string into the parts representing slots and events.
def seperate(line,f=int):
    line=line.split(",")
    return [f(i) for i in line[BLANK:BLANK+SLOTS]],[f(i) for i in line[BLANK+SLOTS:BLANK+SLOTS+EVENTS]]

#calculates a persons utility matrix from a line.
# a utility matrix stores how much a person would benifit from each event being in each slot.
def person_utils(line):
    slot_u,event_u=seperate(line)
    combination=np.maximum(-np.subtract.outer(slot_u,event_u),0).astype(float)
    #the utility gain is the difference of the event utility, and the utility of whatever else you would be doing in the timeslot
    #except that if this utility is negitive, the person just won't attend, so take the maximum with 0
    if not np.all(combination==0):
        combination/=np.sum(combination)#normalize the utilities, to weigh everyones prefferences more evenly
    return combination
pref=sum(person_utils(line) for line in raw_file)-1/(20*EVENTS*SLOTS)
#summs everyones utilities
#slightly weighted towards no event unless someone wants to attend
prob = pu.LpProblem("Timetable", pu.LpMaximize)

indicators=np.full([SLOTS,EVENTS],None,np.object0)

for i,j in product(range(SLOTS),range(EVENTS)):
    indicators[i,j]=pu.LpVariable("tt%s,%s"%(i,j),0,1,pu.LpInteger)
#creates LPVariable objects for the linear optimizing.
#each variable represents an event at a timeslot.
#it is 1 iff the event is in that slot, else 0


prob+=(indicators*pref).sum(), "prefferences_to_be_maximized"
#the function of the variables that is to be optimized
for j in range(EVENTS):
    prob+=indicators[:,j].sum()<=1
#each event can happen at most once
for i in range(SLOTS):
    prob+=indicators[i,:].sum()<=1
#and each timeslot contains at most one event

prob.solve()

slot_n,event_n=seperate(column_names,str)
for i,j in product(range(SLOTS),range(EVENTS)):
    v=pu.value(indicators[i,j])
    if v>0:
        print(slot_n[i],"\n",event_n[j],"\n")
#print what happens when.
