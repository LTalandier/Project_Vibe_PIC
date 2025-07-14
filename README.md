# VibePIC

A conversational AI front-end for photonic integrated circuit (PIC) design using gdsfactory.

## Setup

Install dependencies:
```
pip install -r requirements.txt
```

## LLM Setup

To use the LLM features:
1. Sign up for a free Hugging Face account at https://huggingface.co/.
2. Generate an API token in your settings.
3. Set it as an environment variable: `export HUGGINGFACE_API_KEY=your_token_here` (or use `set` on Windows).

This enables open-source LLM integration with Mistral via Hugging Face.

## Usage

Run the example:
```
python examples/01_create_mzi.py
```

This will generate and display a standard Mach-Zehnder Interferometer based on the prompt.

For more advanced usage, extend the `design` method in `vibepic/main.py` with LLM integration. 