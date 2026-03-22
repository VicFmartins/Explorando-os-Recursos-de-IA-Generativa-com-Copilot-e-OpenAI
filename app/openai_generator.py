from __future__ import annotations

import json
import os

import httpx

from app.models import StartupPackRequest, StartupPackResponse


SYSTEM_PROMPT = """You generate concise startup-planning assets in Brazilian Portuguese.
Return valid JSON with keys:
company_names, executive_summary, market_opportunity, pitch_outline, investor_email, logo_prompt.
company_names must be an array of 3 names.
pitch_outline must be an array of 5 bullet strings.
Do not wrap the JSON in markdown fences."""


class OpenAIStartupPackGenerator:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    @property
    def configured(self) -> bool:
        return bool(self.api_key)

    def generate(self, request: StartupPackRequest) -> StartupPackResponse:
        if not self.configured:
            raise RuntimeError("OPENAI_API_KEY nao configurada.")

        response = httpx.post(
            "https://api.openai.com/v1/responses",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "input": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": (
                            f"Ideia de negocio: {request.business_idea}\n"
                            f"Publico: {request.audience}\n"
                            f"Regiao: {request.region}\n"
                            f"Tom: {request.tone}\n"
                            "Gere um startup pack objetivo."
                        ),
                    },
                ],
            },
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        text = payload.get("output_text", "").strip()
        data = json.loads(text)
        return StartupPackResponse(
            provider="openai_responses_api",
            company_names=data["company_names"],
            executive_summary=data["executive_summary"],
            market_opportunity=data["market_opportunity"],
            pitch_outline=data["pitch_outline"],
            investor_email=data["investor_email"],
            logo_prompt=data["logo_prompt"],
            warning=None,
        )
