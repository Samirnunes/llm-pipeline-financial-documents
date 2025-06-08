from llm_pipeline_financial_documents import FinancialDocumentsPipeline

pipeline = FinancialDocumentsPipeline()

pipeline.invoke("./documents/informe_de_rendimentos.pdf")
