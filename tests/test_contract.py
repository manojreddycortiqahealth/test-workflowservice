import asyncio
from adapter import get_suggestions

def test_orchestrator_contract():
    payload = asyncio.run(get_suggestions("r-1", "hello"))
    assert payload.record_id == "r-1"
    assert payload.suggestions
    assert payload.suggestions[0].title
    assert payload.orchestrator_version
