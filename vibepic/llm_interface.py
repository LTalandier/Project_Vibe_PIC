import ollama
from typing import Any


def generate_component_code(prompt: str, pdk_name: str = "generic") -> str:
    """Send prompt to a local Ollama model and get back Python code for gdsfactory component."""
    
    system_prompt = f"You are an expert assistant for the '{pdk_name}' gdsfactory PDK. You generate Python code for gdsfactory components. Your responses must contain only the raw Python code, without any explanations, comments, or markdown formatting."
    
    # More detailed instructions to guide the model.
    user_prompt = f"""Generate Python code that creates a gdsfactory component for: '{prompt}'.

IMPORTANT INSTRUCTIONS:
1.  Your code MUST import gdsfactory as gf.
2.  You MUST use components and layers available in the '{pdk_name}' PDK.
3.  Pay close attention to the keyword arguments for the gdsfactory functions. They are very specific. For instance, `gf.components.mzi` accepts arguments like `delta_length`, `length_y`, and `length_x`. It does NOT accept a generic `length` argument.
4.  The final gdsfactory.Component object MUST be assigned to a variable named 'component'.
5.  The code should be a direct script. Do NOT define a function.
6.  Your output MUST be ONLY the raw Python code, enclosed in ```python ... ```.

Example of the required output format for a simple straight component:
```python
import gdsfactory as gf

component = gf.components.straight(length=10, width=0.5)
```"""

    response = ollama.chat(
        model='codellama',
        messages=[
            {
                'role': 'system',
                'content': system_prompt,
            },
            {
                'role': 'user',
                'content': user_prompt,
            },
        ],
    )
    return response['message']['content'].strip()


def create_component_from_code(code: str) -> Any:
    """Safely execute the generated code to create a gdsfactory Component."""
    local_vars = {}
    # Clean up the code string if it's wrapped in markdown
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0]
    elif "```" in code:
        code = code.split("```")[1].split("```")[0]

    exec(code, {"gf": __import__('gdsfactory')}, local_vars)
    # Assume the code defines a variable 'component' or returns it
    return local_vars.get('component'), code


def generate_modified_code(previous_code: str, prompt: str, pdk_name: str = "generic") -> str:
    """Send a prompt to Ollama to modify existing gdsfactory code."""
    system_prompt = f"You are an expert assistant for the '{pdk_name}' gdsfactory PDK. You modify Python code for gdsfactory components. Your responses must contain only the raw Python code, without any explanations, comments, or markdown formatting."

    user_prompt = f"""Given the following Python code for a gdsfactory component from the '{pdk_name}' PDK:
```python
{previous_code}
```

Please modify it according to the following instruction: '{prompt}'.

IMPORTANT INSTRUCTIONS:
1.  Your output MUST be the complete, modified Python code, making sure it's compatible with the '{pdk_name}' PDK.
2.  Do NOT just return a snippet. Return the full script required to generate the component.
3.  The final gdsfactory.Component object MUST be assigned to a variable named 'component'.
4.  Your output MUST be ONLY the raw Python code, enclosed in ```python ... ```.
"""

    response = ollama.chat(
        model='codellama',
        messages=[
            {
                'role': 'system',
                'content': system_prompt,
            },
            {
                'role': 'user',
                'content': user_prompt,
            },
        ],
    )
    return response['message']['content'].strip() 