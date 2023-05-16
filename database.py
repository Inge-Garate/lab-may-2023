from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret)

with engine.connect() as connection:
  result = connection.execute(text("select * from materiales_prefabricados"))
  print(result.all())