# WAF to find in which of the line does word "using" occur first. print -1 if word does not found in file.
def check_line():         #we already created a file "practice.txt" and written some line in it,before this program.
    word="using" 
    line_no=1
    data=True    
    with open("practice.txt","r")as f:
        while data:
            data=f.readline()
            if word in data:
                print(line_no)
                return
            line_no+=1
    return -1    
print(check_line())