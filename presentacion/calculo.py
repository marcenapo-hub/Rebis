"""Motor de calculo de la presentacion de estructuras de inversion.

Reimplementacion fiel de la hoja `Inputs` / `Calculos y Resultados` del
"Modelo de Flipping Rebis v1" (Google Drive). Reproduce exactamente el caso
base: coste total 1.776.382,39 EUR, capital propio 1.102.632,39 EUR y
beneficio bruto 272.917,61 EUR.

Uso:  python3 calculo.py
"""
# Reimplementacion fiel del "Modelo de Flipping v1" (hoja Inputs / Calculos)
def op(P, V, obra, m2=162, ltv=0.55, meses_obra=8, meses_com=3, coste_fin=37000.0,
       muebles=22000.0, derramas=8000.0, con_hipoteca=True):
    H = P*ltv if con_hipoteca else 0.0
    adq = P*0.03*1.21 + 50 + P*0.02 + 2700 + 394.46 + 1850 + 900
    fin = (839.44 + H*0.012 + H*0.005 + coste_fin + 575.28 + 649.51 + 1780 + 394.46 + 900) if con_hipoteca else 0.0
    ref = obra + muebles + obra*0.0568 + derramas + 210 + 2226.91 + 810*meses_obra
    ven = V*0.03*1.21 + 1350 + H*0.005 + 394.46 + 900 + P*0.02
    coste = P + adq + fin + ref + ven
    bruto = V - coste
    capital = coste - H
    return dict(P=P,V=V,H=H,adq=adq,fin=fin,ref=ref,ven=ven,coste=coste,bruto=bruto,
                capital=capital,meses=meses_obra+meses_com)

def anual(roi, meses): return (1+roi)**(12/meses)-1

BASE = op(1225000, 2049300, 264107)


VEHICULO = 4700 + 3000 + 9000 * 11 / 12   # TMF neto (7.000-2.300) + legales/notariales + mantenimiento 11 meses
FEE = 0.20        # comision de gestion Rebis sobre el beneficio del proyecto
IS = 0.25         # Impuesto sobre Sociedades (Modelo B)
WHT_DIV = 0.10    # retencion por salida de capital / dividendo (Modelo B), a validar


def cascada(o, veh=VEHICULO):
    """Reparte el beneficio bruto por los dos caminos: A (prestamo) y B (sociedad)."""
    proyecto = o['bruto'] - veh
    fee = proyecto * FEE
    base = proyecto - fee
    a_neto = base                       # interes participativo: gasto deducible -> IS 0
    b_tras_is = base * (1 - IS)
    b_neto = b_tras_is * (1 - WHT_DIV)
    return dict(bruto=o['bruto'], vehiculo=veh, proyecto=proyecto, fee=fee, base=base,
                a_neto=a_neto, a_roi=a_neto / o['capital'], a_anual=anual(a_neto / o['capital'], o['meses']),
                b_is=base * IS, b_tras_is=b_tras_is, b_wht=b_tras_is * WHT_DIV,
                b_neto=b_neto, b_roi=b_neto / o['capital'], b_anual=anual(b_neto / o['capital'], o['meses']))


ESCENARIOS = {   # mismos supuestos que la hoja "Escenarios" del modelo v1
    'Conservador': dict(dP=+0.03, dV=-0.08, dObra=+0.10, dMeses=+2, dFin=+0.15),
    'Base':        dict(dP=0.00,  dV=0.00,  dObra=0.00,  dMeses=0,  dFin=0.00),
    'Optimista':   dict(dP=-0.03, dV=+0.06, dObra=-0.05, dMeses=-1, dFin=-0.10),
}

