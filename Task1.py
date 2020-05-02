import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
total_Count = set()

for i in texts:
    total_Count.add(i[0])
    total_Count.add(i[1])
for j in calls:
    total_Count.add(j[0])
    total_Count.add(j[1])
print("There are "+str(len(total_Count)) + " different telephone numbers in the records")
    