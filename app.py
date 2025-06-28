import os
from flask import Flask
from app.routes.main import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port railway
    app.run(debug=False, host='0.0.0.0', port=port)
