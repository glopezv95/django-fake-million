import os
import django
from pathlib import Path
import pandas as pd
from multiprocessing import Pool, cpu_count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Client

def load_data():

    BACKEND_DIR = Path(__file__).parent
    DATA_FILE_DIR = BACKEND_DIR / 'data' / 'data.csv'

    df = pd.read_csv(DATA_FILE_DIR, index_col = 0)
    
    client_data = df.to_dict(orient = 'records')
    Client.objects.bulk_create([Client(**data) for data in client_data])

if __name__ == '__main__':

    num_processes = cpu_count() - 1
    
    with Pool(processes=num_processes) as pool:
        pool.map(load_data, [])