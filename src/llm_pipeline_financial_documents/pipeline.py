from litellm import completion
from llm_pipeline_financial_documents.config import configure
from llm_pipeline_financial_documents.prompt import Prompt
from llm_pipeline_financial_documents.models import NotaFiscalDeServico

configure()

SYSTEM = Prompt.from_yaml("prompts/nota_fiscal_de_servico/system.yaml")

USER = Prompt.from_yaml("prompts/nota_fiscal_de_servico/user.yaml")

with open("documents/nota_fiscal_de_servico.txt", "r") as f:
    nfs = f.read()

response = completion(
    model="lm_studio/meta-llama-3.1-8b-instruct",
    messages=[
        {
            "role": "system",
            "content": SYSTEM.format({})
        },
        {
            "role": "user",
            "content": USER.format({"document": nfs}),
        }
    ],
    response_format=NotaFiscalDeServico,
)

print(response.choices[0].message.content)