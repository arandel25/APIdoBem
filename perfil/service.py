from webbrowser import get
import requests
from typing import Dict
from django.http import response

class PerfilService():
    def buscar_cep(self, cep:str) -> Dict:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if not response.ok:
            return None
        return response.json()

    def create_to_save(self, data_response:dict, data_request:dict) -> Dict:
        return {
            "nome_instituicao" : data_request.get("nome_instituicao"),
            "cnpj" : data_request.get("cnpj"),
            "cep" : data_request.get("cep"),
            "logradouro" : data_response.get("logradouro"),
            "complemento" : data_response.get("complemento"),
            "bairro" : data_response.get("bairro"),
            "municipio" : data_response.get("localidade"),
            "uf" : data_response.get("uf"),
        }
    