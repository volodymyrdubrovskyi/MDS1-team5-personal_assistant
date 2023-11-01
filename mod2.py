from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

# Внешний пакет нужно сначала установить в терминале: pip install prompt_toolkit

commands = WordCompleter([
    "close", "exit", "hello", "add", "edit", "del", "add-phone", "edit-phone", "del-phone", "all"], ignore_case=True)
session = PromptSession(completer=commands)