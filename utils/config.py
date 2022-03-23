import logging

import os 

from pydantic import BaseSettings

log = logging.getLogger('uvicorn')

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")