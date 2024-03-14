import time

from analysis.generate import pool_df, clean_df

if __name__ == '__main__':
    
    length = int(input('Length of DataFrame: '))
    start_time = time.time()
    df = pool_df(length = length)
    df_cleaned = clean_df(df)
    
    end_time = time.time()
    elapsed_time_s = end_time - start_time
    elapsed_time_min = round(elapsed_time_s / 60, 2)
    
    print(f'Proccess completed.')
    print(f'Length of the DataFrame generated: {len(df)}')
    print(f'Elapsed time: {round(elapsed_time_s, 2)} s ({elapsed_time_min} min)')