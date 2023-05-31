import os
import sys
import subprocess

from flask import (
    Blueprint, render_template, request
)

bp = Blueprint("task", __name__)

@bp.route("/task4", methods=("GET", ))
def task4():

    return render_template("tasks/task4.html")


@bp.route("/task4_solution", methods=("POST", ))
def task4_solution():
    r1 = request.form.get("R1")
    r2 = request.form.get("R2")
    r3 = request.form.get("R3")
    r4 = request.form.get("Rsum")
    # ["/usr/bin/git", "commit", "-m", "Fixes a bug."]
    cmd = ["solver/a.out"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.wait()
    a, b = p.communicate()
    stdout, stderr = a.decode("utf-8"), b.decode("utf-8")
    print(stdout, stderr)


    # return "{} {} {} {}".format(r1, r2, r3, r4)
    return stdout
