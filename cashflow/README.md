# Cash-Flow del Inversor · Ruiz Jiménez 3

`Cash-Flow-Inversor-Ruiz-Jimenez-3.xlsx` — dos escenarios conservadores sobre
la misma operación, para enviar al Inversor.

| Hoja | Estructura |
|---|---|
| Opción 1 · Participativo | La operación se canaliza por la sociedad de Rebis. El Inversor entra con préstamo participativo y cobra su porcentaje de participación. La hipoteca y el aval son de Rebis. |
| Opción 2 · Sociedad propia | La sociedad titular es del Inversor, que toma la hipoteca a su nombre con aval personal y recibe la totalidad del resultado restante. |

Fuente: `Cash-Flow.xlsx` de Sebastián (Drive) y las notas de la reunión del
22/09/2026. Las celdas con fondo cerámica son los datos de entrada; el resto
son fórmulas.

## Aplicación del Manual de Identidad

- **Tipografía Arial**, Regular y Bold. El manual designa a Arial como fuente
  de sistema de Rebis para «entornos técnicos, digitales o administrativos»,
  que es donde Poppins no está disponible: un libro de cálculo es ese caso.
- **Wordmark en la esquina superior derecha** de cada hoja, en su versión
  negra sobre fondo claro, con el área de protección libre alrededor. Es la
  única variante admitida en material corporativo.
- **Paleta principal**: negro para las bandas de sección, arcilla para los
  totales destacados, cerámica para los datos de entrada, concreto y hormigón
  para el texto secundario. **Roble Natural** queda reservado como único
  acento, sobre la rentabilidad final y la URL.
- **«Rebis»** escrito siempre con mayúscula inicial y minúsculas, nunca en
  versales.
- Cierre con la tagline a la izquierda y `rebis.com` en la esquina inferior
  derecha, alineada con el logotipo.

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

## En Google Drive

Las dos opciones están en la carpeta Lole como Hojas de cálculo nativas, con
las fórmulas vivas:

- [Opción 1 · Préstamo participativo](https://docs.google.com/spreadsheets/d/1sLJHchdOhK0BP2FYdSwcQ7g6E48WvxtHFJhNigkkqeg/edit)
- [Opción 2 · Sociedad propia](https://docs.google.com/spreadsheets/d/1WK-19NWvmQs5KihKVTjw3ZW0ceD0n9Y76l09TXcqd6o/edit)

Se cargaron como TSV con convención de locale español —coma decimal y punto y
coma como separador de argumentos—, porque el conector de Drive corrompe las
subidas binarias: un .xlsx de 19.344 bytes llegó como 18.665. El libro con
formato de marca es el `.xlsx` de esta carpeta y hay que subirlo a mano.

## Una trampa de openpyxl

El openpyxl de este entorno escribe todo el texto como `inlineStr` y no genera
`xl/sharedStrings.xml`. Es OOXML válido, pero el importador de Google no lo
interpreta y el libro se abre sin ningún texto. `tabla_cadenas.py` reescribe el
paquete con la tabla de cadenas compartidas; hay que ejecutarlo después de
generar el libro y antes de distribuirlo.
