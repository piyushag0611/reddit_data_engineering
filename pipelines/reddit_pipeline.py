import pandas as pd
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts, transform_data, load_data_to_csv

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day', limit=None):

    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    posts = extract_posts(instance, subreddit, time_filter, limit)
    posts_df = pd.DataFrame(posts)
    posts_df = transform_data(posts_df)
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(posts_df, file_path)

    return file_path

