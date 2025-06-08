from enum import Enum

import instructor
from litellm import completion
from pydantic import BaseModel, Field

from ..log import logger
from ..prompt import Prompt

PATH = "prompts/classifier/"

SYSTEM = Prompt.from_yaml(PATH + "system.yaml")
USER = Prompt.from_yaml(PATH + "user.yaml")
TOOL = Prompt.from_yaml(PATH + "tool.yaml")
CLASSIFICATION_FIELD = Prompt.from_yaml(PATH + "classification-field.yaml")


class DocumentType(Enum):
    NOTA_FISCAL_DE_SERVICO = "nota-fiscal-de-servico"
    INFORME_DE_RENDIMENTOS = "informe-de-rendimentos"


class DocumentClass(BaseModel):
    f"""{TOOL.format({})}"""
    classification: DocumentType = Field(
        ..., description=CLASSIFICATION_FIELD.format({})
    )


class FinancialDocumentClassifier:
    def __init__(self) -> None:
        self._client = instructor.from_litellm(completion)

    def invoke(self, text: str) -> str:
        """
        Invokes the document classifier.
        """
        logger.info(f"Running {self.__class__.__name__}...")

        response: DocumentClass = self._client.chat.completions.create(
            model="lm_studio/meta-llama-3.1-8b-instruct",
            messages=[
                {"role": "system", "content": SYSTEM.format({})},
                {
                    "role": "user",
                    "content": USER.format({"text": text}),
                },
            ],
            response_model=DocumentClass,
        )
        classification = response.classification.value

        logger.info(f"Financial document classification: {classification}")

        return classification
