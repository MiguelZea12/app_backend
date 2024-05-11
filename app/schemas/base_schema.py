from marshmallow import Schema, pre_load


class BaseSchema(Schema):  # Define una nueva clase llamada BaseSchema que hereda de Schema de Marshmallow
    """Esquema base.""" 

    @pre_load(pass_many=True)  # Decorador pre_load para ejecutar la función antes de cargar los datos
    def string_to_none(self, data, many, **kwargs):  # Define una función llamada string_to_none que convierte cadenas vacías en None
        def turn_to_none(x):  # Función interna para convertir una cadena vacía en None
            return None if (x == "" or (x == 0 and type(x) == int)) else x  # Convierte una cadena vacía en None

        if isinstance(data, dict):  # Si los datos son un diccionario
            for k, v in data.items():  # Itera sobre los elementos del diccionario
                data[k] = turn_to_none(v)  # Convierte los valores de cadena vacía a None
        elif isinstance(data, list):  # Si los datos son una lista
            for i in range(len(data)):  # Itera sobre los elementos de la lista
                for k, v in data[i].items():  # Itera sobre los elementos de cada diccionario en la lista
                    data[i][k] = turn_to_none(v)  # Convierte los valores de cadena vacía a None
        return data  # Devuelve los datos modificados

