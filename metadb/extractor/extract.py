import sqlalchemy as db

def extract_metadata(databse_connection_string):
    engine = db.create_engine(databse_connection_string)
    connection = engine.connect()
    metadata = db.MetaData()
    metadata.reflect(engine)
    
    for table in metadata.tables.values():
        print("table :" + table.name)

        for column in table.columns:
            print("column: " +column.name)
    return metadata.tables.values()
