
filepath='D:/365-Day-Data-AI-Roadmap/notes/mbox-short.txt'
print('trying to access the file')
unique_senders=[]

try:
    with open(filepath,'r') as file:
        for line in file:  
           line=line.rstrip()
           line=line.split()
           for word in line:
               if word=="From":
                    
                   
                   if line[1] not in unique_senders:
                       unique_senders.append(line[1])
                       for unique in unique_senders:
                           
                           unique=unique.split()
                       print(unique[0])

    count=len(unique_senders)  
    print(count)   
                               

except FileNotFoundError:
    print(f'file not found in path {filepath}')     