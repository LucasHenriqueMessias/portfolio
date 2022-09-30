from flask import Flask, render_template

app = Flask(__name__)

#Create the 1st page 
@app.route("/") #Route -> caminho depois do domínio (meusite.com/rota/rotafilho)
def homepage(): #Function -> o que será exibido na página
    return render_template("/homepage.html")

@app.route("/about-me")
def aboutMe():
    return render_template("about_me.html")

@app.route("/music")
def Music():
    return render_template("music.html")
#Initializate the site
if __name__ == "__main__":
    app.run(debug=True)
