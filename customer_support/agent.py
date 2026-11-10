
from google.adk.agents import LlmAgent

# Banco de dados simulado
ORDERS_DB = {
    "ORD123": {
        "status": "shipped",
        "total": 99.99,
        "customer": "john@email.com"
    },
    "ORD456": {
        "status": "processing",
        "total": 149.99,
        "customer": "jane@email.com"
    },
    "ORD789": {
        "status": "delivered",
        "total": 249.99,
        "customer": "bob@email.com"
    },
}


# Ferramenta 1: verificar o status do pedido
def check_order_status(order_id: str) -> dict:
    """Verifica o status atual do pedido de um cliente.

    Use esta opção quando um cliente perguntar sobre o status do pedido
    ou da entrega.

    Args:
        order_id (str): O código do pedido (ex: "ORD123").

    Returns:
        dict: Informações sobre o status do pedido.

        Em caso de sucesso:
        {'status': 'success', 'order_status': '...', 'details': {...}}

        Em caso de erro:
        {'status': 'error', 'error_type': 'not_found'/'invalid_format'}
    """

    # Validar formato
    if not order_id.startswith("ORD"):
        return {
            "status": "error",
            "error_type": "invalid_format",
            "error_message": (
                "Os códigos dos pedidos precisam começar com 'ORD' "
                "(ex: ORD123)"
            )
        }

    # Pesquisar pedido
    if order_id not in ORDERS_DB:
        return {
            "status": "error",
            "error_type": "not_found",
            "error_message": f"Pedido {order_id} não encontrado no sistema"
        }

    # Sucesso
    order = ORDERS_DB[order_id]

    return {
        "status": "success",
        "order_id": order_id,
        "order_status": order["status"],
        "details": order
    }


# Ferramenta 2: processar reembolso
def process_refund(order_id: str, reason: str) -> dict:
    """Processa um pedido de reembolso para um pedido.

    Utilize essa opção SOMENTE após verificar se o pedido existe
    com check_order_status.

    Args:
        order_id (str): O código do pedido a ser reembolsado.
        reason (str): Motivo pelo qual o cliente solicitou o reembolso.

    Returns:
        dict: Resultado do processamento do reembolso.

        Em caso de sucesso:
        {'status': 'success', 'refund_amount': X, 'reference': 'REF###'}

        Em caso de erro:
        {'status': 'error', 'error_type': 'order_not_found'/'cannot_refund'}
    """

    # Verificar se o pedido existe
    if order_id not in ORDERS_DB:
        return {
            "status": "error",
            "error_type": "order_not_found",
            "error_message": (
                f"Não é possível processar o reembolso. "
                f"O pedido {order_id} não foi encontrado"
            )
        }

    order = ORDERS_DB[order_id]

    # Verificar se o pedido se qualifica para reembolso
    if order["status"] == "delivered":

        # Simular reembolso concluído
        return {
            "status": "success",
            "refund_amount": order["total"],
            "reference": f"REF{order_id[3:]}",
            "estimated_days": 5,
            "message": "Reembolso processado com sucesso"
        }

    else:
        # Não é possível reembolsar pedidos ainda não entregues
        return {
            "status": "error",
            "error_type": "cannot_refund",
            "error_message": (
                f"Não é possível reembolsar o pedido com o status "
                f"'{order['status']}'. Apenas pedidos entregues "
                "podem ser reembolsados."
            )
        }


# Ferramenta 3: encaminhar ao supervisor
def escalate_to_supervisor(issue_summary: str, order_id: str) -> dict:
    """Encaminha questões complexas para um supervisor humano.

    Use esta opção quando não conseguir resolver o problema do cliente
    com as ferramentas disponíveis ou quando o cliente pedir
    explicitamente para falar com um supervisor.

    Args:
        issue_summary (str): Breve resumo do problema (1-2 frases).
        order_id (str): Código do pedido mencionado, se aplicável.

    Returns:
        dict: Confirmação de encaminhamento para um supervisor.

        Sempre retorna:
        {'status': 'success', 'ticket_id': 'TICKET###'}
    """

    # Gerar ID do tíquete
    ticket_id = f"TICKET{hash(issue_summary) % 10000:04d}"

    return {
        "status": "success",
        "ticket_id": ticket_id,
        "message": "Problema encaminhado ao supervisor",
        "estimated_response": "dentro de 2 horas",
        "order_id": order_id if order_id else "N/A"
    }


