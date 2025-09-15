 
## Day 2 Challenge: Python Basics 🐍 
 #This problem will test  your understanding of loops, conditionals (if%e==0lif%e==0lse), and basic data type manipulatio n.
 #The Task :
 #Write a single Python function called number_game that takes one integer, n, as an argumen t. The function should loop through all numbers from 1 to n (inclusive) and print a specific output based  on the following rules, in this exact order of priority:
 # If the number contai ns the digit '7' (e.g., 7, 17 , 27), it must print "Lucky". This rule  overrides al l others .
 # If the number is a m ultiple of both 3 and 5, it must print "FizzBuzz" .
 #If the number is a multiple of only 3, it must print "Fizz".
 # If the number is a multiple of only 5, it must print "Buzz" .
 #Otherwise, it should just print the number itself .
try:
   n=int(input("< enter your number"))
   def number_game(n):
    
#If the number contains the digit '7' (e.g., 7, 17, 27), it must print "Lucky". This rule overrides all others.    
   
    for check  in range(1,n+1):
        if  '7' in str(check):
         print("lucky")
         
        elif check%3==0 and check%5==0:
            print("fizzbuzz")
        elif check%3==0 :
            print("fizz")
        elif check%5==0 :
            print("buzz")
        else:
            print(f"{check}")        
   number_game(n)                       
except:
    print("enter correct number")
 


"""## Day 2 Challenge: The Remix 🔁
The Task: The Prime Number Finder
Write a single Python function called analyze_primes that takes one integer, n, as an argument. The function must:
Find and print every prime number between 2 and n (inclusive).
After finding all the primes, it should print the total count of how many prime numbers were found.
## What is a Prime Number?
A prime number is a number greater than 1 that has only two divisors: 1 and itself. For example, 5 is a prime number because it can only be divided by 1 and 5. 
The number 6 is not prime because it can be divided by 1, 2, 3, and 6."""


n=int(input("< enter n number"))
def analyze_prime(n):
   count=0
   for check in range(2,n+1):
      is_prime=True
      for divisor in range(2, check):
        if check%divisor==0:
           is_prime=False
           break
      if is_prime:
         print(check)
         count=count+1    
   print(f"total prime numbers are {count}")    
analyze_prime(n)


#correct solution     
word=input('enter the palan word')
def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")

    n = 0
    i = len(word) - 1

    while n < i:
        if word[n] != word[i]:
            return False
        n = n + 1
        i = i - 1

    return True

# Example Usage
word = input("Enter your word: ")
if is_palindrome(word):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

#"The quick brown fox jumps over the lazy dog.
def word_frequency(text):
    # 1. Preprocess the string: make it lowercase and split it into words.
    text = text.lower()
    words = text.split()
    
    # 2. Create an empty dictionary to store the counts.
    word_counts = {}
    
    # 3. Loop through each word in the list.
    for word in words:
        # 4. Check if the word is already a key in our dictionary.
        if word in word_counts:
            # If it is, increment its count by 1.
            word_counts[word] += 1
        else:
            # If it's a new word, add it to the dictionary with a count of 1.
            word_counts[word] = 1
            
    # 5. After the loop is finished, return the final dictionary.
    return word_counts

# --- Example Usage ---
sentence = "The quick brown fox jumps over the lazy dog."
frequencies = word_frequency(sentence)
print(frequencies)
      


   
