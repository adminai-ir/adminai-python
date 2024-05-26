# Shared Types

```python
from adminai.types import ErrorObject, FunctionDefinition, FunctionParameters
```

# Completions

Types:

```python
from adminai.types import CompletionUsage
```

# Chat

## Completions

Types:

```python
from adminai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionContentPart,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartText,
    ChatCompletionFunctionCallOption,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionNamedToolChoice,
    ChatCompletionRole,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionTool,
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)
```

Methods:

- <code title="post /openai/v1/chat/completions">client.chat.completions.<a href="./src/adminai/resources/chat/completions.py">create</a>(\*\*<a href="src/adminai/types/chat/completion_create_params.py">params</a>) -> <a href="./src/adminai/types/chat/chat_completion.py">ChatCompletion</a></code>

# Embeddings

Types:

```python
from adminai.types import CreateEmbeddingResponse, Embedding
```

Methods:

- <code title="post /openai/v1/embeddings">client.embeddings.<a href="./src/adminai/resources/embeddings.py">create</a>(\*\*<a href="src/adminai/types/embedding_create_params.py">params</a>) -> <a href="./src/adminai/types/create_embedding_response.py">CreateEmbeddingResponse</a></code>

# Audio

## Transcriptions

Types:

```python
from adminai.types.audio import Transcription, TranscriptionCreateResponse
```

Methods:

- <code title="post /openai/v1/audio/transcriptions">client.audio.transcriptions.<a href="./src/adminai/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/adminai/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/adminai/types/audio/transcription_create_response.py">TranscriptionCreateResponse</a></code>

## Translations

Types:

```python
from adminai.types.audio import Translation, TranslationCreateResponse
```

Methods:

- <code title="post /openai/v1/audio/translations">client.audio.translations.<a href="./src/adminai/resources/audio/translations.py">create</a>(\*\*<a href="src/adminai/types/audio/translation_create_params.py">params</a>) -> <a href="./src/adminai/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

# Models

Types:

```python
from adminai.types import Model, ModelDeleted, ModelListResponse
```

Methods:

- <code title="get /openai/v1/models/{model}">client.models.<a href="./src/adminai/resources/models.py">retrieve</a>(model) -> <a href="./src/adminai/types/model.py">Model</a></code>
- <code title="get /openai/v1/models">client.models.<a href="./src/adminai/resources/models.py">list</a>() -> <a href="./src/adminai/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /openai/v1/models/{model}">client.models.<a href="./src/adminai/resources/models.py">delete</a>(model) -> <a href="./src/adminai/types/model_deleted.py">ModelDeleted</a></code>
