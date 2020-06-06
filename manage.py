import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--host', '-h', default='0.0.0.0', help='The host to listen on')
@click.option('--port', '-p', default=5000, help='The port to listen on')
@click.option('--debug/--no-debug', '-d', default=True, help='To enable or disable the Flask debug mode')
def runServer(host, port, debug):
    '''Starts the web server'''
    click.echo('Starting web server at http://{}:{}/'.format(host, port))
    from app import app
    app.run(host=host, port=port, debug=debug)

@cli.command()
def migrate():
    '''Creates all tables in the database'''
    from model import db
    click.echo('Creating Tables')
    db.create_all()
    click.echo('All Tables are created')

@cli.command()
def tinker():
    '''Opens In-App Shell'''
    from app import app
    from model import db
    from IPython import embed
    embed()

if __name__ == '__main__':
    cli()
