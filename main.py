import pandas as pd
import sqlalchemy as sa
from sqlalchemy import Table, Column, String, Numeric, Date


class DataLoader():

    def __init__(self, filepath:str) -> None:
        """
        Loads a CSV file path into a Dataframe

        Args:
            filepath (str): file path to the CSV file
        """
        df = pd.read_csv(filepath, header=0)

        self.df = df

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
        # add multiple column names together with a "-" to create unique columns
        df[index_name] = df[column_names].apply(lambda row: "-".join(row.values.astype(str)), axis=1)
        
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
        df = self.df
        # write to sql taking db table name as the name, db_engine as the engine if this already exists append it to existing table
        # write 2000 rows at a time.
        df.to_sql(db_table_name, con=db_engine, if_exists="append", chunksize=2000)
        self.df = self

    def merge_tables(self, dataframe, left_on, right_on, join_cols, how='left'):
        """
        Merge DataFrames on specific columns with multiple csvs, limited to an output of 20
        """
        df = self.df
        df = pd.merge(left= self.df, right=dataframe[join_cols], left_on=left_on, right_on=right_on, how=how)
        self.df = df.head(20)
        
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
    engine = sa.create_engine(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}", future=True) 
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
    # 
    albums_table = Table("albums",
        meta,
        Column("artist_id", String(256), primary_key=True),
        Column("album_type", String(256)),
        Column("available_markets", String(1024)),
        Column("external_urls", String(512)),
        Column("href", String(256)),
        Column("id", String(256)),
        Column("images", String(1024)),
        Column("name", String(1024)),
        Column("release_date", Date),
        Column("release_date_precision", String(128)),
        Column("total_tracks", Numeric),
        Column("track_id", String(256)),
        Column("track_name_prev", String(256)),
        Column("uri", String(256)),
        Column("type", String(256))
    )
    artists_table = Table("artists",
        meta,
        Column("id", String(256), primary_key=True),
        Column("artist_popularity", Numeric),
        Column("followers", Numeric),
        Column("genres", String(1024)),
        Column("name", String(256)),
        Column("track_id", String(128)),
        Column("track_name_prev", String(128)),
        Column("type", String(128)),
        )
    # your code to drop and create tables go here
    if drop_first:
        meta.drop_all()
    
    meta.create_all(checkfirst=True)


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
    artist_filepath = "./data/spotify_artists.csv"
    album_filepath = "./data/spotify_albums.csv"
    # instance data loader for both csv"s
    artist_data = DataLoader(artist_filepath)
    album_data = DataLoader(album_filepath)
    # print head of both
    artist_data.head()
    album_data.head()
    # set index of both data sets
    artist_data.add_index("artist_index", ["id"])
    album_data.add_index("albums_index", ["artist_id","id","release_date"])
    # sort artist by name
    artist_data.sort("name")
    # create db engine
    engine = db_engine(db_host="127.0.0.1", db_user="root", db_pass="mysql", db_name="spotify")
    # create db metadata table/columns
    db_create_tables(engine)
    # load both in db
    artist_data.load_to_db(engine, "artists")
    album_data.load_to_db(engine, "albums")

if __name__ == "__main__":
    main()