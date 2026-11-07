from orchestrator import Settings, SuggestionContext, SuggestionPayload, build_suggestions

_settings = Settings(model="fake-model")

async def get_suggestions(record_id: str, text: str) -> SuggestionPayload:
    ctx = SuggestionContext(record_id=record_id, text=text)
    return await build_suggestions(ctx, settings=_settings)
