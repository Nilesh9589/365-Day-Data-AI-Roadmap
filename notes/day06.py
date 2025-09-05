name='nilesh'
letter=name

print(letter[0]+letter[1]+letter[2]+letter[3]+letter[4]+letter[5])


#string length

name="nilesh"
print(len(name))

#looping through string
name="nilesh"        
index=0
while index<len(name):    
    letter=name[index]     
    print(letter)
    index=index+1

#looping through the for loop

name='nilesh'

for length in name:
    print(length)

#looping and counting
#suppose we have nilesh and we want to know how  many time n was used 

name='nilesh'
count=0
for length in name:
    if length=='n':
        count=count+1

print(count)        

name='nilesh mukati'
print(name[0:6])    #: sign is cut through basically if we talk indexing it would be 5
print(name[7:13])   # space is also counted in indexing 

print(name[:13])  #by default if we leave the first one it would count as beginning and 
print(name[0:])                  #$same if we leave last


#lets use in operator in string 
name='nilesh'
if 'n' in name:
    print(True)

#string comparison it uses dictionary wise or alphabetical 

name=str(input(""))
if name=='nilesh':
    print("all right , good to go")   
elif name<'nilesh': 
    print("smaller")
elif name>'nilesh':
    print("larger")    

#string function library codes
name='nileshMukati'
change=name.lower()  #will change all to smalller 
print(change)






    
   

