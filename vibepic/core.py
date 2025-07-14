from rich import print
from .llm_interface import generate_component_code, create_component_from_code, generate_modified_code
from .pdk_handler import activate_pdk

class VibePIC:
    def __init__(self, pdk_name: str = "generic"):
        self.pdk_name = pdk_name
        self.component = None
        self.code = None
        activate_pdk(self.pdk_name)
        print(f"Activated PDK: [bold blue]{self.pdk_name}[/bold blue]")

    def design(self, prompt: str, is_modification: bool = False):
        print("[blue]Processing prompt with LLM...[/blue]")

        if is_modification and self.code:
            generated_code = generate_modified_code(self.code, prompt, pdk_name=self.pdk_name)
        else:
            generated_code = generate_component_code(prompt, pdk_name=self.pdk_name)

        print(f"[green]Generated code:[/green] {generated_code}")
        
        self.component, self.code = create_component_from_code(generated_code)
        
        if self.component is None:
            raise ValueError("Failed to generate component from prompt.")
        
        print("[bold green]Component generated successfully.[/bold green]")
        return self.component 