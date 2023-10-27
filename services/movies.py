from models.movies import Movie as MovieModel
from schemas.movies import Movie as MovieSchema

class MovieService():
  def __init__(self, db) -> None:
    self.db = db

  def get_movies(self):
    result = self.db.query(MovieModel).all()
    return result
  
  def get_movie(self, id):
    result = self.db.query(MovieModel).where(MovieModel.id == id).one_or_none()
    return result
  
  def get_movies_by(self, category: str = None, year: int = None):
    query = self.db.query(MovieModel)
    if category:
      # query = query.where(MovieModel.category.like(f'%{category}%'))
      query = query.where(MovieModel.category == category)
    if year:
      query = query.where(MovieModel.year == year)
    result = query.all()
    return result
  
  def create_movie(self, movie: MovieSchema):
    new_movie = MovieModel(**movie.model_dump())
    self.db.add(new_movie)
    self.db.commit()
    self.db.refresh(new_movie)
    return new_movie
  
  def update_movie(self, movie: MovieSchema, movie_update: MovieSchema):
    for field, value in movie_update.model_dump(exclude_unset=True).items():
      setattr(movie, field, value)

    self.db.commit()
    self.db.refresh(movie)
    return movie
  
  def delete_movie(self, movie):
    self.db.delete(movie)
    self.db.commit()
    return