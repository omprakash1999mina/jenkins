from datetime import datetime

now = datetime.now()
# Format the date and time
formatted_datetime = now.strftime("%d-%m-%Y %H:%M %A")
print(formatted_datetime)