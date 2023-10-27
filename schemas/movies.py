from pydantic import BaseModel, Field, constr, confloat, conint
from typing import Optional
import datetime

class Movie(BaseModel):
  id: Optional[int] = None
  title: str = Field(min_length=1, max_length=100)
  overview: Optional[str] = None
  year: conint(le=datetime.date.today().year)
  rating: float = Field(ge=1, le=10)
  category: str = Field(min_length=1, max_length=100)

  model_config = {
    "json_schema_extra" : {
      "example": {
          "title": "Mi Pelicula",
          "overview": "Descripcion de la pelicula",
          "year": 2023,
          "rating": 9.0,
          "category": "Anime"
      }
    }
  }

class MovieUpdate(BaseModel):
  title: Optional[constr(min_length=1, max_length=100)] = None
  overview: Optional[str] = None
  year: Optional[conint(le=datetime.date.today().year)] = None
  rating: Optional[confloat(ge=1, le=10)] = None
  category: Optional[constr(min_length=1, max_length=100)] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
          "title": "Mi Pelicula",
          "overview": "Descripcion de la pelicula",
          "year": 2023,
          "rating": 9.0,
          "category": "Anime"
      }
    }
  }