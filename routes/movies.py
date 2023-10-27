from fastapi import APIRouter, Response, status, HTTPException, Depends, Query
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base
from services.movies import MovieService
from schemas.movies import Movie as MovieSchema

movie_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@movie_router.get(
    path='/movies', 
    tags=['movies'], 
    status_code=status.HTTP_200_OK,
    response_model=List[MovieSchema],
    dependencies=[Depends(JWTBearer())]
  )
def get_movies() -> List[MovieSchema]:
  db = Session()
  result = MovieService(db).get_movies()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron películas'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@movie_router.get(
    path='/movies/{id}', 
    tags=['movies'], 
    status_code=status.HTTP_200_OK,
    response_model=MovieSchema,
    dependencies=[Depends(JWTBearer())]
  )
def get_movie(id: int) -> MovieSchema:
  db = Session()
  result = MovieService(db).get_movie(id)
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la película'})
  return result

############################################################################
# Obtener varios registros según los criterios de busqueda (categoría y año)
############################################################################
@movie_router.get(
    path='/movies/', 
    tags=['movies'], 
    status_code=status.HTTP_200_OK,
    response_model=List[MovieSchema],
    dependencies=[Depends(JWTBearer())]
  )
def get_movies_by(category: str = Query(None, description="Filtrar por categoría"), year: int = Query(None, description="Filtrar por año")) -> List[MovieSchema]:
  if category is None and year is None:
    raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail={'message': 'Debes proporcionar al menos un parámetro de búsqueda'})
  
  db = Session()
  result = MovieService(db).get_movies_by(category=category, year=year)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la película'})
  return result

############################################################################
# Insertar un registro
############################################################################
@movie_router.post(
    path='/movies', 
    tags=['movies'], 
    status_code=status.HTTP_200_OK,
    response_model=MovieSchema,
    dependencies=[Depends(JWTBearer())]
  )
def create_movie(movie: MovieSchema) -> MovieSchema:
  db = Session()
  new_movie = MovieService(db).create_movie(movie)
  return new_movie

############################################################################
# Actualizar un registro
############################################################################
@movie_router.put(
    path='/movies/{id}', 
    tags=['movies'], 
    status_code=status.HTTP_200_OK,
    response_model=MovieSchema,
    dependencies=[Depends(JWTBearer())]
  )
def update_movie(id: int, movie_update: MovieSchema) -> MovieSchema:
  db = Session()
  movie = MovieService(db).get_movie(id)
  if not movie:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la película'})
  
  result = MovieService(db).update_movie(movie, movie_update)

  return result

############################################################################
# Borrar un registro
############################################################################
@movie_router.delete(
    path='/movies/{id}', 
    tags=['movies'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(JWTBearer())]
  )
def delete_movie(id: int):
  db = Session()
  movie = MovieService(db).get_movie(id)
  if not movie:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró la película'})
  
  MovieService(db).delete_movie(movie)

  return Response(status_code=HTTP_204_NO_CONTENT)