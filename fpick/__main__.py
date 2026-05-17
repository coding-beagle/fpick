import click
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


@click.command()
def cli():
    """write chosen file to stdout"""
    file_path = filedialog.askopenfilename()
    click.echo(file_path)
