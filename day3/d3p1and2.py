import re

def regex_build():
    f = open('day3/inputfile.txt', 'r')
    testsstring = f.read()
    pattern = re.compile(r'mul\(\d*,\d*\)|do\(\)|don\'t\(\)')
    result = pattern.findall(testsstring)
    cleaned_output = []
    enabled = "do"
    for val in result:
        if val == "don't()":
            enabled = "don't"
        elif val == "do()":
            enabled = "do"
        if enabled == "do" and val !='do()':
            val = val.replace('mul(','')
            val = val.replace(')','')
            cleaned_output.append(val)
        else:
            pass
    multiplier(cleaned_output)

def multiplier(input):
    total = 0
    for val in input:
        array = val.split(',')
        product = int(array[0])*int(array[1])
        total = total+product
    print(total)

def main():
    regex_build()

main()