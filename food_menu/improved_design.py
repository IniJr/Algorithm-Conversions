from rich.console import Console
from rich.text import Text
from rich.panel import Panel


console = Console()
text = Text("Welcome to Mk’s Cuisine", justify="center")
text.stylize("bold red")
panel = Panel(text)
console.print(panel)
