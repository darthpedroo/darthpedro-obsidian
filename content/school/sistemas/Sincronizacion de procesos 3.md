---
date: 2025-05-14T18:28:31-03:00
lastmod: 2025-05-14T18:28:31-03:00
title: Sincronizacion de procesos 3
---
# ¿Por que necesitamos que sea correcto nuestro programa?

Necesitamos que el software que tenemos sea correcto. 

- El software de un avión no puede fallar
- El software de una excavadora no puede fallar

Ejemplo: Quiero verificar si un número es primo o no. -> Hay que demostrar que el programa

# ¿Como se que mi programa es correcto?

**Precondiciones**: Que garantiza el que va a usar el software antes de usarlo.

EJ: Ingresar un número Natural. Si no se ingresa, yo no garantizo nada. 

**Postcondiciones**: Dadas las precondiciones, determinan lo que debería pasar con el programa.

EJ: Dados dos números, el resultado será la suma de ambos.


## Problemas: Ciclos

**Ciclos Finitos**: No generan problemas , podemos desglosar el ciclo para ver todas las instrucciones.

**Ciclos Variables**: No sabemos cuantas "vueltas" va a dar el programa

Existe una **Condición de corte**

## Como se que mi programa concurrente es correcto
Estas herramientas no se trasladan muy bien en programas concurrentes.  -> Se pierde validez cuando agregamos **threads** y **recursos compartidos**

**No nos vamos a dedicar a demostrar la correctitud de nuestros progrmas concurrentes.**


### Propiedades Programas Concurrentes
- **Safety:** Propiedad que evita que "algo malo" suceda
- **Liveness** Propiedad que asegura que "algo bueno" eventualmente sucede.

**ACLARACIÓN:**

Debemos asumir que el scheduler es justo y no va a preferir **muy injustamente** a un Thread por sobre otro.

#### Liveness
Relacioando con el **progreso**. El programa avanza, eventualmente.

**OJO:** No siempre, porque sino no podriamos dejar un thread esperando.

**Tipos de progreso**

- **Local** Un thread progresa
- **Global** Todo el sistema progresa


##### Propiedades de progreso
- **Deadlock-Freedom**  En todos los estados alcanzables, al menos un thread puede progresar.

- **Starvation Freedom** En todos los estados alcanzables, todos los threads pueden progresar.

**Starvation freedom implica deadlock-freedom pero no al revés**

#### Safety
##### Propiedades de seguridad
- **Mutual exclusión**  En todos los estados alcanzables, **no hay dos threads** que accedan a un recurso compartido al mismo tiempo

- **Memory Safety**: En todos los estados alcanzables, ningún thread accede a una dirección de memoria

- **No division-by-zero** : Si se trata de dividir por 0, se levanta una 


## Problemas Clasicos de concurrencia
Son problemas que requieren de un razonamiento cuidadoso para evitar **starvation y deadlock** 

### La cena de filosofos

[Source](https://en.wikipedia.org/wiki/Dining_philosophers_problem) 

Un grupo de filósofos se sientan a la mesa a cenar

Cada filósofo tiene un tenedor a su izquierda

Un filósofo necesita dos tenedores para comer 

Más de un filósofo deberá poder comer al mismo tiempo

Que solución podemos implementar para evitar deadlocks y starvation

**Solución 1**

1 Semáforo binario por tenedor.

Se agarra un tenedor y espero un tiempo (random) // no nos sincronizamos. Si veo que no puedo comer me vuelvo a meter en la cola del semáforo

**Esperar para comer impide deadlock**

- Libre de deadlock
- Libre de starvation


**Solucion 2**

Creamos un token como el chancho va. Se va pasando entre los filósofos y les habilita comer. 

### El problema del productor-consumidor

- Tenemos un thread que cumple el rol de **productor de datos** y los coloca en un buffer (**cola con tamaño fijo**).

- Tenemos un consumidor que toma los datos del buffer y los consume. 

- Buffer tiene un tamaño limitado

- El productor no puede producir si el buffer está lleno

- El consumidor no puede consumir si el buffer esta vacío 

- **Hay que evitar el busy waiting** 

Mutex del buffer. Nunca va a pasar que uno piense que esta lleno y el otro piense que esta vacio.


¿ Que pasa sino hay un unico productor y consumidor?


### El problema de los lectores-escritores

[Source](https://en.wikipedia.org/wiki/Readers%E2%80%93writers_problem)

- En un sistema de archivos, si varios threads leen un archivo, pero no lo modifican, pueden hacerlo al mismo tiempo.

- Si un thread necesita modificar el archivo, no puede haber ningún otro thread leyendo ni modificando el archivo.

- Evitar busy waiting

- ¿ Cómo hacemos para evitar deadlocks y starvation?



Usarlo paro pensar el de hombres y mujeres (baño)



