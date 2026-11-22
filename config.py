"""
Configuration file for the AI Career Coach application.
Loads environment variables from a .env file and provides access to configuration settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    "Central Configuration Class"

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME","gemini-3.1-flash-lite")

    @staticmethod
    def validate() -> None:
        "Validate Mandatory Configuration"

        if not Config.GEMINI_API_KEY:
            raise ValueError("Gemini API KEY is missing. Please check the file.")