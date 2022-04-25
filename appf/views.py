from appf import app

@app.route('/')
def index():
    return 'Ну привет! Это приложение "Каталог оборудования"'