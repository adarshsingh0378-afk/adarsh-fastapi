from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from .config import settings

# 1. Connection URL
# Fixed codegit push origin main
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.database_username}:{settings.database_password}@"
    f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)

# 2. Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Define Base (This is what models.py imports)
Base = declarative_base()

# 5. Dependency for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
#while True:
 #   try:
  #      conn = psycopg2.connect(
  #          host='localhost', 
   #         database='fastapi', 
    #        user='postgres', 
     #       password='', 
      #      cursor_factory=RealDictCursor
       # )
        #cursor = conn.cursor()
        #print("Database connection was succesfull!")
        #break
    #except Exception as error:
     #   print("Connecting to database failed")
      #  print("Error: ", error)
       # time.sleep(2)  