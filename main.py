import itertools
import os
import pickle
from typing import List, Dict, AnyStr

from services.nlp.util import extract_tipo


def extract_data(archivo_normales: AnyStr) -> Dict:
    """
    Extraer lod datos del .pkl
    :return:
    """
    path = 'data/' + archivo_normales
    with open(path, 'rb') as f:
        data: dict = pickle.load(f)
    return data


def normalize_dicts(data_dict: dict) -> List[Dict]:
    """
    Toma los datos originales de pickle, y retorna una lista de diccionarios.
    [{'edicion', 'seccion', 'organismo', 'sujeto_obligado', 'nombre', 'fecha_emision', 'url', 'texto', 'pdf', 'dof_id'}]
    La última llave es agregada dof_id, que es el identificador del documento.
    :param data_dict:
    :return List[Dict]
    """
    dof_id = [_id for _id in data_dict]
    dict_values: List[Dict] = [value for value in data_dict.values()]
    for unique, val in zip(dof_id, dict_values):
        val['dof_id'] = unique

    return dict_values


def refifinado(lista: List):
    normales = list()

    for element in lista:
        original_data: Dict = extract_data(element)
        normalizados = normalize_dicts(original_data)
        normales.append(normalizados)

    return list(itertools.chain(*normales))


def lower_strip_text(los_com):
    for diccionario in los_com:
        new_title: AnyStr = diccionario['nombre'].lower().strip()
        new_text: AnyStr = diccionario['texto'].lower().strip()
        diccionario['texto'] = new_text
        diccionario['nombre'] = new_title

    return los_com


def main():
    lista_de_pepinillos = os.listdir(path='/Users/usuarioman/Desktop/MMSL/durazo/data')
    los_comunes = refifinado(lista_de_pepinillos)
    striped = lower_strip_text(los_comunes)
    con_tipo = extract_tipo(los_comunes)
    return con_tipo


if __name__ == '__main__':
    main()



