from __future__ import annotations

import re

from app.models import StartupPackRequest, StartupPackResponse


def _slug_words(text: str) -> list[str]:
    return [word.capitalize() for word in re.findall(r"[a-zA-ZÀ-ÿ]{4,}", text)[:6]]


def generate_startup_pack_locally(request: StartupPackRequest) -> StartupPackResponse:
    words = _slug_words(request.business_idea)
    base = words[:3] or ["Nova", "Idea", "Lab"]
    names = [
        "".join(base[:2]),
        f"{base[0]}Flow" if base else "IdeaFlow",
        f"{base[0]}Hub" if base else "IdeaHub",
    ]

    summary = (
        f"A proposta cria uma solucao para {request.audience.lower()} em {request.region}, "
        f"transformando a ideia central em um servico mais simples, escalavel e facil de vender."
    )
    market = (
        f"Oportunidade de mercado baseada na dor descrita: {request.business_idea[:180]}. "
        "Existe espaco para diferenciar a oferta por especializacao, rapidez de atendimento e uso de IA generativa."
    )
    pitch = [
        "Problema do cliente e contexto atual",
        "Solucao proposta e diferencial competitivo",
        "Publico-alvo e tamanho da oportunidade",
        "Modelo de receita e aquisicao de clientes",
        "Roadmap inicial e uso de IA para ganhar eficiencia",
    ]
    investor_email = (
        "Assunto: Reuniao para apresentar oportunidade de negocio\n\n"
        "Ola,\n\n"
        f"Gostaria de apresentar uma iniciativa focada em {request.business_idea.lower()}.\n"
        "Estruturamos uma tese inicial de mercado, proposta de valor e um plano enxuto de execucao.\n\n"
        "Se fizer sentido, posso compartilhar um resumo executivo e marcar uma conversa breve nesta semana.\n\n"
        "Atenciosamente,\nSeu Nome"
    )
    logo_prompt = (
        f"Crie um conceito de logo {request.tone.lower()} para uma startup voltada a {request.business_idea.lower()}, "
        "com visual limpo, memoravel e apropriado para apresentacoes a investidores."
    )

    return StartupPackResponse(
        provider="local_template",
        company_names=names,
        executive_summary=summary,
        market_opportunity=market,
        pitch_outline=pitch,
        investor_email=investor_email,
        logo_prompt=logo_prompt,
        warning="Resultado gerado localmente para demonstracao. Configure OPENAI_API_KEY para usar a OpenAI API.",
    )
