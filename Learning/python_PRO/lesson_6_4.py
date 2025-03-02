import csv
import pickle
import sys
from collections import namedtuple
from datetime import datetime


with open('meetings.csv', encoding='utf-8') as csv_f:
    fieldnames, *friends = csv.reader(csv_f)

Friends = namedtuple('Friends', fieldnames[:~0])

for friend in sorted([Friends(surname, name, datetime.strptime(''.join(meeting_date), '%d.%m.%Y%H:%M'))
                  for surname, name, *meeting_date in friends], key=lambda x: x[~0]):
    print(f"{friend.surname} {friend.name}")

sys.exit(999)
User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

for user in sorted(users, key=lambda x: (['Gold', 'Silver', 'Bronze', 'Basic'].index(x.plan), x.email)):
    print(f"{user.name} {user.surname}")
    print(f"  Email: {user.email}")
    print(f"  Plan: {user.plan}")
    print()


sys.exit(999)
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', 'rb') as pkl_f:
    for animal in pickle.load(pkl_f):
        for key, value in zip(Animal._fields, Animal(*animal)):
            print(f"{key}: {value}")
        print()

