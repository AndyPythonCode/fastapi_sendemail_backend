import sqlalchemy
import databases
from sqlalchemy.sql.schema import MetaData
from databases.core import Database
from decouple import config

class Conexion():
    def __init__(self) -> None:
    
        self.__DATABASE_URL = config('DATABASE_URL')
        self.__database = databases.Database(self.__DATABASE_URL)
        self.__metadata = sqlalchemy.MetaData()
        self.__engine = sqlalchemy.create_engine(self.__DATABASE_URL)

    def createTables(self) -> None:
        self.__metadata.create_all(self.__engine)
    
    def getDataBase(self) -> Database:
        return self.__database
    
    def getMetaData(self) -> MetaData:
        return self.__metadata
