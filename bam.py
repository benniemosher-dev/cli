import click

class Config(object):

   def __init__(self):
      self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose

@cli.command()

@pass_config
def say(config, string, repeat, out):
    """This script greets you."""
    if config.verbose:
       click.echo('We are in verbose mode.')
    for x in range(repeat):
      click.echo('Hello %s!' % string, file=out)
