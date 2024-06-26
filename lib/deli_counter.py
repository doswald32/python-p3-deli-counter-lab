katz_deli = []

def line(deli_line):
    sent_start = "The line is currently:"
    if deli_line:
        for i, name in enumerate(deli_line, start=1):
            addition = f' {i}. {name}'
            sent_start += addition
        print(sent_start)
    else: 
        print("The line is currently empty.")
    
def take_a_number(line, name):
    line.append(name)
    print(f"Welcome, {name}. You are number {line.index(name) + 1} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else: 
        print(f'Currently serving {deli_line[0]}.')
        rev_line = deli_line[1:]
        print(rev_line)
        

