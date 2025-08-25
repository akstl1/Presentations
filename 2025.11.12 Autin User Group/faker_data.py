from faker import Faker
from random import randint
import pandas as pd
import numpy as np     

fake = Faker() 

def input_data(x): 
    client_df = pd.DataFrame({
        'Client Name':[],
        'Client Address':[],
        'Client Email':[],
        'Client Region':[],
        'Client Status':[]
    })

    student_data ={} 
    for i in range(0, x): 
        student_data[i]={} 
        student_data[i]['id']= randint(1, 100) 
        student_data[i]['name']= fake.name() 
        student_data[i]['address']= fake.address() 
        student_data[i]['latitude']= str(fake.latitude()) 
        student_data[i]['longitude']= str(fake.longitude()) 
    print(student_data) 

def main(): 

    # Enter number of students 
    # For the above task make this 100 
    number_of_students = 10 
    input_data(number_of_students) 
main() 
# The folder or location where this python code 
# is save there a students.json will be created 
# having 10 students data. 