from fastapi import FastAPI

from app.fallback_generator import generate_startup_pack_locally
from app.models import StartupPackRequest, StartupPackResponse
from app.openai_generator import OpenAIStartupPackGenerator


app = FastAPI(
    title="Copilot + OpenAI Startup Pack Demo",
    version="1.0.0",
    description="API para transformar uma ideia de negocio em materiais de pitch usando OpenAI, com fallback local para demonstracao.",
)

openai_generator = OpenAIStartupPackGenerator()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "copilot-openai-genai"}


@app.post("/api/startup-pack", response_model=StartupPackResponse)
def startup_pack(payload: StartupPackRequest) -> StartupPackResponse:
    if openai_generator.configured:
        return openai_generator.generate(payload)
    return generate_startup_pack_locally(payload)
