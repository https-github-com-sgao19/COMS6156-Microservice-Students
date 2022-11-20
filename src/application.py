from flask import Flask, Response, request, make_response
from datetime import datetime
import json
from columbia_student_resource import ColumbiaStudentResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/test", methods=["GET", "POST"])
def test_flask():
    params = request.args
    body = request.json
    if request.method == "POST":
        msg = {1: "test POST"}
        rsp = Response(json.dumps(msg), status=404, content_type="application/json")
    else:
        msg = {2: "test GET"}
        rsp = make_response(msg)
        rsp.status = 404
        rsp.headers['customHeader'] = 'This is a custom header'

    return rsp


@app.put("/students/<uni>")
def put_student(uni):
    params = request.args
    ColumbiaStudentResource.update_by_key(uni, params)
    return get_student_by_uni(uni)


@app.post("/students")
def post_student():
    body = request.json
    try:
        ColumbiaStudentResource.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return get_student_by_uni(body["uni"])


@app.delete("/students/<uni>")
def delete_student(uni):
    try:
        ColumbiaStudentResource.delete_by_key(uni)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@app.get("/students")
def get_students_by_template():
    pass


@app.route("/students/<uni>", methods=["GET"])
def get_student_by_uni(uni):
    result = ColumbiaStudentResource.get_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