if __name__ == '__main__':
    print(f"{'Escenario':<13}{'Coste':>13}{'Bruto':>12}{'Capital':>13}{'Meses':>7}"
          f"{'A neto':>12}{'A ROI':>9}{'B neto':>12}{'B ROI':>9}")
    for nombre, s in ESCENARIOS.items():
        o = op(1225000 * (1 + s['dP']), 2049300 * (1 + s['dV']), 264107 * (1 + s['dObra']),
               meses_obra=8 + s['dMeses'], coste_fin=37000 * (1 + s['dFin']))
        c = cascada(o)
        print(f"{nombre:<13}{o['coste']:>13,.0f}{c['bruto']:>12,.0f}{o['capital']:>13,.0f}"
              f"{o['meses']:>7}{c['a_neto']:>12,.0f}{c['a_roi']:>9.2%}{c['b_neto']:>12,.0f}{c['b_roi']:>9.2%}")

    print("\nMisma operacion sin hipoteca:")
    o = op(1225000, 2049300, 264107, con_hipoteca=False)
    c = cascada(o)
    print(f"  capital necesario {o['capital']:,.0f} EUR | B ROI {c['b_roi']:.2%}")

    print("\nPunto de equilibrio (beneficio bruto = 0), manteniendo el resto constante:")
    lo, hi = 1500000.0, 2100000.0
    for _ in range(80):
        m = (lo + hi) / 2
        hi, lo = (m, lo) if op(1225000, m, 264107)['bruto'] > 0 else (hi, m)
    print(f"  precio de venta minimo: {(lo + hi) / 2:,.0f} EUR")
    lo, hi = 1000000.0, 1600000.0
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if op(m, 2049300, 264107)['bruto'] > 0 else (lo, m)
    print(f"  precio de compra maximo: {(lo + hi) / 2:,.0f} EUR")


# ---------------------------------------------------------------------------
# Honorarios variables por tramo de rentabilidad (nota-ejecutiva-honorarios-*)
#
# La comision de gestion, en vez de un 20% fijo, depende del tramo de
# rentabilidad que alcanza el proyecto (beneficio del proyecto / capital
# propio, antes de comision). Dos formas de aplicar esos tramos:
#
#   Variante 1: se aplica UNA sola tasa -- la del tramo alcanzado -- sobre
#               la TOTALIDAD del beneficio del proyecto.
#   Variante 2: cada tasa se aplica solo a la PORCION de beneficio que cae
#               dentro de su propio tramo (la tasa efectiva resultante es
#               un promedio ponderado, siempre <= la tasa de la Variante 1).
#
# Los tramos y tasas son los mismos en ambas variantes; ver
# nota-ejecutiva-honorarios-1.pdf / -2.pdf para su presentacion al inversor.
TRAMOS = [(0.00, 0.15, 0.20), (0.15, 0.20, 0.225), (0.20, 0.25, 0.25), (0.25, float('inf'), 0.30)]


def fee_variante1(gross_roi, proyecto):
    """Tasa unica del tramo alcanzado, sobre la totalidad del beneficio."""
    for lo, hi, rate in TRAMOS:
        if gross_roi < hi or hi == float('inf'):
            return rate * proyecto


def fee_variante2(gross_roi, capital):
    """Cada tasa aplica solo a la porcion de beneficio dentro de su tramo."""
    fee = 0.0
    for lo, hi, rate in TRAMOS:
        amt = max(0.0, min(gross_roi, hi) - lo) * capital
        fee += amt * rate
    return fee


def cascada_variable(o, variante, veh=VEHICULO):
    """Igual que cascada(), pero con comision de gestion variable por tramo."""
    proyecto = o['bruto'] - veh
    capital = o['capital']
    gross_roi = proyecto / capital
    fee = fee_variante1(gross_roi, proyecto) if variante == 1 else fee_variante2(gross_roi, capital)
    base = proyecto - fee
    a_neto = base
    b_tras_is = base * (1 - IS)
    b_neto = b_tras_is * (1 - WHT_DIV)
    return dict(bruto=o['bruto'], proyecto=proyecto, gross_roi=gross_roi, fee=fee, fee_pct=fee / proyecto,
                base=base, a_neto=a_neto, a_roi=a_neto / capital, a_anual=anual(a_neto / capital, o['meses']),
                b_is=base * IS, b_wht=b_tras_is * WHT_DIV, b_neto=b_neto,
                b_roi=b_neto / capital, b_anual=anual(b_neto / capital, o['meses']))


