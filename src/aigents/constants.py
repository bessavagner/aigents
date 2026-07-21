"""
    context_chat.agents.constants

Constants for module agents. Some are used in other modules.
Most constants comes from OpenAI documentation. See:
https://platform.openai.com/docs/models
"""

MODELS = (
    'gpt-3.5-turbo-0125',
    'gpt-3.5-turbo-1106',
    'gpt-4-turbo-preview',
    'gpt-4o-mini',  # 3
    'gpt-5.6',
    'gpt-4o-mini-search-preview',
    'gpt-4-vision-preview',
    'gemini-2.5-flash',  # Google # 7
    'gemini-2.5-flash-lite',  # Google # 8
    'gemini-1.5-pro',  # Google # 9
    'gemini-1.5-flash',
    'gemini-1.5-flash-8b',
    'deepseek-v4-flash',
    'deepseek-v4-pro'
)

MAX_TOKENS = (
    (MODELS[0], 16385),
    (MODELS[1], 16385),
    (MODELS[2], 8192),
    (MODELS[3], 128000),
    (MODELS[4], 1050000),
    (MODELS[5], 128000),
    (MODELS[6], 128000),
    (MODELS[7], 1048576),
    (MODELS[8], 1048576),
    (MODELS[9], 2097152),
    (MODELS[10], 1048576),
    (MODELS[11], 1048576),
    (MODELS[12], 1000000),
    (MODELS[13], 1000000),
)

ROLES = (  # roles for messages objects
    'system',
    'user',
    'assistant',
    'model'  # Google gemini
)  # see https://platform.openai.com/docs/guides/gpt/chat-completions-api

"""Constants for embeddings operations"""

MODELS_EMBEDDING = (
    'text-embedding-3-small',
    'text-embedding-3-large',
    'text-embedding-ada-002',
    'models/embedding-001',
    'models/text-embedding-004',
)

TOKENIZER = (
    'cl100k_base',
)

EMBEDDINGS_COLUMNS = ('chunks', 'n_tokens', 'embeddings',)
