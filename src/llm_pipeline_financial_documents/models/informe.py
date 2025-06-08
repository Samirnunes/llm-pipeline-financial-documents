from pydantic import BaseModel, Field

class InformeDeRendimentos(BaseModel):
    ano_calendario: int = Field(
        ..., description="Ano-calendário a que se refere o informe de rendimentos."
    )

    # Fonte Pagadora (Empresa/Instituição)
    nome_empresarial_fonte_pagadora: str = Field(
        ..., description="Nome empresarial da fonte pagadora."
    )
    cnpj_fonte_pagadora: str = Field(..., description="CNPJ da fonte pagadora.")

    # Beneficiário (Pessoa Física)
    nome_completo_beneficiario: str = Field(
        ..., description="Nome completo do beneficiário dos rendimentos."
    )
    cpf_beneficiario: str = Field(
        ..., description="CPF do beneficiário dos rendimentos."
    )

    # Rendimentos Tributáveis
    total_rendimentos_tributaveis: float = Field(
        ...,
        description="Soma total dos rendimentos tributáveis recebidos (salários, pró-labore, etc.).",
    )
    contribuicao_previdenciaria_oficial: float = Field(
        ...,
        description="Valor da contribuição previdenciária oficial (INSS) deduzida.",
    )
    imposto_renda_retido_na_fonte_principal: float = Field(
        ...,
        description="Valor do Imposto de Renda Retido na Fonte (IRRF) sobre os rendimentos principais.",
    )

    # 13º Salário
    valor_13_salario: float = Field(..., description="Valor do 13º salário.")
    imposto_renda_retido_na_fonte_13_salario: float = Field(
        ...,
        description="Valor do Imposto de Renda Retido na Fonte (IRRF) sobre o 13º salário.",
    )

    # Rendimentos Isentos e Não Tributáveis (Exemplos)
    lucros_e_dividendos: float = Field(
        ..., description="Valor de lucros e dividendos recebidos, se aplicável."
    )
    indenizacoes_rescisao_ferias: float = Field(
        ...,
        description="Valor de indenizações por rescisão de contrato e férias indenizadas, se aplicável.",
    )
    outros_isentos_nao_tributaveis: float = Field(
        ...,
        description="Outros rendimentos isentos e não tributáveis (ex: poupança, doações), se aplicável.",
    )
