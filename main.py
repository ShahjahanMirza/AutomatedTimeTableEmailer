import pandas as pd
import datetime as dt
import smtplib
import os
import random
from dotenv import load_dotenv

load_dotenv()
my_email = '03318325446sm@gmail.com'
my_pass = os.getenv('gmail_pass_key')

df = pd.read_csv('Exam timetable.csv')

now = dt.datetime.now()
cur_year = now.year
cur_month = now.month
cur_day = now.day

for subject,weekday,day,month,year,type in df.values:
    if (month == cur_month) & (day == cur_day): 
        
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,
                            password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f'Subject: {type.title()} {subject.title()}! \n\n{type} {subject}\nDate:{weekday}-{day}-{month}')

        print('Sent email!')