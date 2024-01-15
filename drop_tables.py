import pandas as pd
from sqlalchemy import create_engine, MetaData
from sshtunnel import SSHTunnelForwarder
from config1 import *


# Function to drop tables from the xo machine, so we can recreate them correctly
def drop_tables():


    # Connect to MYSQL database
    engine = create_engine(XOpath)

    # Create a MetaData object
    metadata = MetaData()

    # Reflect the existing tables
    metadata.reflect(bind=engine)

    # Drop all tables
    metadata.drop_all(bind=engine)


# function is executed only when the script is run directly, not when it is imported as a module.
if __name__ == "__main__":
    drop_tables()