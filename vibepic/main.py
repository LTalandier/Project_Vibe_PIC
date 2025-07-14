from vibepic.core import VibePIC
import traceback
import os
from rich import print
from rich.prompt import Prompt

def main():
    """Main function to run the VibePIC interactive tool."""
    designer = VibePIC()
    print("[bold cyan]Welcome to VibePIC - Your Photonic IC Design Assistant![/bold cyan]")
    print("Start by creating a new component (e.g., 'create a straight waveguide').")
    print("Then, modify it with commands like 'make it longer' or 'change the width'.")
    print("Type 'new' to start over, or 'exit'/'quit' to end.")

    is_first_prompt = True

    while True:
        prompt = Prompt.ask("[bold yellow]VibePIC[/bold yellow]")

        if prompt.lower() in ["exit", "quit"]:
            print("[bold cyan]Goodbye![/bold cyan]")
            break
        
        if prompt.lower() == 'new':
            designer = VibePIC()
            is_first_prompt = True
            print("[bold cyan]Starting a new design.[/bold cyan]")
            continue

        try:
            # Determine if it's a modification or a new design
            # For now, we treat the first prompt as creation, and subsequent ones as modifications.
            is_modification = not is_first_prompt
            component = designer.design(prompt, is_modification=is_modification)
            is_first_prompt = False
            
            # Suggest a filename based on the component name
            sanitized_name = component.name.replace('<', '').replace('>', '').replace(':', '_')
            output_gds = f"{sanitized_name}.gds"
            output_png = f"{sanitized_name}.png"

            component.write_gds(output_gds)
            print(f"[bold green]Success! Component saved to '{os.path.abspath(output_gds)}'[/bold green]")
            
            # Add visualization
            fig = component.plot(return_fig=True)
            if fig:
                fig.savefig(output_png, dpi=300)
                print(f"[bold green]Image of component saved to '{os.path.abspath(output_png)}'[/bold green]")

        except Exception as e:
            print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
            traceback.print_exc()

if __name__ == "__main__":
    main() 