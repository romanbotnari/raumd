from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "good" : "green",
    "bad": "red",
    "important": "purple",
    "accent": "blue",
    })

console = Console(theme=custom_theme)