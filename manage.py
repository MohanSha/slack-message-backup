#!/usr/local/bin/python3
import os
from app import create_app, db
from app.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app("default")
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return (dict(app=app, db=db, user=User))

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def create_db():
    db.create_all()


if __name__ == "__main__":
    app.run()
    # manager.run()
