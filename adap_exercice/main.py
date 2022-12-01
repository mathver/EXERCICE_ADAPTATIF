"""Description.
Application en ligne de commande pour la modification de l'exercice adaptatif.
"""
from .latex_fin import document
from rich import print
from sympy import Rational
import os
import typer

app = typer.Typer(pretty_exceptions_show_locals=False)

@app.callback()
def callback():
    """
    This application is used to create an modified version of an exercice of economics, where the user can choose some parameters.
    """

@app.command()
def original():
    """
    Function to obtain the original exercice with the parameters set by default.
    """
    document()
    typer.secho(f"\n\nThe .tex and .pdf files are in the folder C:/Users/{os.environ.get('USERNAME')}", fg=typer.colors.BRIGHT_GREEN)

@app.command()
def modifier():
    """
    Function used to modify parameter of quality and gamma in the exercice with prompt to choose them.
    The high quality must be superior or equal to low quality.
    """
    h = typer.prompt("What's the value of high quality ?", default = 4)
    l = typer.prompt("What's the value of low quality ?", default = 2)
    ghn = typer.prompt("What's the value of high quality numerator of gamma in second period ?", default = 1)
    ghd = typer.prompt("What's the value of high quality denominator of gamma in second period ?", default = 4)
    gln = typer.prompt("What's the value of low quality numerator of gamma in second period ?", default = 1)
    gld = typer.prompt("What's the value of low quality denominator of gamma in second period ?", default = 2)
    if l > h :
        typer.secho("The value of high quality must be superior or equal to the low quality one", fg = typer.colors.RED)
        raise typer.Exit()
    gh = Rational(ghn,ghd)
    gl = Rational(gln, gld)
    document(h, l, gh, gl)
    typer.secho(f"\n\nThe .tex and .pdf files are in the folder C:/Users/{os.environ.get('USERNAME')}", fg=typer.colors.BRIGHT_GREEN)