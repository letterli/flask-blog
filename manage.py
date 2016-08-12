# _*_ coding: utf-8 _*_

import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app.models import User, Role, Permission, Article 
from app import create_app, db

app = create_app(os.environ.get('CONFIG_NAME') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Article=Article)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

