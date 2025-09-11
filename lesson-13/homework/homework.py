
#Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Ask user for birthdate input
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    # Convert input string to a datetime object
    birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
    today = datetime.today()

    # Calculate difference using relativedelta
    age = relativedelta(today, birthdate)

    # Display the result
    print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")

except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")


#Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
from datetime import datetime,timedelta

birthdate_str=input("your birthdate(MM-DD):")
birthday_month,birthday_day=map(int,birthdate_str.split("-"))
today=datetime.today()
current_year=today.year
next_birthday=datetime(current_year,birthday_month,birthday_day)
if next_birthday<today:
    next_birthday=datetime(current_year+1,birthday_month,birthday_day)
days_remaining=(next_birthday-today).days
print(f'your next birthday is in {days_remaining}:day!')


#Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime,timedelta
current_datetime_str=input('Enter the current date and time (YYYY-MM-DD HH:MM):')
current_datetime=datetime.strptime(current_datetime_str,"%Y-%m-%d %H:%M")
hours=int(input("enter you meeting hours:"))
minutes=int(input("enter you meeting minutes:"))
durations=timedelta(hours=hours,minutes=minutes)
end_datetime=current_datetime+durations
print(f'the metting will end at:{end_datetime.strftime('%Y-%m-%d %H:%M')}')


#Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

# Step 2: Get user input
datetime_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_timezone_str = input("Enter your current timezone (e.g., 'Asia/Kolkata'): ")
to_timezone_str = input("Enter the timezone to convert to (e.g., 'America/New_York'): ")

# Step 3: Parse the input datetime
naive_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

# Step 4: Set the current timezone
from_timezone = pytz.timezone(from_timezone_str)
localized_datetime = from_timezone.localize(naive_datetime)

# Step 5: Convert to target timezone
to_timezone = pytz.timezone(to_timezone_str)
converted_datetime = localized_datetime.astimezone(to_timezone)

#Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re
def is_valid_email(email):
    pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None
def main():
    email=input("Enter an email address to validate: ")
    if is_valid_email(email):
        print("✅ Valid email address.")
    else:
        print("❌ Invalid email address.")
if __name__=="__main__":
    main()

#Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re
def format_phone_number(phone):
    digits=re.sub(r'\D', '', phone)

    if len(digits) !=10:
        return None
    
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
def main():
    user_input=input("Inter phone number")
    formatted=format_phone_number(user_input)
    if formatted:
        print(f"📞 Formatted Number: {formatted}")
    else:
        print("❌ Invalid phone number. Please enter exactly 10 digits.")

if __name__=="__main__":
    main()

#Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
import re
def find_word_occurences(text,word):
    matches=list(re.finditer(rf'\b{re.escape(word)}\b', text, re.IGNORECASE))
    if matches:
        print(f"\n🔍 Found {len(matches)} occurrence(s) of the word '{word}':\n")
        for i,match in enumerate(matches,1):
            start,end=match.start(),match.end()
            print(f"{i}. Position: {start}-{end} ➜ '{text[start:end]}'")
    else:
        print(f"\n❌ The word '{word}' was not found in the text.")
def main():
    sample_text="""
    Python is a powerful programming language. Many developers love Python because of its simplicity and readability.
    Python can be used for web development, data analysis, AI, and more. PYTHON is truly versatile.
    """
    print("📘 Sample Text:")
    print(sample_text.strip())
    search_word=input("\nEnter the word to search for: ").strip()
    find_word_occurences(search_word,sample_text)
if __name__=="__main__":
    main()
