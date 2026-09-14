from typing import Any, Dict, List

from convopro_private_chatgpt.llm_factory.get_llm import get_llm


def get_answer(model_name: str, chat_history: List[Dict[str, Any]]) -> str:
    """Gets a chat completion from OpenAI for model_name, given prior chat_history as [{"role", "content"}, ...]."""
    llm = get_llm(model_name)

    # Always prepend a system message
    messages = [{"role": "system", "content": "You are a helpful chat assistant."}]

    # Append the rest of the history -- strip extra keys (e.g. Mongo's "ts") the API doesn't accept
    messages.extend({"role": msg["role"], "content": msg["content"]} for msg in chat_history)

    response = llm.chat.completions.create(model=model_name, messages=messages)
    return response.choices[0].message.content


# example usage
# model_name = "gpt-4o-mini"
# chat_history = [
#     {"role": "user", "content": "What is Artificial Intelligence?"}
# ]
# response = get_answer(model_name, chat_history)
# print(response)
