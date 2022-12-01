"""Description.
Application en ligne de commande pour la modification de l'exercice adaptatif.
"""
from .latex_fin import document
from rich import print
from sympy import Rational
import typer

app = typer.Typer()

@app.callback()
def callback():
    pass

@app.command()
def original():
    document()
    typer.echo("Les fichier .tex et .pdf sont dans le dossier")

@app.command()
def test():
    type.echo("C'est un test")
