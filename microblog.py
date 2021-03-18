from flask import Flask

app = Flask("microblog")

#aqui vai comentário
@app.route("/")
def index():
    return "Hello World"

app.run()