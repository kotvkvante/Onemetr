import os
import sys
import subprocess

from flask import (
    Blueprint, render_template, request, current_app
)

bp = Blueprint("task", __name__)

@bp.route("/task4", methods=("GET", ))
def task4():
    return render_template("tasks/task4.html")


@bp.route("/task4_solution", methods=("POST", ))
def task4_solution():
    R1 = request.form.get("R1")
    R2 = request.form.get("R2")
    R3 = request.form.get("R3")
    Rsum = request.form.get("Rsum")
    EsR1 = request.form.get("EsR1")
    EsR2 = request.form.get("EsR2")
    EsR3 = request.form.get("EsR3")
    EsRsum = request.form.get("EsRsum")
    EiR1 = request.form.get("EiR1")
    EiR2 = request.form.get("EiR2")
    EiR3 = request.form.get("EiR3")
    EiRsum = request.form.get("EiRsum")

    # ["/usr/bin/git", "commit", "-m", "Fixes a bug."]

    path = "Onemetr/solver/task4.bin"
    if current_app.debug:
        path = "solver/task4.bin"

    cmd = [path, R1, R2, R3, Rsum, EsR1, EsR2, EsR3, EsRsum, EiR1, EiR2, EiR3, EiRsum]
    print(cmd)

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.wait()
    a, b = p.communicate()
    stdout, stderr = a.decode("utf-8"), b.decode("utf-8")
    print("stdout {} >> {}".format(type(stdout), stdout))
    print("stderr >> ", stderr)
    if (stdout == ""):
        return "Incorrect input"

    res = stdout.split(" ")
    print(res)

    return "Rmax = {}\nRmin = {}".format(res[0], res[1])

@bp.route("/task3", methods=("GET", ))
def task3():
    return render_template("tasks/task3.html")

@bp.route("/task3_solution", methods=("POST", ))
def task3_solution():
    dmax = request.form.get("dmax")
    dmin = request.form.get("dmax")
    Smax = request.form.get("Smax")
    Smin = request.form.get("Smin")
    EPCmax = request.form.get("EPCmax")
    EPCmin = request.form.get("EPCmin")
    Dmax = request.form.get("Dmax")
    Dmin = request.form.get("Dmin")

    method = request.form.get("options")
    # print(method)
    # ["/usr/bin/git", "commit", "-m", "Fixes a bug."]

    path = "Onemetr/solver/task3.bin"
    if current_app.debug:
        path = "solver/task3.bin"

    cmd = [path, method, dmax, dmin, Smax, Smin, EPCmax, EPCmin, Dmax, Dmin]
    print(cmd)

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.wait()
    a, b = p.communicate()
    stdout, stderr = a.decode("utf-8"), b.decode("utf-8")
    print("stdout {} >> {}".format(type(stdout), stdout))
    print("stderr >> ", stderr)
    if (stdout == ""):
        return "Incorrect input"

    res = stdout.split(" ")
    print(res)


    return "L = {} mm\nEsL = {}mkm\nEiL = {}mkm".format(res[0], res[1], res[2])
