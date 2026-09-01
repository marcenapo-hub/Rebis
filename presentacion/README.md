# Presentación: dos estructuras de inversión

Material para la segunda reunión con el potencial inversor. Compara las dos
alternativas planteadas: **préstamo participativo** frente a **sociedad propia
del inversor**.

## Contenido

| Archivo | Qué es |
|---|---|
| `modelos-inversion.html` | La presentación completa (web). Página autónoma; se abre en cualquier navegador. |
| `nota-ejecutiva.html` / `.pdf` | Versión condensada a dos carillas A4 para un inversor calificado, con la comisión de gestión fija (20 %). Estilo del Manual de Identidad de Rebis. |
| `nota-ejecutiva-honorarios-1.html` / `.pdf` | Misma nota, con la comisión de gestión variable por tramo de rentabilidad — Variante 1 (una sola tasa sobre la totalidad del beneficio, la del tramo alcanzado). |
| `nota-ejecutiva-honorarios-2.html` / `.pdf` | Misma nota, con la comisión de gestión variable por tramo de rentabilidad — Variante 2 (cada tasa aplica solo a la porción de beneficio de su propio tramo). **Versión vigente**, sobre un ejemplo redondo de 1.000.000 € de capital / 250.000 € de ganancia / 12 meses. |
| `calculo.py` | Motor de cálculo que produce todas las cifras económicas. `python3 calculo.py` |

## De dónde salen los números

`nota-ejecutiva-honorarios-2` (la versión vigente) no proyecta una operación
concreta: usa un ejemplo redondo — 1.000.000 € de capital, 250.000 € de
ganancia del proyecto (25 % sobre capital) y 12 meses — para que las dos
estructuras se comparen en igualdad de condiciones. La cascada completa está
reconciliada dentro del propio documento. Las otras dos notas siguen sobre las
cifras derivadas del modelo y aún no se actualizaron.

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

- `FEE = 0.20` — comisión de gestión de Rebis sobre el beneficio del proyecto (nota-ejecutiva base)
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
