import psycopg2
from conf import host, user, password, db_name


class Database:
    """This is for accessing Postgresql and creating table with saving the binary wav data"""

    @classmethod
    def convert_To_Binary(cls, filename):
        with open(filename, 'rb') as file:
            data = file.read()
        return data
    

    @classmethod
    def insert_BLOB(cls, S_No, FileName):
        conn = None
        try:

            conn = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
    
            cur = conn.cursor()
    
            file_data = cls.convert_To_Binary(FileName)
    
            BLOB = psycopg2.Binary(file_data)

            cur.execute(
                """CREATE TABLE IF NOT EXISTS blob_datastore(
                    id serial PRIMARY KEY,
                    file_name varchar(50) NOT NULL,
                    blob_data bytea
                );
                """
            )

            cur.execute(
                "INSERT INTO blob_datastore(id, file_name, blob_data)\
                VALUES(%s,%s,%s)", (S_No, FileName, BLOB))
    
            cur.close()

            print("[INFO] Table is succesfully fulfilled")
    
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.commit()
  
  