from flask import Flask
from MediaController import media
from NavigationController import navigation
from ZeroConfWrapper import ZeroConfWrapper

app = Flask(__name__)
app.register_blueprint(media)
app.register_blueprint(navigation)

if __name__ == "__main__":
    z = ZeroConfWrapper()
    z.register_service()
    app.run(ssl_context=("./res/certificate.crt.pem", "./res/private_key.key.pem"), host="0.0.0.0", port=5000)
