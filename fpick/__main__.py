import click
import os
import shelve
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


FPICK_CACHE = "fpickcache"  # previous directory
LAST_DIR_KEY = "last_dir"


def file_extension_string_to_arg(ext_string: str) -> tuple[str, str]:
    """Check if user has put a . before the ext string, and also create a label"""
    stripped_string = ext_string.strip()

    if stripped_string.startswith("."):
        label: str = stripped_string.split(".")[-1]

        return (f"{label.upper()} Files (*{stripped_string})", stripped_string)
    else:
        label: str = stripped_string
        return (
            f"{label.upper()} Files (*{stripped_string.lower()})",
            f".{stripped_string.lower()}",
        )


@click.command()
@click.option(
    "--directory",
    "-d",
    is_flag=True,
    default=False,
    help="Select directories instead of files",
)
@click.option(
    "--file_extension",
    "-f",
    default=None,
    help="File extension to filter by",
)
def cli(directory, file_extension):
    """Return a selected file to stdout"""

    with shelve.open(FPICK_CACHE) as fcache:
        last_dir = fcache.get(LAST_DIR_KEY, None)

        if last_dir is None:
            last_dir = os.getcwd()

        to_cache: str = ""

        if directory:
            file_path: str = filedialog.askdirectory(initialdir=last_dir)
            to_cache = file_path
        else:

            if file_extension:
                file_path: str = filedialog.askopenfilename(
                    initialdir=last_dir,
                    filetypes=[file_extension_string_to_arg(file_extension)],
                )
            else:
                file_path: str = filedialog.askopenfilename(initialdir=last_dir)
            to_cache = os.path.dirname(file_path)

        click.echo(file_path)

        if to_cache != "":
            fcache[LAST_DIR_KEY] = to_cache
            fcache.sync()
