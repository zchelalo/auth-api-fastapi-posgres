from config.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  email = Column(String(100), nullable=False, unique=True)
  password = Column(String(150), nullable=False)