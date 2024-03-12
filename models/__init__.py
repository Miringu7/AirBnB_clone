#!/usr/bin/python3
"""__init__ method for models folder"""
from models.engine.file_storage import FileStorage
"""import file_storage.py"""


storage = FileStorage()
"""create the variable storage, an instance of FileStorage"""
storage.reload()
"""call reload() method on the storage variable"""
