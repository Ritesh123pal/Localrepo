# return the line containing maximum nunber of digit characterin file.txt
max_digit=0
with open("file.txt","r")as f:
   for line in f:
      digit_count=0
      for char in line:
         if(char.isdigit ()):
            digit_count+=1
         if(digit_count>=max_digit):
            max_digit=digit_count   
print(line)            
