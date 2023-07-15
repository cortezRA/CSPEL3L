import matplotlib.pyplot as plt
import csv
  
subjects = []
scores = []
  
with open('subjectmarks.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        subjects.append(row[0])
        scores.append(int(row[1]))
  
plt.pie(scores,labels = subjects,autopct = '%.2f%%')
plt.title('Marks of a Student', fontsize = 20)
plt.show()