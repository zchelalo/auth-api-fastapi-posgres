from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Utiliza las variables de entorno para configurar la conexión
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")

# Es la cadena de conexión
db_url = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'

# Representa el motor de la base de datos, con el comando "echo=True" para que al momento de realizar la base de datos, me muestre por consola lo que esta realizando
engine = create_engine(db_url, echo=False)

# Se crea session para conectarse a la base de datos, se enlaza con el comando "bind" y se iguala a engine
Session = sessionmaker(bind=engine)

# Sirve para manipular todas las tablas de la base de datos
Base = declarative_base()