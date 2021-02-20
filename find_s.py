#-------------------------------------------------------------------------
# AUTHOR: Jonathan Lu
# FILENAME: find_s.py
# SPECIFICATION: This program reads a file called csv.reader and finds the maximally specific hypothesis
# FOR: CS 4200- Assignment #1
# TIME SPENT: ~2 hours
#-----------------------------------------------------------*/

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open("C:/Users/Administrator/Desktop/contact_lens.csv", 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

for j in range(0, num_attributes):
    hypothesis[j] = db[0][j];

print("\n Find S: Finding a Maximally Specific Hypothesis\n")
for i in range(0,len(db)):
    if db[i][num_attributes]=='Yes':
        for j in range(0,num_attributes):
            if db[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
            else:
                hypothesis[j]=db[i][j]
    print("For Training instance No :{0} the hypothesis is".format(i),hypothesis)

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)