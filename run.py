from app import app
from app.models import User, Post, db, Merch

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Merch': Merch}

if __name__ == '__main__':
    app.run()