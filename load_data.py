import pandas as pd
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from config1 import *


# ssh_tunnel = SSHTunnelForwarder(
#         (ssh_host, port),  # replace with your SSH server details
#         ssh_username=ssh_username,
#         ssh_password=ssh_password,
#         remote_bind_address=('localhost', 3306)  # replace with your MySQL server details
#     )

# ssh_tunnel.start()


# This function handles the loading of data into the database.
def load_movies_data():
    # Read the CSV
    df = pd.read_csv('notebooks/DB_models/DB_genres.csv')

    # Connect to MYSQL database on linux box
    # engine = create_engine(
    #   f"mysql+pymysql://{db_username}:{db_password}@localhost:{ssh_tunnel.local_bind_port}/{db_name}")

    # Connect to MYSQL database on my machine
    engine = create_engine(
        f"mysql+pymysql://{db_username}:{db_password}@localhost/{db_name}")

    # Insert data into table
    df.to_sql('genre', con=engine, if_exists='append', index=False)

    #ssh_tunnel.close()


# function is executed only when the script is run directly, not when it is imported as a module.
if __name__ == "__main__":
    load_movies_data()
