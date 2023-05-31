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

    if(R1)
    # ["/usr/bin/git", "commit", "-m", "Fixes a bug."]

    path = "Onemetr/solver/a.out"
    if current_app.debug:
        path = "solver/a.out"

    cmd = [path, R1, R2, R3, Rsum, EsR1, EsR2, EsR3, EsRsum, EiR1, EiR2, EiR3, EiRsum]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.wait()
    a, b = p.communicate()
    stdout, stderr = a.decode("utf-8"), b.decode("utf-8")
    print(stdout, stderr)


    # return "{} {} {} {}".format(r1, r2, r3, r4)
    return stdout
