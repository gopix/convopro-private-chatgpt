from openai import OpenAI

from convopro_private_chatgpt.config.settings import settings

_current_model_name: str | None = None  # cache key -- which model the cached client was built for
_current_llm_instance: OpenAI | None = None  # cached client -- rebuilt only when the model changes


def get_llm(model_name: str = settings.OPENAI_MODEL) -> OpenAI:
    """Factory: returns a cached OpenAI client for model_name -- swap in other providers here later by model_name."""
    global _current_model_name, _current_llm_instance

    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance

    _current_llm_instance = OpenAI(api_key=settings.OPENAI_API_KEY)
    _current_model_name = model_name
    return _current_llm_instance


if __name__ == "__main__":
    model = settings.OPENAI_MODEL
    check_llm = get_llm(model)
    print(f"Model: {model}")
    print(check_llm)