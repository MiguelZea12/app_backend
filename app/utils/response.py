from flask import jsonify, make_response
from typing import Union, List

def create_response(status: str, data: Union[dict, List[dict], None] = None, message: str = None, status_code: int = 200):
  """Crea una respuesta para el cliente.
     
  Args:
  `status`: str - Estado de la respuesta.
  `data`: dict, List[dict], None - Datos de la respuesta.
  `message`: str - Mensaje de la respuesta.
  `status_code`: int - Código de estado de la respuesta.
    
  """


  response = {
        'status': status,
        'message': message,
        'data': data
    }
    
  return make_response(jsonify(response), status_code)
