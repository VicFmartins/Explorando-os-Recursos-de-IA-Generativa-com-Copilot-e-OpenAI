# Explorando IA Generativa com Copilot e OpenAI

## O que o projeto entrega

- API REST em FastAPI
- geracao de startup pack a partir de uma ideia
- integracao opcional com a OpenAI API
- modo local de fallback para demonstracao sem chave
- instrucoes de repositorio para Copilot
- exemplos de payload e workflow
- testes automatizados

## Endpoints

### `GET /health`

Retorna o status da API.

### `POST /api/startup-pack`

Recebe uma ideia e devolve materiais iniciais de negocio.

Exemplo de payload:

```json
{
  "business_idea": "Uma startup que usa IA generativa para transformar uma ideia inicial em plano de negocio, pitch deck, email para investidor e proposta visual.",
  "audience": "fundadores em fase inicial",
  "region": "Brasil",
  "tone": "profissional"
}
```

## Como executar localmente

### Com Python

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Com Docker

```bash
docker build -t copilot-openai-genai .
docker run -p 8000:8000 copilot-openai-genai
```

## OpenAI

Se `OPENAI_API_KEY` estiver configurada, a API usa a OpenAI Responses API.

Base de ambiente em [.env.example](.env.example).

Se a chave nao estiver configurada, o projeto continua funcionando em modo local de demonstracao com templates.

## Copilot

Tambem deixei instrucoes de repositorio em [.github/copilot-instructions.md](.github/copilot-instructions.md), para orientar o uso do GitHub Copilot em tarefas como:

- expandir ideia de negocio
- revisar pitch
- transformar o pack em slides
- ajustar linguagem para investidores

## Estrutura do projeto

- `app/main.py`: endpoints da API
- `app/openai_generator.py`: integracao com OpenAI Responses API
- `app/fallback_generator.py`: fallback local sem API key
- `app/models.py`: contratos da API
- `docs/workflow.md`: fluxo combinado Copilot + OpenAI
- `examples/sample-request.json`: payload pronto para teste
- `.github/copilot-instructions.md`: instrucoes de repositorio para Copilot

## Referencias oficiais

Para alinhar o projeto com a documentacao atual da OpenAI, usei como base referencias oficiais:

- [OpenAI API FAQ](https://platform.openai.com/docs/faq/should-i-use-chatgpt-or-the-api)
- [Responses API guide](https://platform.openai.com/docs/guides/responses)
- [Text generation guide](https://platform.openai.com/docs/guides/text)

Pela documentacao oficial atual, a OpenAI recomenda em geral comecar por `gpt-4o` ou `gpt-4o-mini`; por isso o projeto usa `gpt-4o-mini` como padrao em [.env.example](.env.example).

## Validacao

```bash
pytest
```

Os testes cobrem:

- geracao estruturada no fallback local
- resposta do endpoint principal
