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

@pass_config
@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def terraform(config, verbose):
    config.verbose = verbose

@terraform.commands()
def init(config):
    """This script inits a Terraform project."""
    if config.verbose:
       click.echo('We are in verbose mode.')
    click.echo('terraform init')
