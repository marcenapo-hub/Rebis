# Cash-Flow del Inversor · Ruiz Jiménez 3

`Cash-Flow-Inversor-Ruiz-Jimenez-3.xlsx` — dos escenarios conservadores sobre
la misma operación, para enviar al Inversor.

| Hoja | Estructura |
|---|---|
| Opción 1 · Participativo | La operación se canaliza por la sociedad de Rebis. El Inversor entra con préstamo participativo y cobra su porcentaje de participación. La hipoteca y el aval son de Rebis. |
| Opción 2 · Sociedad propia | La sociedad titular es del Inversor, que toma la hipoteca a su nombre con aval personal y recibe la totalidad del resultado restante. |

Fuente: `Cash-Flow.xlsx` de Sebastián (Drive) y las notas de la reunión del
22/09/2026. Las celdas en azul son los datos de entrada; el resto son fórmulas.

## Resultado

| | Opción 1 | Opción 2 |
|---|---|---|
| Aporte del Inversor | 906.254,45 € | 906.254,45 € |
| Beneficio de la operación | 427.210,60 € | 372.093,09 € |
| Honorarios de Rebis | 86.240,02 € | 92.605,72 € |
| Ganancia del Inversor | 124.525,52 € | 207.562,54 € |
| **Rentabilidad sobre su capital** | **13,74 %** | **22,90 %** |

## Dos correcciones sobre el archivo original

1. **Los 6.500 € de interiorismo y arquitectura no se habían propagado al
   aporte del Inversor.** Entraron en el bloque de reforma, pero el aporte
   siguió en 899.754,45 €: los aportes sumaban 1.959.368,44 € contra un
   capital necesario de 1.965.868,44 €, y los porcentajes de participación
   sumaban 99,67 % en lugar de 100 %. El aporte correcto es **906.254,45 €**,
   y ahora sale por fórmula en las dos hojas. La Opción 2 llega al mismo
   importe por un camino independiente, lo que confirma la cifra.

2. **La comisión inmobiliaria de venta** pasa a calcularse como 3,63 %
   (3 % más IVA) sobre el precio de venta, en vez de ir fijada a mano.

La ganancia de la constructora es la única cifra sin fórmula, tal como estaba
en el original. Queda marcada en azul como dato de entrada en ambas hojas.

## Equivalencia sin honorarios

El modelo muestra la rentabilidad después de los honorarios de Rebis. La línea
siguiente devuelve la equivalencia sin ellos: 18,13 % en la Opción 1 y 33,12 %
en la Opción 2. Es el cálculo exacto — dividir por 0,758 — y no el atajo de
multiplicar por 1,242, que se queda corto.
