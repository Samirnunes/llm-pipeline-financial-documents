from typing import Dict

from tenacity import retry, stop_after_attempt, wait_fixed

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

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(2))
    def invoke(self, file_path: str) -> Dict:
        logger.info(f"Running {self.__class__.__name__}...")
        text = self._ocr.invoke(file_path)
        classification = self._classifier.invoke(text)
        return self._extractor.invoke(text, classification)
