import sqlalchemy as db
from sqlalchemy.orm import Session
from sqlalchemy import select, func, text

def extract_metadata(databse_connection_string):
    engine = db.create_engine(databse_connection_string)
    connection = engine.connect()
    metadata = db.MetaData()
    metadata.reflect(engine)
    response=[]
    table_list=[]
    for table in metadata.tables.values():
        table_list.append(db.Table(table.name, metadata))


    with Session(engine) as session:
        for table in table_list:
            meta_dict={}
            meta_dict["columns"] = []
            for column in table.columns:
                column_dict={"col_name": column.name, "col_type": str(column.type)}
                meta_dict["columns"].append(column_dict)
            rows=session.scalar(select(func.count()).select_from(table))
            meta_dict["name"] = table.name
            meta_dict["num_rows"] = rows
            meta_dict["database"] = session.bind.url.database
            meta_dict["schema"] = ""
            if table.schema:
                meta_dict["schema"] = table.schema
            response.append(meta_dict)
    return response
    
