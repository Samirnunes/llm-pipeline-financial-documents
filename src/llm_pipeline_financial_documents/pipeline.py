from typing import Dict

from .assistants import FinancialDocumentClassifier, FinancialDocumentExtractor
from .config import configure
from .log import logger
from .tools import OCR


class FinancialDocumentsPipeline:
    def __init__(self) -> None:
        configure()
        self._ocr = OCR()
        self._classifier = FinancialDocumentClassifier()
        self._extractor = FinancialDocumentExtractor()

    def invoke(self, file_path: str) -> Dict:
        logger.info(f"Running {self.__class__.__name__}...")
        text = self._ocr.invoke(file_path)
        classification = self._classifier.invoke(text)
        return self._extractor.invoke(text, classification)
