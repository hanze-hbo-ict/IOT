from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/temperature", methods=["POST"])
def temperature():
    """An endpoint accepting a temperature reading"""

    data = request.json  # temperature reading

    print("Data received", data)

    message = {"warn": False}

    # if temperature exceeds a certain treshold (e.g. 22 °C),
    # reply with a warning so the client can set the red LED

    if data["value"] > 22:
        message["warn"] = True

    # else just reply all is well and maybe signal that
    # the red LED should be switched off

    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)