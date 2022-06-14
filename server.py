from flask import Flask, render_template,redirect,session


app = Flask(__name__)
app.secret_key='secret'



@app.route("/counter")
def counter():
    # in the if statement the name count  has to be the same name that you use to call the session 
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1 
    return render_template("index.html" )


@app.route("/counter/add", methods =["Post"] )
def add_counter():
    session["count"] += 1
    return redirect("/counter")


@app.route("/clear", methods =["Post"] )
def delete_counter():
    session["count"] = 0
    return redirect("/counter")


if __name__ == "__main__":
    app.run(debug=True)

