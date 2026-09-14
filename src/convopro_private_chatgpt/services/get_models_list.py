from typing import List

from convopro_private_chatgpt.config.settings import settings


def get_openai_models_list() -> List[str]:
    """Returns the configured list of selectable OpenAI models (comma-separated in .env)."""
    models_list = settings.OPENAI_MODELS  # str data type from .env file
    openai_models = [model.strip() for model in models_list.split(",") if model.strip()]
    return openai_models


# Example usage
# check_openai_models = get_openai_models_list()
# print(type(check_openai_models))   # <class 'list'>
# print(check_openai_models)         # ['gpt-4o-mini', 'gpt-4o']
