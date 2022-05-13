import pandas as pd
import sqlalchemy as sa
from sqlalchemy import Column, String, Numeric


class DataLoader():

    def __init__(self, filepath:str) -> None:
        """
        Loads a CSV file path into a Dataframe

        Args:
            filepath (str): file path to the CSV file
        """
        df = pd.read_csv(filepath, header=0)

        self.df = df
        pass

    def head(self) -> None:
        """
        prints the head of the dataframe to console
        """
        print(self.df.head())

    def add_index(self, index_name:str, column_names:list) -> None:
        """
        Create a dataframe index column from concatenating a series of column values. Column values are concatenated by a dash "-".

        For example if you have three columns such as: artist="Metallica", song="Ride the Lighting"
        the index would be ""Metallica-Ride the Lighting"

        Args:
            index_name (str): the index column name
            colum_names (list): list of columns to concatenate into an index column
        """
        df = self.df
        # add multiple column names together with a '-' to create unique columns
        df[index_name] = df[column_names].apply(lambda row: '-'.join(row.values.astype(str)), axis=1)
        # use unique column to set as index
        df.set_index(index_name, inplace=True)
        self.df = df
        

    def sort(self, column_name:str) -> None:
        """
        Sorts the dataframe by a particular column

        Args:
            column_name (str): column name to sort by
        """
        df = self.df
        # Sort dataframe by inputted column_name
        df.sort_values(column_name)
        self.df = df

    def load_to_db(self, db_engine, db_table_name:str) -> None:
        """
        Loads the dataframe into a database table.

        Args:
            db_engine (SqlAlchemy Engine): SqlAlchemy engine (or connection) to use to insert into database
            db_table_name (str): name of database table to insert to
        """



def db_engine(db_host:str, db_user:str, db_pass:str, db_name:str="spotify") -> sa.engine.Engine:
    """Using SqlAlchemy, create a database engine and return it

    Args:
        db_host (str): datbase host and port settings
        db_user (str): database user
        db_pass (str): database password
        db_name (str): database name, defaults to "spotify"

    Returns:
        sa.engine.Engine: sqlalchemy engine
    """
    engine = sa.create_engine(f'mysql+pymsql://{db_user}:{db_pass}@{db_host}/{db_name}', future=True) 
    return engine


def db_create_tables(db_engine, drop_first:bool = False) -> None:
    """
    Using SqlAlchemy Metadata class create two spotify tables (including their schema columns and types)
    for **artists** and **albums**.


    Args:
        db_engine (SqlAlchemy Engine): SqlAlchemy engine to bind the metadata to.
        drop_first (bool): Drop the tables before creating them again first. Default to False
    """
    meta = sa.MetaData(bind=db_engine)

    # your code to define tables go in here
    #   - Be careful, some of the columns like album.available_markets are very long. Make sure you give enough DB length for these. ie: 10240 (10kb)
    # ,href,id,images,name,release_date,release_date_precision,total_tracks,track_id,track_name_prev,uri,type
    albums_table = sa.Table('albums',
        meta,
        Column('album_type', String(256), primary_key=True),
        Column('artist_id', String(256)),
        Column('available_markets', String(1024)),
        Column('external_urls', String(512)),
        Column('href', String(256)),
        Column('id', ),
        Column('images', ),
        Column('name', ),
        Column('release_date', ),
        Column('release_date_precision', ),
        Column('total_tracks', Numeric),
        Column('track_id', String(256)),
        Column('track_name_prev', String(256)),
        Column('uri', String(256)),
        Column('type', String(256))
    )

    # Column('', ),
    # your code to drop and create tables go here


def main():
    """
    Pipeline Orchestratation method.

    Performs the following:
    - Creates a DataLoader instance for artists and albums
    - prints the head for both instances
    - Sets artists index to id column
    - Sets albums index to artist_id, name, and release_date
    - Sorts artists by name
    - creates database engine
    - creates database metadata tables/columns
    - loads both artists and albums into database
    """
    pass


if __name__ == '__main__':
    main()