import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

total_numbers = []
total_numbers1 = set()
for i in calls:
  ss = i[0]
  rr = i[1]
  if ss[:5]=='(080)':
    if '(0' in rr:
      total_numbers.append(rr.split(')')[0][1:])
    elif '' in rr:
      total_numbers.append(rr.split()[0])
    elif rr[:3]=='140':
      total_numbers.append(rr[:3])
for ii in total_numbers:
  total_numbers1.add(ii)
total_banglaro_call_count = 0
total_calls = len(total_numbers)
for i in total_numbers:
  if i == '080':
    total_banglaro_call_count += 1
part2_ans = (total_banglaro_call_count/total_calls)*100

print("The numbers called by people in Bangalore have codes:")
for i in sorted(total_numbers1):
  print(i)
print("The list of codes should be print out one per line in lexicographic order with no duplicates")
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(part2_ans))
