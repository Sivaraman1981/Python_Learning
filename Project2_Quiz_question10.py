import json
import sys

f = open("C:\\Siva_OldLaptop\\Laptop_E_prompt\\NOTES\\Python\\Quiz.json")

data = json.load(f)

for i in data['Questions']:
    print(i)
 
# Closing file
f.close()
