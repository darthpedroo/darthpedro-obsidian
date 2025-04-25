---
creation date: 2025-04-25 02:44
modification date: Friday 25th April 2025 02:44:41
title: bash
---
# Cuestionario Bandit

## Pregunta 1
- ¿Qué es SSH y para qué sirve? ¿En qué se diferencia de Telnet? ¿De qué maneras lo utilizaron para conectarse al servidor de bandit? ¿Qué es PuTTY y para qué sirve?

[Como funciona SSH](https://www.youtube.com/watch?v=5JvLV2-ngCI)

### Que es SSH 
SSH es un protocolo de red que permite acceder de manera segura a una computadora a través de una red **insegura** (internet)

SSH se creó para reemplazar los sistemas de login inseguros como **Telnet**.

El problema de Telnet es que los paquetes se envían **públicamente** con las claves. (Se envía usuario y contraseña x el internet)

SSH encripta los datos del mensaje. 
El problema es que un atacante puede **ver** que está encriptado esto pero pueden hacer poco con esta información.

El paquete SSH contiene:

* Packet Length: Te dice el tamaño del paquete
* Padding Amount: Cuánto padding se va a usar.
* Payload: La data real que necesitas
* Padding: Random bytes que se combinan con el payload para complicar el sniffing de paquetes
* Message Authentication Code: Mensaje que verifica que la data no se haya modificiado. 

Cuando esta encriptado solo se ve el Packet Length y el Message Authentication Code. 

### Conectarse al server de bandit
Para conectarse al server de bandit me loguee con el commando **ssh**, especificando la url de bandit, el puerto y el usuario. Luego te pedía una contraseña y podías acceder al server.

### Putty
[Reel sobre putty](https://www.instagram.com/aprendiendo.con.personajes/)
https://www.lenovo.com/in/en/glossary/putty/

Putty es un emulador de terminal que permite conectarse a dispositivos o computadoras remotas mediante varios protocolos (SSH, Telnet, etc)

La principal ventaja de putty es que tiene una interfaz más amigable para conectarse en vez de estar haciendo todas las conexiones con comandos desde la consola. Se pueden guardar configuraciones y automatizar tareas con putty.

## Pregunta 2
- De cinco ejemplos de comandos que se utilicen para navegar/manipular el filesystem, cada uno con por lo menos dos opciones que modifiquen el comportamiento por defecto del comando.

### rm
Borra referencias a objetos del filesystem. Por defecto no borra directorios.

```bash
rm text.txt
```
-> Borra el archivo

**Parametros extra:**
* -r : Recursivo. Borra recursivamente las carpetas y los archivos que haya dentro de estas.
* -f : Force: No pide confirmación para borrar un archivo

```bash
rm -rf directory 
```

-> Borra el directorio y todo lo q haya adentro.

### ls
Lista archivos y directorios.

**Parametros extra**:

* -l : Muestra los detalles de cada archivo/directorio. Los permisos, el tamaño, propietario, etc.
* -a Muestra archivos ocultos.

El comando **ls -la** es el alias del comando **ll**

### mkdir
Permite crear directorios.

**Parametros extra:**
* -p: Permite crear directorios anidados sin que tiren error.

```bash
mkdir test/test1/test2
```

Si no existe test tira el error "no such file or directory"

```bash
mkdir -p test/test1/test2
```

Crea el directorio anidado sin tirar error.

* -m Especifica permisos al crear el directorio

```bash
mkdir -m 755 test
```

### mv

Mueve archivos

**Parametros especiales:**

* -i: Si se va a sobreescribir un archivo, pide confirmación antes de hacerlo.

```bash
mv -i test test2
```

Si ya existe test en test2, muestra el mensaje: 

```bash
mv: overwrite 'test2/test'?
```

* -n: No sobreescribe archivos existentes.


```bash
mv -i test test2
```

Si ya existe test en test2, muestra el mensaje:

```bash
mv: not replacing 'test2/test'
```

### chown
Cambia el propietario y/o el grupo de un archivo o directorio. **chown = change ownership**

**Parametros adicionaes:**

* -R: Cambia el propietario de forma recusriva en los directorios

```bash
chown -R porky:porky test
```

* --from : Cambia si pertenece a un usuario especifico.
```bash
sudo chown --from=porky root:root test
```

Cambia de porky a root. Lo hace de manera recursiva.

## Pregunta 3
https://www.reddit.com/r/bash/comments/1dmfkes/learning_file_permissions_what_is_the_owner_group/
https://www.redhat.com/en/blog/linux-file-permissions-explained

- Explique brevemente los distintos niveles de usuarios (owner, group, user) y describa cómo se relacionan con el filesystem.

**Owner**: Es el propietario de un archivo o directorio. Puede cambiar los permisos de dicho archivo (lectura, escritura, etc) para él mismo , otros usuarios u otros grupos. **Generalemente el owner de un archivo no debería cambiar pero si alguien es root puede hacerlo**

**Grupo**: Se puede asociar una carpeta o un archivo con un grupo de usuarios. Estos miembros compartes ciertos permisos sobre dicha carpeta o archivo. 

**User/Other:** Se aplican estos permisos cuando el usuario que interactúa no es ni el owner ni forma parte de un grupo

## Pregunta 4
- ¿Por qué programas como gzip necesitan que el archivo a descomprimir posea en su nombre la extensión .gz explícitamente? ¿Cómo resolvieron este inconveniente a la hora de resolver el level 12 -> level 13?

https://unix.stackexchange.com/questions/709708/why-gzip-utility-cares-about-extension


Gzip usa la extensión .gz para reconocer un archivo y no tener que acceder al contenido para determinar si lo debe descomprimir o no. 
Para ponerle nombre al archivo descomprimido, gzip borra el nombre de la extensión. Sin la extensión, no se podría renombrar o debería buscar el nombre original en las propiedades del archivo, lo cuál ralentizaría el comando

Para resolver el ejercicio de bandit, había que usar el comando:

```bash
file "test"
```

Esto servía para ver que tipo de compresión tenía. Si se comprimió usando **gzip**, había que copiar el archivo a otro llamado **test2.gz** o agregarle el formato .gz al nombre del archivo.

## Pregunta 5
- Explique con sus palabras las diferencias y similitudes entre la criptografía simétrica y asimétrica. ¿Por qué es más seguro utilizar criptografía asimétrica comparado al uso de contraseñas?

**Fuentes:**
https://security.stackexchange.com/questions/9957/can-i-use-a-private-key-as-a-public-key-and-vice-versa
https://www.instagram.com/p/DHmMImEuHmn/
https://www.youtube.com/watch?v=o_g-M7UBqI8

Tanto la criptografía simétrica como la asimétrica utilizan encriptación basada en llaves, sin embargo, lo hacen de manera distinta. 

### Criptografía Simétrica:
Se utiliza la misma tanto para encriptar como para desencriptar un mensaje
![Image Description](/images/Pasted%20image%2020250324190856.png)

En este ejemplo se muestra como se encripta la palabra hello. Se usa un algoritmo que mueve las letras y se usa como clave secreta el **3**, que representa las posiciones hacia la derecha a mover cada letra. 
En este caso se encripta y desencrpita usando la misma clave secreta. 


### Criptografía asimétrica
Se utilizan distintas claves para encriptar y desencriptar

![Image Description](/images/Pasted%20image%2020250324191350.png)

Se usan dos claves, una pública y una privada. 

Este algoritmo encripta con una clave, pero requiere de la otra clave para desencriptarlo.

Por ejemplo, podemos encriptar con la clave privada pero si queremos desencriptar el mensaje, tendremos que usar la clave pública. De la misma manera, si encriptamos con la clave pública tendremos que usar la clave privada para desencriptar.

En la practica, existen dos casos:

**Firmar y encriptar**:

**Encriptar**: Se encripta con la clave pública y luego una persona desencripta con su clave privada.

**Firmar**: Una persona **encripta** con su clave privada, firmando así el mensaje. Luego, el resto de personas que tengan la clave pública pueden verificar que el mensaje fue firmado por determinada persona con su clave privada.

### Ventajas y desventajas de cada uno

#### Encriptación asimétrica
**Desventajas** :
	Es más lento el algoritmo ya que requiere claves mucho más largas
	El texto a encriptar se expande en tamaño. Hay que enviar mas bytes de información

**Ventajas** :
	Al no compartir la clave privada, la encriptación se vuelve más segura.
#### Encriptación simétrica
**Desventajas**:
	La llave privada se comparte, generando que sea menos seguro. 

**Ventajas**:
	Es más rápido el algoritmo
	El texto cifrado tiene el mismo tamaño que el texto normal

### Casos de uso
**Encriptación Asimétrica**: Se utiliza para datos más limitados y pequeños

**Encriptación simétrica**: Se utiliza para volumenes masivos de datos.

## Pregunta 6
https://www.youtube.com/watch?v=zMKacHGuIHI&t
https://en.wikipedia.org/wiki/Standard_streams

¿Qué son los standard streams y para qué se usan? 
Explique cada uno de ellos (stdin, stdout, stderr) ¿Cómo se los puede modificar (en una shell de linux)? 
¿Qué es un pipeline? 

De por lo menos dos ejemplos de manipulación de la entrada o salida estándar de un comando a partir de algunos de los “levels” realizados de bandit.

### Standard Streams
Son canales predefinidos usados para la entrada y salida de datos entre los procesos y el sistema operativo. Actúan como una **interfaz*** para que los programas puedan recibir y enviar entradas y salidas sin tener que preocuparse por la implementación especifica de los mismos. 
![Image Description](/images/Pasted%20image%2020250324204127.png)
#### stdin (Standard Input)
Se leen los datos de entrada, comunmente desde el teclado. 
No todos los programas requieren este input, por ejemplo, **ls** muestra los directorios sin pedir ningún input adicional. 

Para modificar este stream se puede hacer lo siguiente:

```bash
cat < test.txt
```

Esto va a cambiar la entrada a un archivo de texto en vez de al teclado.

#### stdout (Standard output)
Se escriben datos de salida, generalmente en la pantalla. 
No todos los programas producen comandos de salida. Por ejemplo, **mv** no genera ninguna salida por pantalla.

Para modificar este stream se puede hacer lo siguiente:

```bash
echo "hola prof" > test.txt
```

Esto hace que el mensaje salga en test.txt en vez de la consola.

#### stderr (Standard error)
Se muestran mensajes de error o diagnósticos. Es independiente de stodut y puede ser redirigido de manera separada.
Su principal utilidad es que permite distinguir entre **salidas y error** 

Para modificar este stream se puede hacer lo siguiente:

```bash
ls wrong_nonexistent_directory 2> error.log
```
![Image Description](/images/Pasted%20image%2020250324204530.png)

### Que es un pipeline
Un pipeline es una serie de procesos encadenados entre sí por sus **standard streams**. 
La salida **(stdout)** de cada proceso se le pasa al siguiente como input **(stdin)**

Un ejemplo puede ser:

```bash
man cp | grep copy
```

El comando **cp** produce como salida su página de manual y se le pasa al **grep** como entrada. Grep devuelve como salida todas las ocurrencias de la palabra "copy" en la página del manual.


### Manipulación de entrada y salida en bandit

```bash
ll | grep 1033
```

**ll** le pasa como entrada a grep los detalles de todos los archivos y grep busca aquéllos que pesen exactamente 1033 bytes.

```bash
2>/dev/null
```

Al agregar esto al final de un comando, el **stderror** será redirigido a **/dev/null**. Este archivo se descarta cada vez que se le escribe algo así que es perfecto para descartar errores.
