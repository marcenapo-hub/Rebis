# -*- coding: utf-8 -*-
"""Pasa las cadenas en linea (inlineStr) a una tabla de cadenas compartidas.

openpyxl escribe aqui todo el texto como <is><t>...</t></is> y no genera
xl/sharedStrings.xml. Es valido, pero el importador de Google no lo interpreta
y el libro se abre sin ningun texto. Esto reescribe el paquete con la tabla.
"""
import re, shutil, sys, zipfile

CELDA = re.compile(
    r'<c ([^>]*?)t="inlineStr"([^>]*?)>\s*<is>\s*<t([^>]*?)>(.*?)</t>\s*</is>\s*</c>',
    re.S)
SST_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
SST_CT = ("application/vnd.openxmlformats-officedocument."
          "spreadsheetml.sharedStrings+xml")
SST_REL = ("http://schemas.openxmlformats.org/officeDocument/2006/"
           "relationships/sharedStrings")


def convertir(path):
    with zipfile.ZipFile(path) as z:
        partes = {i.filename: z.read(i.filename) for i in z.infolist()}
        orden = [i.filename for i in z.infolist()]

    tabla, indice, total = [], {}, 0

    def reemplazar(m):
        nonlocal total
        pre, post, attrs, texto = m.groups()
        clave = (attrs, texto)
        if clave not in indice:
            indice[clave] = len(tabla)
            tabla.append(clave)
        total += 1
        return f'<c {pre}t="s"{post}><v>{indice[clave]}</v></c>'

    hojas = [n for n in partes if re.match(r'xl/worksheets/sheet\d+\.xml$', n)]
    for n in hojas:
        partes[n] = CELDA.sub(reemplazar, partes[n].decode("utf-8")).encode("utf-8")

    if not tabla:
        return 0, 0

    sst = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           f'<sst xmlns="{SST_NS}" count="{total}" uniqueCount="{len(tabla)}">']
    sst += [f'<si><t{a}>{t}</t></si>' for a, t in tabla]
    sst.append('</sst>')
    partes["xl/sharedStrings.xml"] = "".join(sst).encode("utf-8")

    ct = partes["[Content_Types].xml"].decode("utf-8")
    if "sharedStrings.xml" not in ct:
        ct = ct.replace("</Types>",
                        f'<Override PartName="/xl/sharedStrings.xml" ContentType="{SST_CT}"/></Types>')
        partes["[Content_Types].xml"] = ct.encode("utf-8")

    rels = partes["xl/_rels/workbook.xml.rels"].decode("utf-8")
    if "sharedStrings.xml" not in rels:
        usados = set(re.findall(r'Id="(rId\d+)"', rels))
        nuevo = next(f"rId{i}" for i in range(1, 1000) if f"rId{i}" not in usados)
        rels = rels.replace("</Relationships>",
                            f'<Relationship Id="{nuevo}" Type="{SST_REL}" Target="sharedStrings.xml"/></Relationships>')
        partes["xl/_rels/workbook.xml.rels"] = rels.encode("utf-8")

    if "xl/sharedStrings.xml" not in orden:
        orden.insert(orden.index("xl/workbook.xml") if "xl/workbook.xml" in orden else 0,
                     "xl/sharedStrings.xml")

    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n in orden:
            z.writestr(n, partes[n])
    shutil.move(tmp, path)
    return total, len(tabla)


if __name__ == "__main__":
    t, u = convertir(sys.argv[1])
    print(f"{t} cadenas en linea -> tabla compartida de {u} entradas")
