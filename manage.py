from flask_script import Manager, Server
# import app and db from app
from app import create_app
# import tables from app.models


app = create_app()
manager =  Manager(app)
manager.add_command('server',Server(use_debugger=True))

if __name__== "__main__":
    manager.run()
