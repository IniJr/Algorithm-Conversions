from rich.console import Console
from rich.text import Text
from rich.panel import Panel


console = Console()
text = Text("Hello World", justify="center")
text.stylize("bold red")
panel = Panel(text)
console.print(panel)
