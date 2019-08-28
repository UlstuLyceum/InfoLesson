from infolesson.initialization import app

try:
    import infolesson.local_config as config
except ImportError:
    import infolesson.example_config as config

if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.FLASK_DEBUG)
