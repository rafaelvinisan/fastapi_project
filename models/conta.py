from settings.database import Base
from sqlalchemy import Column, Numeric, String, Integer
class Conta(Base):
    __tablename__ = "Conta"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    value = Column(Numeric)
    type = Column(String(30))
    