import sqlalchemy
import databases
from sqlalchemy.sql.schema import MetaData
from databases.core import Database

class Conexion():
    def __init__(self) -> None:
    
        self.__DATABASE_URL = 'postgres://danzbsvvdhcxje:0257312b7f40189ee62b0b3541a480ef83b79b09bb01af5baa175c75a98ab9b9@ec2-184-73-198-174.compute-1.amazonaws.com:5432/dcbgjll9h0dq18'
        self.__database = databases.Database(self.__DATABASE_URL)
        self.__metadata = sqlalchemy.MetaData()
        self.__engine = sqlalchemy.create_engine(self.__DATABASE_URL)

    def createTables(self) -> None:
        self.__metadata.create_all(self.__engine)
    
    def getDataBase(self) -> Database:
        return self.__database
    
    def getMetaData(self) -> MetaData:
        return self.__metadata
