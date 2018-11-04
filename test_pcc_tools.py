import csv
import os
root_dir = os.path.dirname(__file__)

def user_lst_from_roster_csv(csv_file):
    username_lst = []
    with open(csv_file, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            for entry in row:
                if '@' in entry:
                    username = entry.split('@')[0]
                    username_lst.append(username)
    return username_lst


def user_lst_from_email_roster(txt_file):
    '''
    takes a roster.txt with

    peter.marchineo@pcc.edu
    even.baker@pcc.edu
    nelly.manning@pcc.edu
    jess.rod2@pcc.edu

    and returns a list with

    ['peter.marchineo', 'even.baker','nelly.manning','jess.rod2']

    '''
    with open(txt_file, 'r') as f:
        return [x.split('@')[0] for x in f.readlines()]

whitelist = set()
extra_users = ['peter.marchineo','faculty.name1','faculty.name2','test.student2']

for f in os.listdir(root_dir):
    if f.endswith('roster.csv'):
        user_list = user_lst_from_roster_csv(os.path.join(root_dir, f))
    if f.endswith('roster.txt'):
        user_list = user_lst_from_email_roster(os.path.join(root_dir, f))

if user_list:
    for user in user_list:
        whitelist.add(user)

if extra_users:
    for extra_user in extra_users:
        whitelist.add(extra_user)

for x in whitelist:
    print(x)