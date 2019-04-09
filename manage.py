from royblog.app import create_app

app = create_app('test')

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)
    