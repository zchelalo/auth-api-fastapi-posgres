from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Text

class Movie(Base):
  __tablename__ = "movies"

  id = Column(Integer, primary_key=True)
  title = Column(String(100))
  overview = Column(Text)
  year = Column(Integer)
  rating = Column(Float)
  category = Column(String(100))