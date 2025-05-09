---
date: 2025-05-07T18:31:54-03:00
lastmod: 2025-05-07T18:31:54-03:00
title: Threads
---

# Problemas de la concurrencia

Dificil de saber si son **correctos**

**Correctitud**: Dadas las precondiciones que pide el programa, el resultado del proceso que corre el programa coincide con la función matemática que nosotros planteamos de la teoría. 

## No determinismo

## Race conditions

Se pueden generar comportamientos que no queremos.

Para el mismo input el programa da resultados distintos (**erróneos en algunos casos**) dependiendo del orden en el que se ejecutan sus distintas tareas. 

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430184337.png)

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430184423.png)

**IMPORTANTE:** Estamos asumiendo que se ejecutan de manera atómica. 

Si no fuera atḿica puden pasar peores cosas:

## Data Race 

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430184842.png)

Se accede a la misma estructura de datos y al menos uno de los dos lo modifica. 

### Data race vs Race Condition

Data race = Genera resultados que no son equivalentes a **NINGUNA EJECUCIÓN SECUENCIAL**

## Como sincrozinar los threads

Buscamos sincronizar **lo menos posible** pero que aún así devuelva trazas validas.

### Clock
- Se puede usar un clock -> Trae mucho overhead. No es muy recomendable.

### Mensajes

Se pueden comunicar a través de mensajes:

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430185945.png)

EJEMPLO: Queremos que pepe Codee antes que pato. Buscamos tener una traza valida para que pase esto.

Para esto, agregamos a BOB, 

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430190345.png)

#### Problemas de los mensajes

- Utiliza recursos del sistema
- Utiliza **tiempo** -> Escribir en el disco. 
- Dificir de implementar y mantener. Especialmente en sistemas grandes. 
- Los mensajes tienen un límite en tamaño. 

**EJEMPLO:** Si Pepe se muere antes de codear, pato **JAMÁS VA A CODEAR.**

### Sección Crítica:

#### Ejemplo práctico
En el cuarto oscuro, no debería haber más de una persona a la vez. Para garantizar el carácter secreto del voto. 

Se siguen protocolos para "sincronizar"  a las personas para que no haya dos votando, etc. 

El recurso compartido sería el cuarto oscuro. 

#### Ejemplo técnico

- Considerar un sistema de **n procesos** 

- Cada proceso tiene un segmento de código, llamado **sección crítica** , en el cual peude modificar variables compartidas. 

- Debemos encontrar un protocolo que **GARANTICE** que hay un solo proceso en la sección crítica. 


##### Que va a necesitar esta solución?

- **Exlucusión mutua:** Si un proceso está ejecutando en su sección crítica, ningún otro puede estar ejecutando la suya. 

- **Garantía de entrada:** Si un proceso intenta entrar a su sección crítica, **eventualmente** lo logra. ( Esto garantiza que no haya **starvation**)


##### Implementación en este código
![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430192605.png)

Asumimos que critical section nunca se cuelga.

**Ejemplo mal**

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430195908.png)

**Ejemplo mal x2**
![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430201552.png)

##### Solución: Algoritmo de Peterson

[Source](https://es.wikipedia.org/wiki/Algoritmo_de_Peterson)

**Problema**: Hace busy Waiting...


![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250430202701.png)







