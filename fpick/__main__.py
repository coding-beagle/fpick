import click
import os
import shelve
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


FPICK_CACHE = "fpickcache"  # previous directory
LAST_DIR_KEY = "last_dir"


@click.command()
@click.option("--directory", "-d", is_flag=True, default=False)
def cli(directory):
    """Open the file dialog and write it to stdout, and cache the folder of the last selected file"""

    with shelve.open(FPICK_CACHE) as fcache:
        last_dir = fcache.get(LAST_DIR_KEY, None)

        if last_dir is None:
            last_dir = os.getcwd()

        to_cache: str = ""

        if directory:
            file_path: str = filedialog.askdirectory(initialdir=last_dir)
            to_cache = file_path
        else:
            file_path: str = filedialog.askopenfilename(initialdir=last_dir)
            to_cache = os.path.dirname(file_path)

        click.echo(file_path)

        if to_cache != "":
            fcache[LAST_DIR_KEY] = to_cache
            fcache.sync()
