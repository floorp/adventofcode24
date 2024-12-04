import re

def regex_build():
    f = open('day3/inputfile.txt', 'r')
    testsstring = f.read()
    # testsstring = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    pattern = re.compile(r'mul\(\d*,\d*\)|do\(\)|don\'t\(\)')
    result = pattern.findall(testsstring)
    print(result)
    cleaned_output = []
    enabled = "do"
    for val in result:
        print(val)
        if val == "don't()":
            enabled = "don't"
        elif val == "do()":
            enabled = "do"
        print(enabled)
        if enabled == "do" and val !='do()':
            val = val.replace('mul(','')
            val = val.replace(')','')
            cleaned_output.append(val)
        else:
            pass
    print(cleaned_output)
    multiplier(cleaned_output)

def multiplier(input):
    total = 0
    for val in input:
        array = val.split(',')
        print(array)
        product = int(array[0])*int(array[1])
        total = total+product
    print(total)

def main():
    regex_build()

main()