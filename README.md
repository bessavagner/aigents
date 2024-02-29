# aigents

Adapters for Large Language Models and Generative Pre-trained Transformers APIs

## Installation

```bash
$ poetry install
```

## Usage - Classes

### OpenAIChatter

The `OpenAIChatter` class is a synchronous OpenAI-based chatbot. It inherits from the `OpenAIChatterMixin` and `BaseChatter` classes.

**Constructor:**

```python
def __init__(self,
             *args,
             setup: str = None,
             api_key: str = None,
             organization: str = None,
             temperature: float = 0.0,
             model: str = MODELS[0],
             **kwargs):
```

**Parameters:**

* `*args`: Arguments for the `__configure` method.
* `setup`: Text for setting up a model's or assistant's role.
* `api_key`: OpenAI API key for authentication.
* `organization`: Unique identifier for your organization.
* `temperature`: The sampling temperature, between 0 and 1.
* `model`: Model string identification.
* `**kwargs`: Keyword arguments for the `__configure` method.

**Methods:**

* `answer`: Generate a response to the given prompt.

### AsyncOpenAIChatter

The `AsyncOpenAIChatter` class is an asynchronous OpenAI-based chatbot. It inherits from the `OpenAIChatterMixin` and `BaseChatter` classes.

**Constructor:**

```python
def __init__(self,
             *args,
             setup: str = None,
             api_key: str = None,
             organization: str = None,
             temperature: float = 0.0,
             model: str = MODELS[0],
             **kwargs):
```

**Parameters:**

* `*args`: Arguments for the `__configure` method.
* `setup`: Text for setting up a model's or assistant's role.
* `api_key`: OpenAI API key for authentication.
* `organization`: Unique identifier for your organization.
* `temperature`: The sampling temperature, between 0 and 1.
* `model`: Model string identification.
* `**kwargs`: Keyword arguments for the `__configure` method.

**Methods:**

* `answer`: Generate a response to the given prompt.

### GoogleChatter

The `GoogleChatter` class is a synchronous Google-based chatbot. It inherits from the `GoogleChatterMixin` and `BaseChatter` classes.

**Constructor:**

```python
def __init__(self,
             *args,
             setup: str = None,
             api_key: str = None,
             temperature: float = 0.0,
             **kwargs):
```

**Parameters:**

* `*args`: Arguments for the `__configure` method.
* `setup`: Text for setting up a model's or assistant's role.
* `api_key`: Google AI API key for authentication.
* `temperature`: The sampling temperature, between 0 and 1.
* `**kwargs`: Keyword arguments for the `__configure` method.

**Methods:**

* `answer`: Generate a response to the given prompt.

### AsyncGoogleChatter

The `AsyncGoogleChatter` class is an asynchronous Google-based chatbot. It inherits from the `GoogleChatter` class.

**Constructor:**

```python
def __init__(self,
             *args,
             setup: str = None,
             api_key: str = None,
             temperature: float = 0.0,
             **kwargs):
```

**Parameters:**

* `*args`: Arguments for the `__configure` method.
* `setup`: Text for setting up a model's or assistant's role.
* `api_key`: Google AI API key for authentication.
* `temperature`: The sampling temperature, between 0 and 1.
* `**kwargs`: Keyword arguments for the `__configure` method.

**Methods:**

* `answer`: Generate a response to the given prompt.


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`aigents` was created by Vagner Bessa. Vagner Bessa retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.

## Credits

`aigents` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
