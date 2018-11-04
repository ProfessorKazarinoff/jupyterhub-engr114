# coding: utf-8

# # Read a roster.csv file
#
# On myPCC, if you go to Faculty --> Summary Class List --> Download Roster you get a .csv file.
#
# This notebook is an attempt to write a function that takes that .csv file and outputs a list of user names.
#
# The roster file is:
#
# 34272-roster.csv


import csv

#with open('34272-roster.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print(', '.join(row))

# In[10]:


#with open('34272-roster.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    for row in spamreader:
#        for entry in row:
#           if '@' in entry:
#                print(entry)
#                username = entry.split('@')[0]
#                print(username)


# In[11]:


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


# In[12]:

#to use function above:
# from pcc_tools import user_lst_from_roster_csv
#
# user_lst_from_roster_csv('34272-roster.csv')




def user_lst_from_email_roster(txt_file):
    '''
    takes a roster.txt with

    faculty.name1@pcc.edu
    even.baker@pcc.edu
    nelly.manning@pcc.edu
    jess.rod2@pcc.edu

    and returns a list with

    ['faculty.name1', 'even.baker','nelly.manning','jess.rod2']

    '''
    with open(txt_file, 'r') as f:
        return [x.split('@')[0] for x in f.readlines()]




# to use function above
# from pcc_tools import user_lst_from_email_roster
#
# user_lst_from_email_roster('roster.txt')

