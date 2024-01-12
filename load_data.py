import pandas as pd
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from config import *


ssh_tunnel = SSHTunnelForwarder(
        (ssh_host, port),  # replace with your SSH server details
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=('localhost', 3306)  # replace with your MySQL server details
    )

ssh_tunnel.start()


# This function handles the loading of movie data into the database.
def load_movies_data():
    # Read the CSV
    movies_df = pd.read_csv('notebooks/DB_models/DB_genres.csv')

    # # Add a 'year' column if not present in CSV
    # if 'year' not in movies_df.columns:
    #     movies_df['year'] = None

    # Connect to MYSQL database
    # pymysql: Specifies the MySQL driver to be used for the connection.
    # pymysql is a Python library that provides a MySQL driver for Python.
    engine = create_engine(
        f"mysql+pymysql://{db_username}:{db_password}@localhost:{ssh_tunnel.local_bind_port}/{db_name}")

    # Insert data into the 'movies' table
    # to_sql method to insert the data from the Pandas DataFrame into the 'movies' table in the MySQL database.
    movies_df.to_sql('movie_genre', con=engine, if_exists='append', index=False)

    ssh_tunnel.close()


# function is executed only when the script is run directly, not when it is imported as a module.
if __name__ == "__main__":
    load_movies_data()