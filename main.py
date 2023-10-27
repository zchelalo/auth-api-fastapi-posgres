from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from docs import tags_metadata
from routes.movies import movie_router
from routes.home import home
from routes.users import user_router
from routes.auth import auth_router
import os
import uvicorn

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)

app = FastAPI(
	title= 'REST API de películas',
	description= 'API de películas con autenticación de usuario desarrollada con FastAPI y PostgreSQL',
	version= '0.0.1',
	openapi_tags=tags_metadata
)

app.add_middleware(ErrorHandler)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(movie_router)
app.include_router(home)