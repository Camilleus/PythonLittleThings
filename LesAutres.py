"""
lOGICAL VARIABLES



is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

access = False
is_admin = False
is_active = False
is_permission = False

if access is 1:
    is_permission = True
else:
    is_permission = False

if is_admin is True:
    is_permission = True
    is_active = True
else:
    is_admin = False

if access is True and is_active is True:
    is_permission = True
    is_active = True
else:
    is_permission = False
    is_active = False

if is_permission is True:
    acces = True
else:
    acces = False

"""
"""
SQUARE EQUATION


import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
elif D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
else:
    D < 0
"""
"""
GREATEST COMMON DIVISOR



first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = int( first if first < second else second)
smaller = int( first if first < second else second)
bigger = int( first if first > second else second)

while bigger % gcd != 0 :
    gcd -= 1
    print(gcd)
    if bigger % int(gcd) == 0:
        if smaller % int(gcd) != 0:
            gcd -= 1
            print(gcd)
        else:
            print(gcd)
"""
"""
CAESAR'S CODE



message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    letter = ""
    if not ch.isalpha():
        encoded_message += ch
        continue
    if 65 <= ord(ch) <= 90:
        letter = "A"
    else:
        letter = "a"
    pos = ord(ch) - ord(letter)
    pos = (pos + offset) % 26
    new_char = chr(pos + ord(letter))
    encoded_message += new_char     
"""
"""
FIBONACCI SEQUENCE


def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input)
for i in range(nterms):
    print(f"Fibonacci sequence:{fibonacci(i)}")
"""
"""
Factorial / Silnia



def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)# 120

"""
"""
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    founded_articles = []
    for article in articles_dict:
        title = article['title']
        author = article['author']
        year = article['year']

        if not letter_case:
            key = key.lower()
            title_lower = title.lower()
            author_lower = author.lower()
        else:
            title_lower = title
            author_lower = author

        if key in title_lower or key in author_lower:
            founded_articles.append({
                'author': author,
                'title': title,
                'year': year
            })

    if not founded_articles:
        print("Not found")

    return founded_articles

"""
"""
import re


def find_word(text, word):
    search_result = re.search(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)

    if search_result:
        result_dict = {
            'result': True,
            'first_index': search_result.start(),
            'last_index': search_result.end() - 1,
            'search_string': search_result.group(),
            'string': text
        }
    else:
        result_dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }

    return result_dict
"""
"""
import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        word_pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
        text = word_pattern.sub('*' * len(word), text)
    return text

"""
"""
import re

def find_all_emails(text):
    all_emails = re.compile(r"[a-zA-Z][a-zA-Z0-9_.]+@[a-z]+\.[a-z]{2,}")
    result = all_emails.findall(text)
    return result
"""
"""
import re


def find_all_phones(text):
    all_phones = re.compile(r'\+380\(\d{2}\)777-\d{1,2}-\d{2,3}')
    result = all_phones.findall(text)
    return result


text = "Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"
phones = find_all_phones(text)
print(phones)

"""
"""
def write_employees_to_file(employee_list, path):
    with open(path, "w") as file:
        for department in employee_list:
            for employee in department:
                file.write(employee + "\n")
    file.close()


employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'], ['Drake Mikelsson,19']]
write_employees_to_file(employee_list, "employee_data.txt")
"""
"""
def add_employee_to_file(record, path):
    file = open(path, 'a')  # Otwieranie pliku w trybie dodawania (append)
    file.write(record + '\n')  # Dodawanie nowego pracownika i nowej linii
    file.close()

# Przykład użycia:
add_employee_to_file("Drake Mikelsson,19", "employee_data.txt")
"""
"""
def get_cats_info(path):
    cats_info = []

    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            cat_info = {
                "id": parts[0],
                "name": parts[1],
                "age": parts[2]
            }
            cats_info.append(cat_info)

    return cats_info

# Przykład użycia:
path = "cats_data.txt"
cats_data = get_cats_info(path)
print(cats_data)
"""
"""
def get_recipe(path, search_id):
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == search_id:
                recipe = {
                    "id": parts[0],
                    "name": parts[1],
                    "ingredients": parts[2:]
                }
                return recipe
    
    return None

# Przykład użycia:
path = "recipes.txt"
search_id = "60b90c3b13067a15887e1ae4"
recipe = get_recipe(path, search_id)
if recipe:
    print(recipe)
else:
    print("Przepis o podanym ID nie został znaleziony.")

"""
"""
def sanitize_file(source, output):
    with open(source, 'r') as source_file:
        content = source_file.read()
        sanitized_content = ''.join([char for char in content if not char.isdigit()])
    
    with open(output, 'w') as output_file:
        output_file.write(sanitized_content)

# Przykład użycia:
source_file_path = "source.txt"
output_file_path = "output.txt"
sanitize_file(source_file_path, output_file_path)
print("Plik został oczyszczony i zapisany do", output_file_path)
"""
"""
def save_applicant_data(source, output):
    with open(output, 'w') as output_file:
        for applicant in source:
            name = applicant["name"]
            specialty = applicant["specialty"]
            math_score = applicant["math"]
            lang_score = applicant["lang"]
            eng_score = applicant["eng"]
            output_line = f"{name},{specialty},{math_score},{lang_score},{eng_score}\n"
            output_file.write(output_line)

# Przykład użycia:
applicant_data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output_file_path = "output.txt"
save_applicant_data(applicant_data, output_file_path)
print("Dane kandydatów zostały zapisane do pliku", output_file_path)
"""
"""
def is_equal_string(utf8_string, utf16_string):
    decoded_utf8 = utf8_string.encode('utf-8').decode('utf-8')
    decoded_utf16 = utf16_string.encode('utf-16').decode('utf-16')
    
    return decoded_utf8 == decoded_utf16

# Przykład użycia:
utf8_string = "Hello, world!"
utf16_string = "Hello, world!".encode('utf-16').decode('utf-16')
result = is_equal_string(utf8_string, utf16_string)
print(result)  # Oczekiwane wyjście: True
"""
"""
def is_equal_string(utf8_string, utf16_string):
    utf8_normalized = utf8_string.decode('utf-8').casefold().encode('utf-8')
    utf16_normalized = utf16_string.decode('utf-16').casefold().encode('utf-8')
    return utf8_normalized == utf16_normalized
"""