if __name__ == '__main__':
    print("\n" + "=" * 78)
    print("Honorarios variables por tramo -- comparacion Variante 1 vs Variante 2")
    for variante in (1, 2):
        print(f"\n--- Variante {variante} ---")
        for nombre, s in ESCENARIOS.items():
            o = op(1225000 * (1 + s['dP']), 2049300 * (1 + s['dV']), 264107 * (1 + s['dObra']),
                   meses_obra=8 + s['dMeses'], coste_fin=37000 * (1 + s['dFin']))
            c = cascada_variable(o, variante)
            print(f"{nombre:<13} rentab.proyecto={c['gross_roi']:>7.2%} fee={c['fee']:>10,.0f}({c['fee_pct']:>6.2%}) "
                  f"base={c['base']:>10,.0f}  A={c['a_roi']:>7.2%}/{c['a_anual']:>7.2%}  "
                  f"B={c['b_roi']:>7.2%}/{c['b_anual']:>7.2%}")


# ---------------------------------------------------------------------------
# Comparacion vigente de la nota ejecutiva: rentabilidad ANTES de impuestos.
#
# La diferencia economica entre los dos modelos es quien toma la financiacion
# bancaria y, con ella, quien se queda el apalancamiento y el riesgo:
#
#   Modelo A  Prestamo participativo a la sociedad de Rebis. La hipoteca, si
#             se usa, la toma Rebis sobre su propia sociedad y su historial;
#             el aval es de Rebis. La retribucion del Inversor no se apalanca,
#             de modo que su capital cubre el coste de la operacion.
#   Modelo B  Sociedad propia del Inversor. La hipoteca la toma su sociedad
#             (~55% del precio de compra) con aval personal del Inversor, y el
#             apalancamiento juega a su favor. Paga ademas la comision por la
#             gestion de la hipoteca y el coste de su sociedad vehiculo.
# Los honorarios siguen la escala de TRAMOS por excedente (fee_variante2): cada
# tasa se aplica solo a la porcion de rentabilidad de su propio tramo.
HON_HIPOTECA = 0.02   # comision por gestion de la hipoteca y aporte del aval (solo Modelo B)


def comparacion_pre_impuestos(P=1225000, V=2049300, obra=264107):
    """Rentabilidad del Inversor, antes de sus impuestos, en cada modelo."""
    a = op(P, V, obra, con_hipoteca=False)   # el Inversor financia; Rebis ejecuta
    b = op(P, V, obra)                       # la sociedad del Inversor toma la hipoteca
    a_hon = fee_variante2(a['bruto'] / a['capital'], a['capital'])
    b_hon = fee_variante2(b['bruto'] / b['capital'], b['capital'])
    a_neto = a['bruto'] - a_hon
    b_neto = b['bruto'] - b_hon - b['H'] * HON_HIPOTECA - VEHICULO
    return dict(a_capital=a['capital'], a_neto=a_neto, a_roi=a_neto / a['capital'],
                a_hon=a_hon, a_hon_pct=a_hon / a['bruto'],
                b_capital=b['capital'], b_neto=b_neto, b_roi=b_neto / b['capital'],
                b_hon=b_hon, b_hon_pct=b_hon / b['bruto'],
                hipoteca=b['H'], ltv=b['H'] / b['P'], meses=b['meses'])


if __name__ == '__main__':
    c = comparacion_pre_impuestos()
    print("\n" + "=" * 78)
    print(f"Rentabilidad antes de impuestos, en {c['meses']} meses "
          f"(hipoteca {c['hipoteca']:,.0f} EUR, LTV {c['ltv']:.0%} s/precio)")
    print(f"  Modelo A  capital {c['a_capital']:>12,.0f}  honorarios {c['a_hon']:>10,.0f}({c['a_hon_pct']:>6.2%})"
          f"  resultado {c['a_neto']:>11,.0f}  {c['a_roi']:>7.2%}")
    print(f"  Modelo B  capital {c['b_capital']:>12,.0f}  honorarios {c['b_hon']:>10,.0f}({c['b_hon_pct']:>6.2%})"
          f"  resultado {c['b_neto']:>11,.0f}  {c['b_roi']:>7.2%}   (+2% hipoteca, +vehiculo)")
