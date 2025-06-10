import os
import tempfile

import pytesseract
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
from PIL import Image

from ..log import logger


class OCR:
    def __init__(self) -> None:
        """
        Initializes the OCR processor.
        """
        pass

    def invoke(self, image_path: str) -> str:
        """
        Extracts text from an image or PDF file using Tesseract OCR.

        Args:
            file_path: The path to the image or PDF file.

        Returns:
            The extracted text as a string.
        """
        logger.info(f"Running {self.__class__.__name__} for file: {image_path}")

        try:
            file_extension = os.path.splitext(image_path)[1].lower()

            if file_extension == ".pdf":
                logger.info("PDF file detected. Converting to image...")
                with tempfile.TemporaryDirectory() as temp_dir:
                    try:
                        images_from_path = convert_from_path(
                            image_path, output_folder=temp_dir, fmt="png"
                        )
                    except (
                        PDFInfoNotInstalledError,
                        PDFPageCountError,
                        PDFSyntaxError,
                    ) as e:
                        logger.error(f"Error converting PDF: {e}")
                        return f"Error converting PDF: {e}"
                    except Exception as e:
                        logger.error(
                            f"An unexpected error occurred during PDF conversion: {e}"
                        )
                        return f"An unexpected error occurred during PDF conversion: {e}"

                    if not images_from_path:
                        logger.error("PDF conversion resulted in no images.")
                        return "Error: PDF conversion resulted in no images."

                    text = "\n\n".join(
                        [
                            pytesseract.image_to_string(img, lang="por")
                            for img in images_from_path
                        ]
                    )

            elif file_extension in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
                logger.info(f"Image file detected: {image_path}")
                img = Image.open(image_path)
                text = pytesseract.image_to_string(img, lang="por")
            else:
                logger.error(f"Unsupported file type: {file_extension}")
                return f"Error: Unsupported file type: {file_extension}. Please use PDF, PNG, JPG, JPEG, BMP, or TIFF."

            logger.info(f"Text extracted from document:\n\n{text[:500]}...")

            return text
        except FileNotFoundError:
            logger.error(f"File not found: {image_path}")
            return "Error: File not found."
        except pytesseract.TesseractNotFoundError:
            logger.error("Tesseract is not installed or not in your PATH.")
            return "Error: Tesseract is not installed or not in your PATH."
        except Exception as e:
            logger.error(f"Error processing file {image_path}: {e}", exc_info=True)
            return f"Error processing file: {e}"
