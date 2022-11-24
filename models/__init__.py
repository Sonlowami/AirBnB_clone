#!/usr/bin/python3
"""
Do basic initialization process
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
