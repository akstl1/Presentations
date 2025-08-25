from faker import Faker
from random import randint
import pandas as pd
import numpy as np     

fake = Faker() 

def rgn(x):
    if x==1:
        return "North"
    elif x==2:
        return "South"
    elif x==3:
        return "East"
    else:
        return "West"

def contract_status(x):
    if x==1:
        return "Approved"
    elif x==2:
        return "In Progress"
    elif x==3:
        return "Rejected"
    else:
        return "Not Contacted"

def input_data(x): 
    client_df = pd.DataFrame({
        'Client Name':[],
        'Client Address':[],
        'Client Email':[],
        'Client Region':[],
        'Client Status':[],
        'Contract Value':[]
    })

    for i in range(x): 
        name = fake.name() 
        address = fake.address() 
        email = fake.email()
        region = rgn(randint(1,4))
        status = contract_status(randint(1,4))
        contract_val = randint(1000000, 20000000)
        new_row = pd.DataFrame({
        'Client Name':[name],
        'Client Address':[address],
        'Client Email':[email],
        'Client Region':[region],
        'Client Status':[status],
        'Contract Value':[contract_val]
        })
        client_df = pd.concat([client_df,new_row],ignore_index=True)
    client_df.to_excel('client_df.xlsx', sheet_name='Sheet1', index=False)
    

def main(): 

    # Enter number of students 
    # For the above task make this 100 
    number_of_students = 100 
    input_data(number_of_students) 
main() 
# The folder or location where this python code 
# is save there a students.json will be created 
# having 10 students data. 