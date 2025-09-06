file_path=input("enter the file name with proper path")
count=0
total=0
print("path entered now will copy path and follow ")
try:
    with open(file_path,'r') as file:
         
        for line in file:
         
         if line.startswith('X-DSPAM-Confidence:'): 
            colpos=line.find(':')
            
            numpos=(line[colpos+1:])
            numpos=numpos.lstrip()
            numpos=float(numpos)
            
            total=numpos+total

            count=count+1
        print(float(numpos))    
        print(count)
        average=(total/count)
        print(average)
       
        
        

      
except:
    print(f"file not availabe or error happened while openinh {file_path}")


#D:/365-Day-Data-AI-Roadmap/notes/mbox-short.txt