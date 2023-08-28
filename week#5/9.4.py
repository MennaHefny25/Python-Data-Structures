"""

9.4 Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of 
mail messages. 
The program looks for 'From ' lines and takes 
the second word of those lines as the person 
who sent the mail. The program creates a 
Python dictionary that maps the sender's mail 
address to a count of the number of times they 
appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum 
loop to find the most prolific committer.

"""


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)


email_counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        email_address = words[1]
        if email_address not in email_counts:
            email_counts[email_address] = 1
        else:
            email_counts[email_address] += 1

max_key = None
max_sender = None
for key, value in email_counts.items():
    if max_key is None or value > max_key:
        max_key = value
        max_sender = key
        

print(max_sender, max_key)