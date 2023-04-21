'''
-> = 'follows'
Danielle -> Amanda, Katherine
Katherine -> Samantha
Samantha -> Dana, Danielle
Dana -> Danielle, Amanda
Amanda -> Danielle
'''

graph = {
    'Danielle':['Amanda', 'Katherine'],
    'Katherine':['Samantha'],
    'Samantha':['Dana', 'Danielle'],
    'Dana':[],
    'Amanda':['Danielle']
}