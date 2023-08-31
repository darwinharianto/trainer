import reflex as rx
import requests
from .cvat_cfg import *
import sqlmodel

class User(rx.Model, table=True):
    __tablename__ = 'users'
    id: int = sqlmodel.Field(default=None, primary_key=True)
    username: str

    def fetch_user(self):
        return

    @staticmethod
    def register_user(username:str, email:str, password:str):
        raise NotImplementedError
        return
    
    @staticmethod
    def delete_user(username:str, email:str, password:str):
        raise NotImplementedError
        return
    
    @staticmethod
    def check_credentials(username:str, password:str):
        url = CVAT_ADDRESS + "/api/auth/login"
        body = {
                "username": username,
                "password": password
                }
        headers = {
            "Content-Type": "application/json"
        }
        result = requests.post(url, headers=headers, json=body)
        
        return result