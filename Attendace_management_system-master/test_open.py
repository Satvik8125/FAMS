import os
import csv

# Simulate the cs construction
base = 'C:\\Users\\panda\\OneDrive\\Desktop\\Attendace_management_system-master\\Attendace_management_system-master'

Subject = 'maths'
date = '2026-02-03'
Hour = '13'
Minute = '22'
Second = '28'

filename_part = f"{Subject}_{date}_{Hour}-{Minute}-{Second}.csv"
fileName = os.path.join('Attendance', filename_part)
cs = os.path.join(base, fileName)

print("Testing file open for:", cs)

try:
    with open(cs, newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        print("File opened successfully. First few rows:")
        for row in rows[:5]:  # Print first 5 rows
            print(row)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
except Exception as e:
    print("Other error:", e)
