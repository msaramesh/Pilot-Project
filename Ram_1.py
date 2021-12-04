# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:27:27 2021

@author: mutyala
"""

Marks1 = int(input("Enter English Marks :"))
Marks2 = int(input("Enter Hindi Marks :"))
# Pass or Fail
if Marks1 >=35 and Marks2 >=35 and Marks1 <=100 and Marks2 <=100:
  print("RESULT", "Congratulation Pass")
elif Marks1 >100 or Marks2 >100:
  print("RESULT", "Error Marks entered wrongly")
else:
  print("RESULT", "Fail Better luck next time")
# Total Marks
if Marks1 >=35 and Marks2 >=35 and Marks1 <=100 and Marks2 <=100:
    print("TOTALMARKS", Marks1 + Marks2)
elif Marks1 >100 or Marks2 >100:
    print("TOTALMARKS", "NA")
# Percentage
if Marks1 >=35 and Marks2 >=35 and Marks1 <=100 and Marks2 <=100:
    print("PERCENTAGE", ((Marks1 + Marks2) / 200) * 100)
elif Marks1 >100 or Marks2 >100:
    print("PERCENTAGE", "NA")