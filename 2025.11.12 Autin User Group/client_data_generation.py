from faker import Faker
from random import randint
import pandas as pd
import numpy as np     

fake = Faker() 

## set up region function to translate rand int to region
def rgn(x):
    if x==1:
        return "North"
    elif x==2:
        return "South"
    elif x==3:
        return "East"
    else:
        return "West"

## set up region function to translate rand int to client status
def contract_status(x):
    if x==1:
        return "Approved"
    elif x==2:
        return "In Progress"
    elif x==3:
        return "Rejected"
    else:
        return "Not Contacted"

## Function to get fake data, save to file
def input_data(x): 
    ## set up pandas dataframe to store data
    client_df = pd.DataFrame({
        'Client Name':[],
        'Client Address':[],
        'Client Email':[],
        'Client Region':[],
        'Client Status':[],
        'Contract Value':[]
    })

    ## for loop to get x number of clients, and for each give them the required attribute and append to df
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
    
    ## save df to file
    client_df.to_excel('client_df.xlsx', sheet_name='Sheet1', index=False)
    
## main function to run the input function with number of clients
def main(): 

    # Enter number of clients 
    number_of_clients = 100 
    input_data(number_of_clients) 
main() 