# Connect4Game_Web

Juego "Conecta 4" realizado utilizando JavaScript y Python, con Flask como framework para disponer un servidor en la web.
El juego implementa la lógica algorítmica Min-Max para juegos de dos jugadores, utilizando también el algoritmo de poda Alpha-Beta.

Distribución archivos:

-app.py: dispone el servidor web. Tiene el método "makeplay" que hace referencia al archivo "connect4.py" y ejecuta la IA.
-connect4.py: contiene las classes Node, NodeConnectFour y Tree, en conjunto con múltiples métodos, para realizar la búsqueda de la mejor jugada.


Instrucciones para el uso del juego:

-Como requisito debemos tener instalado Python, prefriblemente la última versión estable.\
-Luego, clonamos el repositorio para adquirir el código.\
-Abrimos una terminal para instalar:\
     Flask: Framework necesario para la implementación web. Permite disponer un servidor escrito en Python.\
     jyserver: Librería necesaria para la integración con código js, html.\
-Ejecutamos en la terminal los comandos: \
     pip install Flask\
     pip install jyserver\
-Ejecutamos el archivo 'app.py' \
-Nos dirigimos al puerto indicado en la terminal, que por defecto es: http://127.0.0.1:8000 \
-Jugamos!


Relizado por:

Simón Echeverri\
Kevin Viera\
Camilo Zapata

