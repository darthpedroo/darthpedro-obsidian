---
date: 2025-05-07T18:31:54-03:00
lastmod: 2025-05-07T18:31:54-03:00
title: sincronizacion de procesos 2
---

# Test And Set
El hardware suele proveer una instrucción que permite establecer **atómicamente** el valor de una variable entera en 1

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250507184537.png)


**Ejemplo de test and set**

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250507185225.png)

El problema del  Test and Set es que seguimos haciendo **BUSY WAITING**

# Semáforos

Un semáforo es un tipo abstracto de datos que nos va a ayudar a resolver problemas de sincronización.

## ¿ Cómo se usan ?

- Lo puedo crear indicando cuantos permisos hay disponibles inicialmente. 

- Puedo hacer **wait()**. Si hay un permiso disponible, lo tomo y si no espero.

- Puedo hacer **signal()**. Libero un permiso y si hay alguien esperando le doy aviso. 

## Que tienen los semáforos ¿?

- Todas las operaciones del semaforo están implementadas para ser ejecutadas **atómicamente**.
- Se utilza algún mecanismo provisto por el sistema operativo o el hardware.
- **PUEDE DESHABILITAR INTERRUPCIONES O USAR PRIMITIVAS ATÓMICAS**
- Por ahora no nos import acomo están implementados, sino que funcionan. 

## Ejemplo de implementación
![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250507190948.png)

## Para pensar…

- Por como está implementado, **NO PODEMOS LEER SU VALOR DIRECTAMENTE NI ASIGNARLE UN VALOR ARBITRARIO**.

- Cuando un thread llama a **signal()** , no puedo saber a que proceso va a despertar.

- No podemos garantizar que el proceso que se despierte sea el que estaba esperando por más tiempo, o el que tiene más prioridad, etc. 

- No podemos garantizar que el thread que se despierte vaya a ser el proximo a ejecutar. El scheduler es quien decide.

## Algunas aclaraciones
Hay 2 tipos de semáforos: **Binarios y contadores**. 
La implementación que vimos es un semaforo contador, que puede tener un valor mayor a 1.

- **Wait()**  también se conoce como **P** (intentar y decrementar)


![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250507192330.png)

## Desventajas de los semáforos

- Si no se utilizan correctamente pueden generar **deadlocks** o **starvation** 

- Tienen cierto **overhead** asociado. Ya que el **wait()** o **signal()** hace un context switch.

- En algunos casos conviene hacer **busy waiting**  utilizando **TASLocks** o **Spinlocks** basados en TAS.






