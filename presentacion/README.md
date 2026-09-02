# Presentación: dos estructuras de inversión

Material para la segunda reunión con el potencial inversor. Compara las dos
alternativas planteadas: **préstamo participativo** frente a **sociedad propia
del inversor**.

## Contenido

| Archivo | Qué es |
|---|---|
| `modelos-inversion.html` | La presentación completa (web). Página autónoma; se abre en cualquier navegador. |
| `nota-ejecutiva-honorarios-2.html` / `.pdf` | **Documento vigente.** Nota de dos carillas A4 para el Inversor, con la rentabilidad antes de impuestos y los honorarios de Rebis explícitos. |
| `nota-ejecutiva.html` / `.pdf` · `nota-ejecutiva-honorarios-1.html` / `.pdf` | Versiones anteriores, **desactualizadas**: cifras después de impuestos y comisión por tramos. No enviar sin realinear. |
| `calculo.py` | Motor de cálculo que produce todas las cifras económicas. `python3 calculo.py` |

## De dónde salen los números

`calculo.py` reimplementa las hojas `Inputs` y `Cálculos y Resultados` del
**Modelo de Flipping Rebis v1** (Google Drive) y reproduce exactamente su caso
base: coste total 1.776.382,39 €, capital propio 1.102.632,39 € y beneficio
bruto 272.917,61 €.

Las dos rentabilidades del documento vigente salen de
`comparacion_pre_impuestos()`, sobre esa misma operación y antes de los
impuestos del Inversor. La diferencia entre ambas es quién toma la hipoteca:

| | Capital del Inversor | Honorarios | Resultado | Rentabilidad (11 meses) |
|---|---|---|---|---|
| Modelo A · préstamo participativo | 1.719.421 € | 67.775 € (20,55 %) | 262.104 € | **15,24 %** |
| Modelo B · sociedad propia | 1.102.632 € | 58.581 € (21,46 %) | 184.911 € | **16,77 %** |

Los honorarios siguen la escala por tramos aplicada sobre el excedente
(`fee_variante2`): cada tasa grava solo la porción de rentabilidad de su propio
tramo, de ahí que la tasa efectiva difiera entre modelos.

En el Modelo A la financiación bancaria y el aval quedan en Rebis, de modo que
el apalancamiento no juega a favor del Inversor. En el Modelo B la hipoteca
(55 % del precio de compra) la toma la sociedad del Inversor, con su aval
personal, y por eso el mismo resultado se obtiene sobre menos capital propio.
El Modelo B soporta además el 2 % por la gestión de la hipoteca y el coste de
la sociedad vehículo.

Fuentes documentales usadas en la presentación:

- Modelo de Flipping Rebis v1 — inputs, escenarios, flujo de fondos y auditoría
- Cash-Flow García Paredes 21 y Ruiz Jiménez 3 — proyecciones
- Liquidación Final San Andrés 1 y Resumen Liquidación Brescia — operaciones cerradas
- Estructuración de la Participación de los Inversores
- Formas de aporte · Plazos para la Adquisición · Información Inversor

## Parámetros de la cascada de reparto

Definidos como constantes en `calculo.py` para poder ajustarlos si cambian los
términos negociados:

- `HON_HIPOTECA = 0.02` — comisión por la gestión de la hipoteca y el aporte del aval (solo Modelo B)
- `FEE = 0.20` — comisión fija usada por las notas anteriores
- `IS = 0.25` — Impuesto sobre Sociedades (solo Modelo B)
- `WHT_DIV = 0.10` — retención por salida de capital vía dividendo (solo Modelo B)
- `VEHICULO` — coste del vehículo societario prorrateado a 11 meses
- `TRAMOS` — tramos de rentabilidad y tasa de comisión para las variantes 1 y 2 (0–15 % → 20 %,
  15–20 % → 22,5 %, 20–25 % → 25 %, >25 % → 30 %), usados por `cascada_variable()`

## Pendiente de validación

La presentación marca explícitamente lo que falta definir o confirmar antes de
firmar (sección 9). Los dos supuestos con mayor impacto económico son la
deducibilidad del interés participativo en el Impuesto sobre Sociedades y el
tipo de retención aplicable; ambos requieren confirmación de un abogado
mercantil y un asesor fiscal españoles.
