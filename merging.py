import csv
import time

from csv import reader
start_time = time.time()
print(start_time)
fout=open("merging.csv","a")
#merging 13 files.........................
for num in range(1,14):
    for line in open("file"+str(num)+".csv"):
         fout.write(line)
#remiving duplicate data..................
inFile = open('merging.csv','r')

outFile = open('merging2.csv','w')

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()
#user input............................
print('Press 1 to view by Date.\n'
      'Press 2 to view by Daily new.\n'
      'Press 3 to view by Total confirmed cases.\n'
      'Press 4 to view by Daily new deaths.\n'
      'Press 5 to view by Total deaths.\n'
      'Press 6 to view by Daily new recovered.\n'
      'Press 7 to view by Total recovered.\n'
      'Press 8 to view by Daily New Tests.\n'
      'Press 9 to view by Total Tests.\n'
      'Press 10 to view by Active Cases.\n')

userChoice=int(input("Enter your choice:\n"))


if userChoice >10 :
    print ("Invaild choice!")
    
#By Date...............................
if userChoice == 1:
    userChoice1 = input("Enter Date(M/D/YYYY) :")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice1 == row[0]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])
                                    

#By Daily new.........................
if userChoice == 2:
    userChoice2 = input("Enter Daily new cases:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice2 == row[1]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])



#By Total confirmed cases...........
if userChoice == 3:
    userChoice3 = input("Enter Total confirmed cases:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice3 == row[2]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])
                                


#By Total Daily new deaths..........
if userChoice == 4:
    userChoice4 = input("Enter Total Daily new deaths:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice4 == row[3]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])

#By Total deaths.................
if userChoice == 5:
    userChoice5 = input("Enter Total deaths:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice5 == row[4]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])

#By Daily new recovered............
if userChoice == 6:
    userChoice6 = input("Enter Daily new recovered:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice6 == row[5]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])

#By Total recovered..............
if userChoice == 7:
    userChoice7 = input("Enter Total recovered:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice7 == row[6]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])

#By Daily New Tests.............
if userChoice == 8:
    userChoice8 = input("Enter Daily New Tests:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice8 == row[7]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])


#By Total Tests...........
if userChoice == 9:
    userChoice9 = input("Enter Total Tests:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice9 == row[8]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])

#By Active Cases........
if userChoice == 10:
    userChoice10 = input("Enter Active Cases:")
    with open('merging2.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if userChoice10 == row[9]: 
                                    print ('Date:',row[0])
                                    print ('Daily new confirmed cases:',row[1])
                                    print ('Total confirmed cases:',row[2])
                                    print ('Daily new deaths:',row[3])
                                    print ('Total deaths:',row[4])
                                    print ('Daily new recovered:',row[5])
                                    print ('Total recovered:',row[6])
                                    print ('Daily New Tests:',row[7])
                                    print ('Total Tests:',row[8])
                                    print ('Active Cases:',row[9])
end_time = time.time()
print(end_time)
