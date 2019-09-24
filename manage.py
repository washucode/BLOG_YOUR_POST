from flask_script import Manager, Server
# import app and db from app
from app import create_app,db
# import tables from app.models
from app.models import User,Post,Comment
from flask_migrate import Migrate,MigrateCommand


app = create_app('production')
manager =  Manager(app)
manager.add_command('server',Server(use_debugger=True))

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)



@manager.shell
def add_shell_context():
    return {'db': db, 'User':User, 'Post':Post, 'Comment':Comment}

@manager.command
def test():
    import unittest
    test=unittest.TestLoader().discover("Test")
    unittest.TextTestRunner(verbosity=5).run(test)

if __name__== "__main__":
    manager.run()
