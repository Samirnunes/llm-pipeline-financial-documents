from typing import Dict

import instructor
from litellm import completion
from pydantic import BaseModel
from tenacity import retry, stop_after_attempt, wait_fixed

from ..log import logger
from ..models import InformeDeRendimentos, NotaFiscalDeServico
from ..prompt import Prompt

MODELS_MAP = {
    "nota-fiscal-de-servico": NotaFiscalDeServico,
    "informe-de-rendimentos": InformeDeRendimentos,
}

PATH = "prompts/extractor/"

SYSTEM = Prompt.from_yaml(PATH + "system.yaml")
USER = Prompt.from_yaml(PATH + "user.yaml")


class FinancialDocumentExtractor:
    def __init__(self) -> None:
        self._client = instructor.from_litellm(completion)

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(5))
    def invoke(self, text: str, classification: str) -> Dict:
        logger.info(f"Running {self.__class__.__name__}...")

        response: BaseModel = self._client.chat.completions.create(
            model="lm_studio/meta-llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM.format({"classification": classification}),
                },
                {
                    "role": "user",
                    "content": USER.format(
                        {"classification": classification, "text": text}
                    ),
                },
            ],
            response_model=MODELS_MAP[classification],
        )

        logger.info(f"Financial document's extracted info: {response.model_dump()}")

        return response.model_dump()
