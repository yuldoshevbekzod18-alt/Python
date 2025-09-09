#Create your own virtual environment and install some python packages.
import os
import sys
import subprocess


evn_name='myenv'

print(f'creating virtual environment{evn_name}')
subprocess.run([sys.executable, "-m", "venv", env_name])

#Create custom modules.
#Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
#Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
# math_operations.py
# main.py
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

print('Add:', add(20, 30))
print('Subtract:', subtract(20, 30))
print('Multiply:', multiply(20, 30))
print('Divide:', divide(60, 4))

print('Reversed string:', reverse_string("Python"))
print('Count vowels:', count_vowels("Python best programm"))


#Create custom packages.
#Create geometry package.
# geometry\
#     __init__.py
#     circle.py
#geometry
import math

def area(radius):
    return math.pi*radius*radius
def circumference(radius):
    return 2*math.pi*radius
from .circle import area, circumference
from geometry_circle import area, circumference
r=5
print("circle area:", area(r))
print("circle circumference:",circumference(r))


#3
import math
def calculate_area(radius):
    return math.pi * radius ** 2
def calculate_circumference(radius):
    return 2 * math.pi * radius

def read_file(file_path):
    with open(r'file_path','r')as file:
        return file.read()

def write_file(file_path,content):
    with open('file_path','w')as file:
         file.write(content)

from circle import calculate_area, calculate_circumference
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

def main():
    radius = 7

    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    content = f"Circle with radius {radius}:\nArea = {area}\nCircumference = {circumference}\n"

    file_path = "circle_info.txt"

    write_file(file_path, content)

    saved_content = read_file(file_path)
    print("Content read from file:")
    print(saved_content)

if __name__ == "__main__":
    main()
  
