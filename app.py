from flask import Flask, render_template
import os

app = Flask(__name__)
app.debug = True

if os.environ.get('ENV') == 'production':
    debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

else:
    debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/local-playlist'



if __name__ == '__main__':
    app.run(debug=debug,port=3000)