# Criar agente de suporte ao cliente com instruções estratégicas
root_agent = LlmAgent(
    model="gemini-3.8-flash",
    name="customer_support_agent",
    description=(
        "Lida com consultas de clientes sobre pedidos e reembolsos "
        "com tratamento de erros abrangente."
    ),
    instruction="""
    Você é um agente de suporte ao cliente prestativo e empático
    para uma empresa de e-commerce.

    # Suas capacidades

    Você tem três ferramentas disponíveis:

    1. check_order_status(order_id) — Verifica o status de um pedido.
    2. process_refund(order_id, reason) — Processa solicitações de reembolso.
    3. escalate_to_supervisor(issue_summary, order_id) — Escala problemas
       complexos para um supervisor.

    # Diretrizes de fluxo de trabalho

    ## Para consultas sobre o status do pedido:

    1. Cumprimente o cliente cordialmente.
    2. Use check_order_status com o código do pedido fornecido.
    3. Aja conforme o resultado:

       - Se status='success': forneça uma atualização de status clara
         com detalhes.
       - Se error_type='not_found': peça educadamente ao cliente que
         verifique o código do pedido.
       - Se error_type='invalid_format': explique que os códigos dos
         pedidos começam com "ORD" (exemplo: ORD123).

    ## Para pedidos de reembolso:

    1. Demonstre empatia pela situação do cliente.
    2. PRIMEIRO, use check_order_status para verificar se o pedido existe.
    3. Se o pedido não for encontrado, não será possível prosseguir
       com o reembolso. Peça ao cliente para verificar o código do pedido.
    4. Se o pedido existir, use process_refund com order_id e o motivo
       (reason) do pedido do cliente.
    5. Aja conforme o resultado do reembolso:

       - Se status='success': confirme o reembolso com o número de
         referência, o valor e o prazo.
       - Se error_type='cannot_refund': explique o motivo (status do pedido)
         e ofereça alternativas ou encaminhamento para instâncias superiores.
       - Se error_type='order_not_found': isso não deveria acontecer se
         o passo 2 tivesse ocorrido com sucesso, mas peça desculpas e verifique.

    ## Estratégia de solução de erros:

    Para erros 'not_found':

    - Peça ao cliente para verificar novamente o código do pedido.
    - Ofereça-se para pesquisar pelo e-mail, caso eles tenham essa opção.
    - Seja paciente e prestativo.

    Para erros 'invalid_format':

    - Explique educadamente o formato correto: "ORD" seguido de números.
    - Forneça um exemplo: ORD123.
    - Peça para fornecer o código do pedido no formato correto.

    Para erros 'cannot_refund':

    - Explique a política claramente (apenas pedidos entregues podem
      ser reembolsados).
    - Demonstre empatia pela frustração do cliente.
    - Ofereça-se para encaminhar o caso ao supervisor se ele quiser
      uma exceção.

    ## Quando escalar um caso para um supervisor:

    Use escalate_to_supervisor quando:

    - O cliente estiver frustrado ou irritado e solicitar um supervisor.
    - O problema não puder ser resolvido com as ferramentas disponíveis.
    - O cliente solicitar uma exceção à política.
    - Várias tentativas com a ferramenta tiverem falhado.
    - O cliente solicitar especificamente falar com um gerente.

    Após o encaminhamento para um supervisor:

    - Forneça o número do tíquete.
    - Informe o tempo de resposta esperado.
    - Agradeça pela paciência.

    # Estilo de comunicação

    - Aja sempre com educação, profissionalismo e empatia.
    - Use o nome do cliente, se souber.
    - Forneça as próximas etapas de forma clara.
    - Reconheça os sentimentos deles (frustração, preocupação).
    - Agradeça pela paciência.
    - Nunca faça promessas que não possa cumprir.
    """,
    tools=[
        check_order_status,
        process_refund,
        escalate_to_supervisor
    ]
)
