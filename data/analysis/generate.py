import pandas as pd
import numpy as np
from numpy import random
from faker import Faker
from datetime import date
from multiprocessing import Pool, cpu_count

random.seed(17)
faker = Faker()

today_year = date.today().year

def generate_salary(studies:str):
    
    match studies:
        case "primary":
            mean = 18000
        case "secondary":
            mean = 24000
        case "tertiary":
            mean = 30000
    
    distribution = random.normal(
        loc = mean,
        scale = 4000,
        size = 20000
    )
    
    return list(distribution)

def generate_df(length:int):
    
    name = [faker.first_name_male() for i in range(length//2)]
    female_name = [faker.first_name_female() for i in range(length//2)]
    name.extend(female_name)
    last_name = [faker.last_name_nonbinary() for i in range(length)]
    
    gender = ["male" for i in range(length//2)]
    gender.extend(["female" for i in range(length//2)])
    
    phone_number = [faker.phone_number() for i in range(length)]
    
    job = [faker.job() for i in range(length)]
    
    studies = random.choice(
        a = ['primary', 'secondary', 'tertiary'],
        p = [0.6, 0.3, 0.1],
        size = length,
        replace = True)
    
    country = [faker.country() for i in range(length)]
    birth_date = [faker.date_of_birth(minimum_age = 18, maximum_age = 65) for i in range(length)]
    
    df = pd.DataFrame({
        'name': name,
        'last_name': last_name,
        'gender': gender,
        'phone_number': phone_number,
        'job': job,
        'studies':studies,
        'country': country,
        'birth_date': birth_date,
    })
    
    study_dict = {
        'primary': generate_salary('primary'),
        'secondary': generate_salary('secondary'),
        'tertiary': generate_salary('tertiary'),
    }
        
    df['salary'] = df['studies'].map(lambda x: round(random.choice(study_dict[x]), 2))
    
    df['birth_date'] = pd.to_datetime(df['birth_date'])
    df['age'] = df['birth_date'].apply(lambda x: today_year - x.year)
    
    return df
    
def pool_df(length:int):
    
    num_processes = int(cpu_count()) - 1
    
    with Pool(processes = num_processes) as pool:
        
        length_map = [length // num_processes] * num_processes
        length_module = length % num_processes
        length_map[-1] += length_module
        
        results = pool.map(generate_df, length_map)
        
    df = pd.concat(results, ignore_index = True)
    
    return df

def clean_df(df:pd.DataFrame):
    
    for character in ['.', 'x', '(', ')', '-', '+']:
        df['phone_number'] = df['phone_number'].str.replace(character, '')

    df['phone_check'] = df['phone_number']

    for number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        df['phone_check'] = df['phone_check'].str.replace(number, '')
        
    phone_check_clean = True if len(df[df['phone_check'] != '']) == 0 else False
    df = df.drop('phone_check', axis = 1) if phone_check_clean else None

    df['phone_number'] = df['phone_number'].astype(np.int64)


    return df.to_csv(path_or_buf = 'data.csv', sep = ',')