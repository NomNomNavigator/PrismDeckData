import pandas as pd
from sqlalchemy import create_engine, MetaData
from sshtunnel import SSHTunnelForwarder
from config import *



def drop_tables():


    # Connect to MYSQL database
    # pymysql: Specifies the MySQL driver to be used for the connection.
    # pymysql is a Python library that provides a MySQL driver for Python.

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