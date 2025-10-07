from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args["color"]
    fashion = request.args["fashionRange"]
    animal = request.args["animal"]
    hobby = request.args["hobby"]
    character = request.args["favCharacter"]
    hufflepuff = 0
    ravenclaw = 0
    gryffindor = 0
    slytherin = 0
    
    match color:
        case "green":
            slytherin = slytherin + 1
        case "red":
            gryffindor = gryffindor + 1
        case "yellow":
            hufflepuff = hufflepuff + 1
        case "blue":
            ravenclaw = ravenclaw + 1
    if fashion < "5":
        slytherin = slytherin + 1
        ravenclaw = ravenclaw + 1
    else:
        gryffindor = gryffindor + 1
        hufflepuff = hufflepuff + 1
    match animal:
        case "cat":
            gryffindor = gryffindor + 1
            ravenclaw = ravenclaw + 1
        case "dog":
            gryffindor = gryffindor + 1
        case "newt":
            slytherin = slytherin + 1
            hufflepuff = hufflepuff + 1
        case "owl":
            ravenclaw = ravenclaw + 1
        case "crow":
            slytherin = slytherin + 1
        case "bunny":
            hufflepuff = hufflepuff + 1
    match hobby:
        case "quidditch":
            gryffindor = gryffindor + 1
        case "mysteries":
            ravenclaw = ravenclaw + 1
        case "creatures":
            hufflepuff = hufflepuff + 1
        case "magic":
            slytherin = slytherin + 1
    match character:
        case "Harry Potter":
            gryffindor = gryffindor + 1
        case "Hermione Granger":
            ravenclaw = ravenclaw + 1
        case "Ron Weasley":
            hufflepuff = hufflepuff + 1
        case "Dumbledore":
            slytherin = slytherin + 1
        case "Snape":
            gryffindor = gryffindor + 1
        case "Voldemort":
            slytherin = slytherin + 1
        case "Draco Malfoy":
            ravenclaw = ravenclaw + 1
        case "Hagrid":
            hufflepuff = hufflepuff + 1
        case "Minerva McGonagall":
            ravenclaw = ravenclaw + 1
        case "Fred/George Weasley":
            gryffindor = gryffindor + 1
        case "Luna Lovegood":
            hufflepuff = hufflepuff + 1
        case "Bellatrix Lestrange":
            slytherin = slytherin + 1
        
    if gryffindor > slytherin and gryffindor > ravenclaw and gryffindor > hufflepuff:
        house = "Gryffindor"
    elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
        house = "Slytherin"
    elif ravenclaw > gryffindor and ravenclaw > slytherin and ravenclaw > hufflepuff:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"
        
    return render_template("response.html", answer = house)

if __name__=="__main__":
    app.run(debug=True)