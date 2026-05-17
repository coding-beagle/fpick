import os
import sys
import shelve
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import click

FPICK_CACHE = "fpickcache"  # previous directory
LAST_DIR_KEY = "last_dir"


def cache_path() -> str:
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local"))
    elif sys.platform == "darwin":
        base = Path.home() / "Library/Caches"
    else:
        base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    d = base / "fpick"
    d.mkdir(parents=True, exist_ok=True)
    return str(d / "cache")


def file_extension_string_to_arg(ext: str) -> tuple[str, str]:
    """Check if user has put a . before the ext string, and also create a label"""
    ext = ext.strip()
    if not ext.startswith("."):
        ext = f".{ext.lower()}"
    return (f"*{ext}", ext)


@click.command()
@click.option(
    "--directory",
    "-d",
    is_flag=True,
    default=False,
    help="Select directories instead of files",
)
@click.option(
    "--file-extension",
    "-f",
    "extensions",
    multiple=True,
    default=None,
    help="File extension to filter by",
)
def cli(directory, extensions):
    """Return a selected file to stdout"""
    root = tk.Tk()
    root.withdraw()

    try:
        with shelve.open(cache_path()) as fcache:
            last_dir = fcache.get(LAST_DIR_KEY) or os.getcwd()

            to_cache: str = ""

            path = None

            if directory:
                path = filedialog.askdirectory(initialdir=last_dir)
            elif extensions:
                filetypes = [file_extension_string_to_arg(e) for e in extensions]
                path = filedialog.askopenfilename(
                    initialdir=last_dir, filetypes=filetypes
                )
            else:
                path = filedialog.askopenfilename(initialdir=last_dir)

            if not path or path == "":
                sys.exit(1)

            click.echo(path)

            to_cache = os.path.dirname(path)
            if to_cache != "":
                fcache[LAST_DIR_KEY] = to_cache
                fcache.sync()
    finally:
        root.destroy()
