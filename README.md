# auth-api-fastapi-posgres
API de películas con autenticación de usuario desarrollada con FastAPI y PostgreSQL.  
  
## **Instalación:**  
Para probar la API debe tener instalado python y postgres, una vez con eso listo clone el proyecto:  
```bash  
git clone https://github.com/zchelalo/auth-api-fastapi-posgres.git
```  
  
Despues de ello asegurese de estar dentro de la carpeta del proyecto y corra el siguiente comando:  
```bash  
pip install -r requirements.txt
```  
  
Es posible que si tiene mas de una versión de python falle y deba correr el siguiente comando en lugar del anterior:  
```bash  
pip3 install -r requirements.txt
``` 
  
Con los requerimientos instalados deberá crear una base de datos en postgres, para despues reemplazar el archivo *.env.example* con sus datos de usuario, y quitarle el *.example*. Seguido de esto deberá añadir una "JWT_KEY" la cual servirá para la autenticación de los usuarios; esta debe estar oculta y ser un string seguro. Por ultimo específique el puerto de su preferencia para que se ejecute la aplicación. Quedará un archivo parecido a esto:  
```env  
DB_NAME=moviesdb
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

JWT_KEY="secret_key_example"

PORT=8000
``` 
  
Una vez hecho esto deberá ejecutar el siguiente comando para que se ejecute la aplicación y a su vez el servidor:  
```bash  
python main.py
``` 
  
En su defecto si tienes problemas o tienes mas versiones de python instaladas, usa:  
```bash  
python3 main.py
``` 
  
Con esto basta con probar la aplicación dirigiendose a cada endpoint con la URL *http://localhost:8000/* en la cual esta alojado el servidor.  
  
## **Documentación:**  
Para poder ver la documentación a la vez que probar la API REST nos podremos dirigir a *http://localhost:8000/docs* una vez que nuestro servidor este activo.  
  
En esta ruta se podrán ver todos los endpoints de la API y podremos probar cada uno de ellos desde ahí mismo, siendo esto muy útil a la hora de testear.  
  
Se utiliza Swagger para documentar la API, de esta forma se ordenan los endpoints en bloques a la misma vez que se documenta su utilidad y funcionamiento.