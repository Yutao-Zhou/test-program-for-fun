import os.path
import smtplib
from email.mime.text import MIMEText
import datetime
from datetime import date

def closeDays():
    closeDays_Dict = dict()
    # find wed and fri closest to today
    today = date.today()
    today_weekday = today.weekday() 
    #
    if today_weekday <= 3:
        closest_wed = date.today() + datetime.timedelta(days=3-today_weekday-1)
    else:
        closest_wed = date.today() + datetime.timedelta(days=6-today_weekday+3)
    closeDays_Dict[closest_wed] = 'Wednesday'
    closest_wed2 = closest_wed + datetime.timedelta(days=7)
    closeDays_Dict[closest_wed2] = 'Wednesday'

    if today_weekday <= 5:
        closest_fri = date.today() + datetime.timedelta(days=5-today_weekday-1)
    else:
        closest_fri = date.today() + datetime.timedelta(days=6-today_weekday+5)
    closeDays_Dict[closest_fri] = 'Friday'
    closest_fri2 = closest_fri + datetime.timedelta(days=7)
    closeDays_Dict[closest_fri2] = 'Friday'

    return today, sorted(closeDays_Dict.items())
while 1:
    name = input("What is the student's name?\n")
    time = input("What time to schedule?\n1. 1:00-1:30 \n2. 1:30-2:00\n")
    today, available_days = closeDays()
    dateweek = input(f'When is the date? \n(Today is {today})\n'+''.join([f"{i+1}. {dateweek[0]} ({dateweek[1]})\n" for i, dateweek in enumerate(available_days)]))
    date, day = available_days[int(dateweek)-1]
    if time == "1":
        time = "1:00-1:30"
    if time == "2":
        time = "1:30-2:00"
    # hours = input("when to send email:\n")
    hours = datetime.datetime.now().hour
    if 5 <= hours <= 11:
        hour = "morning"
    if 12 <= hours <= 16:
        hour = "afternoon"
    if 17 <= hours <= 20:
        hour = "evening"
    if 21 <= hours <= 4:
        hour = "night"
    msg = MIMEText('''Hello, %s: <br> <br> Good %s! <br> <br> I am writing to confirm the academic advising appointment scheduled at <span style="font-weight:bold">%s pm on %s (%s)</span>. \
    Unfortunately, due to the COVID-19, we cannot meet in person. So, all of the appointments will be <span style="font-weight:bold">by phone. I will call you\
     at the scheduled time.</span> <br>  <br> If you prefer a Zoom appointment, please email us at academic_advising@ltsc.ucsb.edu with the \
     appointment date & time, perm, and adviser name. <span style="font-weight:bold">I will send you the Zoom link around appointment time.</span><br> <br> If you have any questions before or after our meeting, please contact our\
      advising office through <span style="font-weight:bold">email or Qless.</span> <br>  <br> Here is a quick link to join the queue: \
      https://kiosk.na1.qless.com/kiosk/app/home/100100000100. <br>  <br> Have a great day!\
       <br> <br> Best, <br> Yutao Zhou <br> Peer Advisor, College of Letters and Science <br> University of California, Santa Barbara'''\
       % (name, hour, time, day, date), "html")
    msg['Content-type'] = 'text/html'
    msg['Subject'] = "Academic Advising Appointment Confirmed"
    email_address = input("What is the student's email address?\n")
    if email_address == "baby":
        email_address = "lingcai@ucsb.edu"
    if email_address == "test":
        email_address = "yutaozhou@ucsb.edu"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("yutaozhou@ucsb.edu", "password")
    # message = 'Subject: {} \n\n{}'.format("Academic Advising Appointment Confirmed", email)
    s.sendmail("yutaozhou@ucsb.edu", email_address, msg.as_string())
    s.quit()
    print(msg)
    print("Email Sended!")
    save = input("Want to save a copy? (y/n) \n")
    if save == "y":
        save_path = 'C:/Users/13520/Desktop'
        name_of_file = input("What is the name of the file: \n")
        completeName = os.path.join(save_path, name_of_file+".txt") 
        file1 = open(completeName, "w+")
        file1.write(msg)
        file1.close()
    e = input("Want to send another email? (y/n) \n")
    if e == "n":
        break