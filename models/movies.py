from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Text

class Movie(Base):
  __tablename__ = "movies"

  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  overview = Column(Text)
  year = Column(Integer)
  rating = Column(Float, nullable=False)
  category = Column(String(100), nullable=False)