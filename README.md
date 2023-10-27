# auth-api-fastapi-posgres
API de películas con autenticación de usuario desarrollada con FastAPI y PostgreSQL.  
  
## **Instalación:**  
Para probar la API debe tener instalado docker, una vez con eso listo clone el proyecto:  
```bash  
git clone https://github.com/zchelalo/auth-api-fastapi-posgres.git
```  
  
Antes de continuar debe tener en cuenta que el nombre de la base de datos, la contraseña y el host vienen predefinidos en el archivo "docker-compose.yml", si quiere hacer algún cambio deberá hacerlo en ese archivo.  
  
A continuación puede cambiar la JWT_KEY del archivo ".env.example" por una más segura, esta se utiliza para la autenticación de los usuarios.  
  
Seguido de esto solo cambie el nombre del archivo ".env.example" quitandole el ".example".  
  
Despues de ello asegurese de estar dentro de la carpeta del proyecto y ejecute el siguiente comando:  
```bash  
docker compose up
```  
  
Es posible que según la versión de docker que tenga o donde lo tenga, tendrá que ejecutar el siguiente comando en lugar del anterior:  
```bash  
docker-compose up
``` 
  
Despues de que se haya hecho la build y esten en ejecución los tres servicios, es momento de probar la API en la URL [http://localhost:8000/](http://localhost:8000/) en la cual esta alojado el servidor.
  
## **Documentación:**  
Para poder ver la documentación a la vez que probar la API REST nos podremos dirigir a [http://localhost:8000/docs](http://localhost:8000/docs) una vez que nuestro servidor este activo.  
  
En esta ruta se podrán ver todos los endpoints de la API y podremos probar cada uno de ellos desde ahí mismo, siendo esto muy útil a la hora de testear.  
  
Se utiliza Swagger para documentar la API, de esta forma se ordenan los endpoints en bloques a la misma vez que se documenta su utilidad y funcionamiento.  
  
Para poner en funcionamiento el sistema necesita hacer lo siguiente:  
1. Primeramente creará un usuario en su correspondiente endpoint, este no necesitará de autenticación la primera vez.  
2. Después se dirigirá al endpoint de auth, en el cual ingresará sus credenciales (email, password), y si todo salio bien le devolverá un token.
3. Copiará el token recibido y dará click en el boton de authorize (tambien puede hacerlo dando click en los candaditos que hay en cada endpoint).  
  
![Muestra del botón](/img/img-auth.png)  
  
4. Seguido de esto ingresará el token copiado en el campo que se muestra a continuación:  
  
![Muestra autenticación](/img/img-auth-2.png)  
  
5. Con esto hecho solo de click en "Authorize" y podrá probar la aplicación. Tome en cuenta que este proceso tendrá que repetirlo cada que recargue la página.