from backend import app
from flask_cors import CORS
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)
if __name__ == '__main__':  # Script executed directly?
    CORS(app, resources={r"/*": {"origins": ["https://asstoken2.github.io", "http://localhost:3000"],
        "methods": ["GET", "POST", "DELETE", "PUT"]}})
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
