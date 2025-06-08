from llm_pipeline_financial_documents import FinancialDocumentsPipeline

pipeline = FinancialDocumentsPipeline()

pipeline.invoke("./documents/nota_fiscal_de_servico.pdf")
