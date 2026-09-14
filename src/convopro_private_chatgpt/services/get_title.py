from convopro_private_chatgpt.llm_factory.get_llm import get_llm

TITLE_PROMPT_TEMPLATE = (
    "You are a helpful assistant that generates short, clear, and catchy titles.\n\n"
    "Task:\n- Read the given user query.\n- Create a concise title (max 7 words).\n"
    "- The title should summarize the intent of the query.\n"
    "- Avoid unnecessary words, punctuation, or filler.\n"
    "- Keep it professional and easy to understand.\n\n"
    "User Query:\n{user_query}\n\n"
    "Output:\nTitle:"
)


def get_chat_title(model: str, user_query: str) -> str:
    """Generates a short, catchy title for a chat, given the first user query."""
    llm = get_llm(model)
    prompt = TITLE_PROMPT_TEMPLATE.format(user_query=user_query)
    response = llm.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


# Example usage
# model = "gpt-4o-mini"
# user_query = "Can you explain the concept of reinforcement learning and its applications in modern AI"
# title = get_chat_title(model, user_query)
# print(title)

# NOTE: smaller/cheaper models may give less accurate or longer titles than requested.
