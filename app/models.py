from pydantic import BaseModel, Field


class StartupPackRequest(BaseModel):
    business_idea: str = Field(min_length=10)
    audience: str = Field(default="pequenas e medias empresas")
    region: str = Field(default="Brasil")
    tone: str = Field(default="profissional")


class StartupPackResponse(BaseModel):
    provider: str
    company_names: list[str]
    executive_summary: str
    market_opportunity: str
    pitch_outline: list[str]
    investor_email: str
    logo_prompt: str
    warning: str | None = None
