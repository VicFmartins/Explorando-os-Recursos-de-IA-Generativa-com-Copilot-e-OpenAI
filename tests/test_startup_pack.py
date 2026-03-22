from fastapi.testclient import TestClient

from app.fallback_generator import generate_startup_pack_locally
from app.main import app
from app.models import StartupPackRequest


client = TestClient(app)


def test_local_generator_returns_structured_pack() -> None:
    request = StartupPackRequest(
        business_idea="Uma plataforma de limpeza corporativa com IA para agendamento, atendimento e previsao de demanda."
    )
    result = generate_startup_pack_locally(request)

    assert result.provider == "local_template"
    assert len(result.company_names) == 3
    assert len(result.pitch_outline) == 5
    assert "solucao" in result.executive_summary.lower()


def test_api_returns_fallback_payload_when_no_key() -> None:
    response = client.post(
        "/api/startup-pack",
        json={
            "business_idea": "Uma startup que usa IA para criar planos de negocio e pitch decks para pequenas empresas.",
            "audience": "PMEs",
            "region": "Brasil",
            "tone": "profissional",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["provider"] in {"local_template", "openai_responses_api"}
    assert len(payload["company_names"]) == 3
    assert len(payload["pitch_outline"]) == 5
