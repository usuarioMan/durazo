import re
from typing import Dict, List

tipo_de_acto = [
    'resolución', 'decreto', 'convenio', 'acuerdo', 'sentencia', 'tasa de interés', 'tipo de cambio',
]


def extract_tipo(lista_dict_normalizados: List[Dict]) -> List[Dict]:
    for diccionario in lista_dict_normalizados:

        # TODO: metele un regex aquí.
        if any(word in diccionario['nombre'] for word in tipo_de_acto):
            for tipo in tipo_de_acto:
                # TODO: re.findall()
                if tipo in diccionario['nombre']:
                    diccionario['tipo'] = tipo

        else:
            diccionario['tipo'] = 'otro'

    return lista_dict_normalizados
