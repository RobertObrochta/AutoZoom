# asks for user input: url, day, and time
# in the future, I will add a screen record feature to this

import webbrowser
import schedule
import time
# import screenrecord

def start_zoom():
  webbrowser.get().open_new(url)
  # screenrecord.record()

url = input('Enter your full Zoom room url: \n')
when_days = input('Which day of the week would you like to open this link? Enter Monday-Sunday entries only: \n')
when_hour = str(input("What time do you want to launch this link? Enter with 24 hour time (eg. 16:35): \n"))
schedule_made =   f"Schedule made! I'll open up {url} on {when_days} at {when_hour} every week. \n"


if when_days.lower() == "monday":
  schedule.every().monday.at(when_hour).do(start_zoom)
  print(schedule_made)
elif when_days.lower() == "tuesday":
  schedule.every().tuesday.at(when_hour).do(start_zoom)
  print(schedule_made)
elif when_days.lower() == "wednesday":
  schedule.every().wednesday.at(when_hour).do(start_zoom)
  print(schedule_made)
elif when_days.lower() == "thursday":
  schedule.every().thursday.at(when_hour).do(start_zoom)
  print(schedule_made)
elif when_days.lower() == "friday":
  schedule.every().friday.at(when_hour).do(start_zoom)
  print(schedule_made)
elif when_days.lower() == "saturday":
  schedule.every().saturday.at(when_hour).do(start_zoom)
  print(schedule_made)
elif when_days.lower() == "sunday":
  schedule.every().sunday.at(when_hour).do(start_zoom)
  print(schedule_made)

while True:
  schedule.run_pending()
  time.sleep(1)
