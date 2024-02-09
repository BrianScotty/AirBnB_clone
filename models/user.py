#!usr/bin/python3
"""Defines the class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
