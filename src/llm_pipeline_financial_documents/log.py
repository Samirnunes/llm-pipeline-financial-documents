import sys
from logging import StreamHandler, getLogger

logger = getLogger("llm-pipeline-financial-documents")
logger.setLevel("INFO")
logger.addHandler(StreamHandler(sys.stdout))
