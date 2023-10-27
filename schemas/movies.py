from pydantic import BaseModel, Field
from typing import Optional
import datetime

class Movie(BaseModel):
  id: Optional[int] = None
  title: str = Field(min_length=1, max_length=100)
  overview: str = Field(default='Descripcion de la película', min_length=1)
  year: int = Field(le=datetime.date.today().year)
  rating: float = Field(ge=1, le=10)
  category: str = Field(min_length=1, max_length=100)

  model_config = {
    "json_schema_extra" : {
      "example": {
          "id": 1,
          "title": "Mi Pelicula",
          "overview": "Descripcion de la pelicula",
          "year": 2023,
          "rating": 9.0,
          "category": "Anime"
      }
    }
  }