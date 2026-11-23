"""
Gemini Service
Responsible for communicating with the Gemini Api

Responsibilities:
- Initialize the Gemini API client using the provided API key.
- Provide a method to generate responses from the Gemini API based on input prompts.
- Return the generated response text or raise an error if the API call fails.
- Keep API specific codes isolated from the agents
"""

from google import genai
from typing import Any, Optional
from config import Config


class GeminiService:
    """
    Wrapper around Google's Gemini API
    """

    def __init__(self):
        Config.validate()
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        

    def generate_response(self, prompt: str, config: Optional[Any] = None) -> Any:
        """
        Generate a response from the Gemini API based on the provided prompt.

        Args:
            prompt (str): The input prompt for which to generate a response.
            config (Optional[Any]): Optional configuration parameters for the Gemini API request.
        Returns:
            AI generated Response
        """

        try:
            response = self.client.models.generate_content(
                model = Config.MODEL_NAME,
                contents = prompt,
                config = config
                )
            return response
        except Exception as ex:
            raise RuntimeError(f"gemini Api Error : {ex}")