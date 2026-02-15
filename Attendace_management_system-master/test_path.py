import os

# Simulate the path construction from Fillattendances function
base = 'C:\\Users\\panda\\OneDrive\\Desktop\\Attendace_management_system-master\\Attendace_management_system-master'

# Example values from the error
Subject = 'maths'
date = '2026-02-03'
Hour = '13'
Minute = '22'
Second = '28'

filename_part = f"{Subject}_{date}_{Hour}-{Minute}-{Second}.csv"
fileName = os.path.join('Attendance', filename_part)
cs = os.path.join(base, fileName)

print("Constructed fileName:", fileName)
print("Constructed cs (full path):", cs)

# Check if directories and file exist
print("Attendance directory exists:", os.path.exists('Attendance'))
print("Full path file exists:", os.path.exists(cs))

# Also check the old incorrect way for comparison
old_fileName = f"Attendance/{Subject}_{date}_{Hour}-{Minute}-{Second}.csv"
old_cs = base + old_fileName
print("Old incorrect fileName:", old_fileName)
print("Old incorrect cs:", old_cs)
print("Old path exists:", os.path.exists(old_cs))
