from pydantic import BaseModel, Field


class NotaFiscalDeServico(BaseModel):
    # Identificação da NFS-e
    numero: str = Field(
        ...,
        description="O número sequencial único da Nota Fiscal de Serviço Eletrônica.",
    )
    data_hora_emissao: str = Field(
        ..., description="A data e hora exata em que a NFS-e foi emitida."
    )
    codigo_verificacao: str = Field(
        ...,
        description="O código alfanumérico usado para verificar a autenticidade da NFS-e junto à prefeitura.",
    )
    rps_substituido: str | None = Field(
        None,
        description="O número do Recibo Provisório de Serviços (RPS) que esta NFS-e está substituindo, se aplicável. Nulo se não houver RPS anterior.",
    )

    # Dados do Prestador de Serviços
    razao_social_prestador_de_servicos: str = Field(
        ...,
        description="A razão social completa da empresa ou profissional autônomo que prestou o serviço.",
    )
    nome_fantasia_prestador_de_servicos: str = Field(
        ...,
        description="O nome fantasia ou nome comercial do prestador de serviços, se houver.",
    )
    cnpj_prestador_de_servicos: str = Field(
        ...,
        description="O Cadastro Nacional de Pessoas Jurídicas (CNPJ) do prestador de serviços.",
    )
    inscricao_municipal_prestador: str = Field(
        ...,
        description="O número de inscrição municipal do prestador de serviços na prefeitura.",
    )
    endereco_prestador: str = Field(
        ...,
        description="O endereço completo do prestador (logradouro, número, complemento, bairro).",
    )
    cidade_prestador: str = Field(
        ..., description="A cidade onde o prestador de serviços está localizado."
    )
    uf_prestador: str = Field(
        ...,
        description="A Unidade Federativa (estado) onde o prestador de serviços está localizado.",
    )
    cep_prestador: str = Field(
        ...,
        description="O Código de Endereçamento Postal (CEP) do prestador de serviços.",
    )
    telefone_prestador: str = Field(
        ..., description="O telefone de contato do prestador de serviços."
    )
    email_prestador: str = Field(
        ..., description="O e-mail de contato do prestador de serviços."
    )

    # Dados do Tomador de Serviços
    razao_social_tomador_de_servicos: str = Field(
        ...,
        description="A razão social completa ou nome completo da pessoa jurídica/física que tomou (recebeu) o serviço.",
    )
    cnpj_ou_cpf_tomador_de_servicos: str = Field(
        ...,
        description="O CNPJ (para pessoa jurídica) ou CPF (para pessoa física) do tomador de serviços.",
    )
    endereco_tomador: str = Field(
        ...,
        description="O endereço completo do tomador (logradouro, número, complemento, bairro).",
    )
    cidade_tomador: str = Field(
        ..., description="A cidade onde o tomador de serviços está localizado."
    )
    uf_tomador: str = Field(
        ...,
        description="A Unidade Federativa (estado) onde o tomador de serviços está localizado.",
    )
    cep_tomador: str = Field(
        ...,
        description="O Código de Endereçamento Postal (CEP) do tomador de serviços.",
    )
    telefone_tomador: str = Field(
        ..., description="O telefone de contato do tomador de serviços."
    )
    email_tomador: str = Field(
        ..., description="O e-mail de contato do tomador de serviços."
    )

    # Detalhes dos Serviços
    codigo_servico: str = Field(
        ...,
        description="O código de identificação do tipo de serviço prestado, conforme lista de serviços municipal/nacional.",
    )
    detalhes_dos_servicos: str = Field(
        ..., description="Uma descrição detalhada dos serviços que foram prestados."
    )

    # Valores e Impostos
    valor_total_dos_servicos: float = Field(
        ..., description="O valor total bruto dos serviços prestados."
    )
    valor_deducoes: float = Field(
        ...,
        description="O valor de deduções sobre a base de cálculo, se aplicável (ex: materiais, subempreitadas).",
    )
    base_de_calculo_iss: float = Field(
        ...,
        description="O valor sobre o qual o Imposto Sobre Serviços (ISS) é calculado, após deduções.",
    )
    aliquota_iss: float = Field(
        ...,
        description="A alíquota percentual do ISS aplicada sobre a base de cálculo.",
    )
    valor_iss: float = Field(
        ..., description="O valor do Imposto Sobre Serviços (ISS) calculado."
    )
    valor_liquido: float = Field(
        ...,
        description="O valor final a ser pago pelo tomador, após todas as deduções e impostos (se não retido na fonte).",
    )

    imposto_retido_na_fonte: bool = Field(
        ...,
        description="Indica se o Imposto Sobre Serviços (ISS) foi retido na fonte pelo tomador. `True` se o imposto foi retido, `False` caso contrário.",
    )

    # Informações Adicionais
    observacoes: str = Field(
        ...,
        description="Campo para quaisquer observações adicionais relevantes para a nota fiscal, como condições de pagamento.",
    )
