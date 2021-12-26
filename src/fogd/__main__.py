"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """FoGD."""


if __name__ == "__main__":
    main(prog_name="fogd")  # pragma: no cover
