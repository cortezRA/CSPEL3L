import matplotlib.pyplot as plt
import csv
  
Names = []
Values = []
  
with open('bpmeasure.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        Names.append(row[0])
        Values.append(int(row[1]))
  
plt.scatter(Names, Values, color = 'darkblue',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('Names')
plt.ylabel('Values')
plt.title('Patients Blood Pressure Report', fontsize = 20)
  
plt.show()