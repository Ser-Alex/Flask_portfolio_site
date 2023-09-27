import logging
from logging.handlers import RotatingFileHandler

from portfolioapp import create_app, db


app = create_app()

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.logger.addHandler(handler)
        app.run(debug=True,port=5000, host='0.0.0.0')
