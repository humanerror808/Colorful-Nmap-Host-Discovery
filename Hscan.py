import subprocess
import sys

def print_colored(text, color_code):
    print(color_code + text + '\033[0m')

def print_green(text, end='\n'):
    sys.stdout.write('\033[92m' + text + '\033[0m' + end)

command = "nmap -sP 192.168.1.0/24 | grep 192 | sed -e 's/Nmap scan report for //g' -e 's/)//g' -e 's/ (/ ==> /g'"
output = subprocess.check_output(command, shell=True, text=True)

lines = output.strip().split('\n')
for line in lines:
    arguments= line.split()
    first_argument = arguments[0]
    second_argument = arguments[1] if len(arguments) > 1 else ''
    third_argument = arguments[2] if len(arguments) > 2 else ''

    print_green(first_argument + ' ', end='')
    print(second_argument + ' ' + third_argument)
