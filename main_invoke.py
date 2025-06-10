import yaml  # type: ignore

from llm_pipeline_financial_documents import FinancialDocumentsPipeline

document_name = "nota_fiscal_de_servico.txt"
document_without_extension = document_name.split(".")[0]

pipeline = FinancialDocumentsPipeline()

result = pipeline.invoke("./documents/" + document_name)

with open(f"result-{document_without_extension}.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(result, f, allow_unicode=True, default_flow_style=False)
