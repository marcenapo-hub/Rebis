# Presentación: dos estructuras de inversión

Material para la segunda reunión con el potencial inversor. Compara las dos
alternativas planteadas: **préstamo participativo** frente a **sociedad propia
del inversor**.

## Contenido

| Archivo | Qué es |
|---|---|
| `modelos-inversion.html` | La presentación. Página autónoma; se abre en cualquier navegador. |
| `calculo.py` | Motor de cálculo que produce todas las cifras económicas. `python3 calculo.py` |

## De dónde salen los números

`calculo.py` reimplementa las hojas `Inputs` y `Cálculos y Resultados` del
**Modelo de Flipping Rebis v1** (Google Drive) y reproduce exactamente su caso
base: coste total 1.776.382,39 €, capital propio 1.102.632,39 € y beneficio
bruto 272.917,61 €.

Fuentes documentales usadas en la presentación:

- Modelo de Flipping Rebis v1 — inputs, escenarios, flujo de fondos y auditoría
- Cash-Flow García Paredes 21 y Ruiz Jiménez 3 — proyecciones
- Liquidación Final San Andrés 1 y Resumen Liquidación Brescia — operaciones cerradas
- Estructuración de la Participación de los Inversores
- Formas de aporte · Plazos para la Adquisición · Información Inversor

## Parámetros de la cascada de reparto

Definidos como constantes en `calculo.py` para poder ajustarlos si cambian los
términos negociados:

- `FEE = 0.20` — comisión de gestión de Rebis sobre el beneficio del proyecto
- `IS = 0.25` — Impuesto sobre Sociedades (solo Modelo B)
- `WHT_DIV = 0.10` — retención por salida de capital vía dividendo (solo Modelo B)
- `VEHICULO` — coste del vehículo societario prorrateado a 11 meses

## Pendiente de validación

La presentación marca explícitamente lo que falta definir o confirmar antes de
firmar (sección 9). Los dos supuestos con mayor impacto económico son la
deducibilidad del interés participativo en el Impuesto sobre Sociedades y el
tipo de retención aplicable; ambos requieren confirmación de un abogado
mercantil y un asesor fiscal españoles.
