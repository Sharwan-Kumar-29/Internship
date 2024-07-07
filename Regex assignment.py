#!/usr/bin/env python
# coding: utf-8

# In[31]:


import regex as re
import pandas as pd

Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
Sample Text- 'Python Exercises, PHP exercises.'

Expected Output: Python:Exercises::PHP:exercises:

# In[32]:


text='Python Exercises, PHP exercises.'
pattern=r"[\s.,]"
result=re.sub(pattern,":",text)
print(result)

Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
Expected output-
0      hello world
1             test
2    four five six

# In[33]:


Dict={'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df=pd.DataFrame(Dict)
df["SUMMARY"]=df["SUMMARY"].str.replace(r"\.|,|!|X+|\d+|:|;","",regex=True)


# In[34]:


df

Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
# In[35]:


def char_find(string):
    pattern=re.compile(r"\w{4,}")
    result=pattern.findall(string)
    return result
char_find("It includes both uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_).")

Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# In[36]:


def char_find3_5(string):
    pattern=re.compile(r"\w{3,5}")
    result=pattern.findall(string)
    return result
char_find3_5("It includes both uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_).")

Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output:
example.com
hr@fliprobo.com
github.com
Hello Data Science World

# In[37]:


def remove_parentheses(list1):
    pattern=re.compile(r'[()]')
    for i in list1:
        result=pattern.sub("",i)
        print(result)
remove_parentheses(["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"])
    

Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
Note- Store given sample text in the text file and then to remove the parenthesis area from the text.


# In[38]:


#Entering the text into the file

sample_text=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
with open("sample.txt", "w") as file:
    for i in sample_text:
        file.write(f"{i}\n")
#Manuplating the text in the file

pattern=re.compile(r"\s+\(.+\)")    
with open("sample.txt", "r") as file:
     original_text = file.read() 
#print(original_text)

cleaned_text=pattern.sub("",original_text)

#print(cleaned_text)

with open("sample.txt","w") as file:
    file.write(cleaned_text)
    
#showing the output/read the file:

with open("sample.txt", "r") as file:
        text=file.read()
print(text)

        

Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”
Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

        
# In[39]:


pattern=re.compile(r"[A-Z][a-z]*")
sample="ImportanceOfRegularExpressionsInPython"
result=pattern.findall(sample)
print(result)

Question 8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

# In[40]:


text="RegularExpression1IsAn2ImportantTopic3InPython"
pattern = r'(\d+)([A-Za-z]+)'
result = re.sub(pattern, r' \1\2', text)#substitute it with space before first capture group and followed by second capture group
print(result)

Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

# In[41]:


def space(text):
    pattern = r'(\d+)([A-Za-z]+)'
    result = re.sub(pattern, r' \1 \2', text)# there is space before and after the first capture group and followed by second group
    return result
space(text)

Question 10-
# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[42]:


import pandas as pd


# In[43]:


df=pd.read_csv("https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv")


# In[44]:


df


# In[45]:


pattern=r'(\w{1,6})'
df["First_five_letter"]=df.Country.str.extract(pattern)


# In[46]:


df

Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[47]:


def match_word(string):
    pattern=re.compile(r'^\w+$')
    result=pattern.match(string)
    if result:
        print(f"\"{string}\" is valid string")
    else:
        print(f"\"{string}\" is invalid string")
    


# In[48]:


match_word("Hello_love123")
match_word("Hello@134")

Question 12- Write a Python program where a string will start with a specific number. 


# In[49]:


def start_with(string,specific_no):
    str_num=str(specific_no)
    
    pattern=re.compile(str_num)
    result=pattern.match(string)
    if result:
        print(f"String starts_with {specific_no} ")
    else:
        print(f"String doesn't starts_with {specific_no} ")
    


# In[50]:


start_with("40 is the start of thestring",40)
start_with("40 is the start of thestring",42)

Question 13- Write a Python program to remove leading zeros from an IP address
# In[ ]:



    


# In[51]:


def remove_leading_zeros(ip_address):
    
    IP_list = ip_address.split(".")

   
    cleaned_list = [str(int(i)) for i in IP_list]

    
    cleaned_ip = ".".join(cleaned_list)

    return cleaned_ip

# Example usage
ip_address = "192.010.001.100"
cleaned_ip = remove_leading_zeros(ip_address)
print(f"Original IP: {ip_address}")
print(f"Cleaned IP: {cleaned_ip}")


# In[ ]:




Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Expected Output- August 15th 1947
Note- Store given sample text in the text file and then extract the date string asked format

# In[52]:


sample_txt=" On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country"
with open("sample.txt","w") as file:
    file.write(sample_txt)
with open("sample.txt","r") as file:
     output=file.read()
date_pattern = re.compile(r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(st|nd|rd|th)\s+(\d{4})")
result=date_pattern.findall(output)
for i in result:
    out=" ".join(i)
out

Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

# In[53]:


def search_literals(text):
    pattern=re.compile(r"fox|dog|horse")
    found_words = pattern.findall(text)
    return found_words


text = 'The quick brown fox jumps over the lazy dog.'

result = search_literals(text)

if result:
    print(f"Found words: {', '.join(result)}")
else:
    print("No matching words found.")

Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

# In[54]:


def search_lit_add(text):
    pattern=re.compile(r"(fox)")
    address = pattern.search(text)
    return address


text = 'The quick brown fox jumps over the lazy dog.'

search_lit_add(text)



Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.

# In[55]:


sample="Python exercises, PHP exercises, C# exercises"

pattern=r"exercises"
result=re.findall(pattern,sample)
result

Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
# In[59]:


def find_substring_positions(text, substring):
    positions = []
    start = 0

    while True:
        index = text.find(substring, start)
        if index == -1:
            break
        positions.append(index)
        start = index + 1

    return positions


sample_text = "The quick brown fox jumps over the lazy dog fox."
searched_substring = "fox"

substring_positions = find_substring_positions(sample_text, searched_substring)

if substring_positions:
    print(f"'{searched_substring}' occurs at positions: {', '.join(map(str, substring_positions))}")
else:
    print(f"'{searched_substring}' not found in the text.")

Question 21- Write a Python program to separate and print the numbers and their position of a given string.
# In[63]:


string = "The quick brown fox jumps 123 over 456 the lazy dog."
numbers = []
for index, char in enumerate(string):
    if char.isdigit():
        numbers.append((char, index))
if len(numbers)>=1:
    print("Numbers and their positions:")
    for num, pos in numbers:
        print(f"Number {num} found at position {pos}.")
else:
    print("No numbers found in the text.")

Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
Expected Output: 950

# In[64]:


string="My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
pattern=re.compile(f"\d+")
result=pattern.findall(string)
print(max(result))

Question 23- Create a function in python to insert spaces between words starting with capital letters.
Sample Text: “RegularExpressionIsAnImportantTopicInPython"
Expected Output: Regular Expression Is An Important Topic In Python

# In[81]:


pattern=re.compile(f"([^A-Z][a-z]*)")
text="RegularExpressionIsAnImportantTopicInPython"
result=pattern.sub(r"\1 ",text)
result

Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
# In[82]:


text = "The Quick brown Fox jumps over the lazy Dog."
pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, text)
print("Matches found:")
for match in matches:
    print(match)

Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
Sample Text: "Hello hello world world"
Expected Output: Hello hello world

# In[83]:


string="Hello hello world world"
regex=r"\b(\w+)(?:\W+\1\b)+"
x=re.sub(regex,r"\1",string)
print(x)

Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.
# In[85]:


text="hello this is 123"
pattern = r'^.*[a-zA-Z0-9]$'  # Alphanumeric character at the end
if re.match(pattern, text):
    print(f"'{text}' is valid (ends with an alphanumeric character).")
else:
    print(f"'{text}' is not valid (does not end with an alphanumeric character).")

Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[102]:


text= """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered 
USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern=re.compile(r"#[A-Za-z]+")
result=pattern.findall(text)
if result:
    print("Extracted hashtags:")
    for hashtag in result:
        print(hashtag)
else:
    print("No hashtags found in the text.")
    


# In[ ]:




Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

# In[108]:


text="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
pattern=re.compile(r'<U\+[\w]+>')
result=pattern.sub("",text)
print(result)

Question 29- Write a python program to extract dates from the text stored in the text file.
Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
Note- Store this sample text in the file and then extract dates.

# In[113]:


text=" Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
with open("date.txt","w") as file:
    file.write(text)
pattern=re.compile(r"\s(\d{2}-\d{2}-\d{4})")
with open("date.txt","r") as file:
    inp=file.read()
result=pattern.findall(inp)
print("Extracted_date:")
for i in result:
    print(i)
    

Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.
Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[119]:


text="The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pattern=re.compile(r'\b\w{2,4}\b')
result=pattern.sub("",text)
print(result)


# In[ ]:




