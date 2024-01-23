from settings.database import Base
from sqlalchemy import Column, String, Integer
class FornecedorCliente(Base):
    __tablename__ = "fornecedor_cliente"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    