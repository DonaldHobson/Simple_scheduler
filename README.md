# Simple scheduler
This program uses linear optimization to help plan events.
It is small and written in python. If you are looking for something with a GUI, or don't know what the word "GUI" means, look elsewhere. 
If you want a sophisticated multifeatured software project, look elsewhere. If you want something with short and understandable code, this might do.
The input is taken to be a .csv file containing peoples prefferences and busynes on a numeric scale.

Suppose you have a number of different timeslots, and a number of different events to put in them.
You ask each person to rate how much they want to go to each event and how busy they are at each timeslot on a scale, (eg 0 to 5 or 1 to 10).

You put this data into a .csv file (this can be done automatically by some web forms).

The expected format is for the top row to be event and timeslot names, and the rest to be data.
The columns should consist of BLANK irrelevent lines (eg names, emails ect) followed by SLOT timeslot scores, followed by EVENT event scores.

The program will output the name of each timeslot that has anything happening at it, followed by the event name.
