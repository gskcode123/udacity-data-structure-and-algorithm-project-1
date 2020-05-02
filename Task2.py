import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

total_numbers = set()
for i in calls:
    total_numbers.add(i[0])
    total_numbers.add(i[1])
d1 = 0
final_dict = {}
for i in total_numbers:
    for j in calls:
        if i==j[0] or i==j[1]:
            d1 = int(j[3]) + d1
        final_dict.update( {i : d1} ) 
    d1 = 0

list1 = []
for i in final_dict:
    list1.append(final_dict[i])
vallll = max(list1)

def get_key(val): 
    for key, value in final_dict.items(): 
         if val == value: 
             return key
keey = get_key(max(list1))
print(keey + " spend the longest time, "+ str(vallll) + " seconds, on the phone during September 2016.")
