from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# Etapa 1: definir a estrutura de saída com Pydantic
class ProductInfo(BaseModel):
    product_name: str = Field(description="O nome completo do produto")
    price: float = Field(description="O preço em USD")
    storage: str = Field(description="Capacidade de armazenamento (ex. '256 GB')")
    color: str = Field(
        default="Não especificado",
        description="Cor do produto, se mencionada",
    )

# Etapa 2: criar o agente com output_schema
root_agent = LlmAgent(
    model="gemini-3.8-flash",
    name="product_extractor",
    description=(
        "Extrai informações do produto das mensagens dos usuários e retorna um "
        "JSON estruturado"
    ),
    instruction="""Você é um extrator de informações do produto.
Sua tarefa: - Ler a mensagem do usuário sobre um produto - Extrair: product_name, price, storage e color (se mencionada) - Responder APENAS com JSON válido que corresponda a este formato:
{
    "product_name": "nome do produto aqui",
    "price": 999.99,
    "storage": "256GB",
    "color": "Space Black"
}
Regras: - o preço precisa ser um número (sem cifrões) - o armazenamento precisa incluir a unidade (GB, TB) - se a cor não for mencionada, use "Não especificado" - APENAS a saída JSON, sem texto explicativo""",
    output_schema=ProductInfo,  # Aplicar esta estrutura exata
    output_key="extracted_product",  # Armazenar o resultado no estado da sessão
)