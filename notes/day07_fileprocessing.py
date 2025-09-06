#new line 
name="nilesh/nmukati"
print(name)
#searching something in file using for loop and iteration
"""xfile=open('mbox.txt')   #just for example this dosent exist 
for cheese in xfile:
    print(cheese)"""

#counting lines in a file 
xfile=open('C:/Users/niles/Downloads/roadmapfinal.txt')
count=0
for everyline in xfile:
  
        count=count+1
print("line count",count)

#reading the whole file

fhand=open('C:/Users/niles/Downloads/roadmapfinal.txt')
inp=fhand.read()
print(len(inp))
print(inp[:300]) 

#searching through a file  
"""
fhand=open('C:/Users/niles/Downloads/roadmapfinal.txt')

for line in fhand:
    line=line.rstrip()
    if line.startswith('Ultimate'):
       print (line)"""
#searching through a file  using not and continue 
fhand=open('C:/Users/niles/Downloads/roadmapfinal.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('Ultimate'):
       continue 
    print (line)

#lets try other examples 
file_path = 'D:/365-Day-Data-AI-Roadmap/notes/mydiary.txt'  # The name of the file to read

print("Attempting to read the file...")

try:
    with open(file_path, 'r') as file:
        # 'r' stands for read mode
        content = file.read()  # .read() gets everything as a single string
        
        print("/n--- File Content ---")
        print(content)
        print("--------------------")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Make sure it's in the right folder.")

print("/nReading process finished.")

#one by self now

file_path='C:/Users/niles/Downloads/hey Nilesh how are you buddy hope y.txt'
print('attempting to open the file')
try:
     with open(file_path,'r') as file:
          content=file.read()
          print(content)
except FileNotFoundError:
     print(f"error:file dosent exist or {file_path} not found")          

#exercise Exercise 1: Write a program to read through a file
#  and print the contents of the file (line by line) all in upper case.
file_path='D:/365-Day-Data-AI-Roadmap/notes/mboxshort.txt'
print("trying to open the file ")
try:
     with open(file_path,'r') as file:
          content=file.read()
          print(content.upper())
except:
     print(f'file name not found or path for{file_path} unable to access')          

        
          
          
     