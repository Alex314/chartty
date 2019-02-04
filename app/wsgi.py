from whitenoise import WhiteNoise

from app import app, socketio

# socketio.run(app)
application = WhiteNoise(app)
# application = WhiteNoise(socketio)
application.add_files('static/', prefix='static/')
# socketio.run(app)
