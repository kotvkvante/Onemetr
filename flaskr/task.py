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
    form = request.form
    R1 = form_get_float_safe(form, "R1")
    R2 = form_get_float_safe(form, "R2")
    R3 = form_get_float_safe(form, "R3")
    Rsum = form_get_float_safe(form, "Rsum")
    EsR1 = form_get_float_safe(form, "EsR1")
    EsR2 = form_get_float_safe(form, "EsR2")
    EsR3 = form_get_float_safe(form, "EsR3")
    EsRsum = form_get_float_safe(form, "EsRsum")
    EiR1 = form_get_float_safe(form, "EiR1")
    EiR2 = form_get_float_safe(form, "EiR2")
    EiR3 = form_get_float_safe(form, "EiR3")
    EiRsum = form_get_float_safe(form, "EiRsum")

    arguments = [R1, R2, R3, Rsum, EsR1, EsR2, EsR3, EsRsum, EiR1, EiR2, EiR3, EiRsum]

    res = 1
    for x in arguments: res = res and x
    if res is None:
        return "Incorrect input"

    cmd = [str(x) for x in arguments]

    path = "Onemetr/solver/task4.bin"
    if current_app.debug:
        path = "solver/task4.bin"

    cmd.insert(0, path)
    # ["/usr/bin/git", "commit", "-m", "Fixes a bug."]
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
    form = request.form
    dmax = form_get_float_safe(form, "dmax")
    dmin = form_get_float_safe(form, "dmin")
    Smax = form_get_float_safe(form, "Smax")
    Smin = form_get_float_safe(form, "Smin")
    EPCmax = form_get_float_safe(form, "EPCmax")
    EPCmin = form_get_float_safe(form, "EPCmin")
    Dmax = form_get_float_safe(form, "Dmax")
    Dmin = form_get_float_safe(form, "Dmin")
    method = form_get_int_safe(form, "options")

    arguments = [method, dmax, dmin, Smax, Smin, EPCmax, EPCmin, Dmax, Dmin]

    res = 1
    for x in arguments: res = res and x
    if res is None:
        return "Incorrect input"

    cmd = [str(x) for x in arguments]
    # print(sarguments)
    path = "Onemetr/solver/task3.bin"
    if current_app.debug:
        path = "solver/task3.bin"

    # ["/usr/bin/git", "commit", "-m", "Fixes a bug."]
    cmd.insert(0, path)
    print("cmd >> ", cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    prog_result = p.wait()
    if prog_result != 0:
        return "Failed: Td / 2 + TD / 2 + TL + TEPC != TS"
    a, b = p.communicate()
    stdout, stderr = a.decode("utf-8"), b.decode("utf-8")
    print("stdout {} >> {}".format(type(stdout), stdout))
    print("stderr >> ", stderr)
    if (stdout == ""):
        return "Incorrect input"

    res = stdout.split(" ")
    print(res)

    return "L = {} mm\nEsL = {} mkm\nEiL = {} mkm".format(res[0], res[1], res[2])

def form_get_int_safe(form, key):
    _value = form.get(key)
    if _value is None:
        return None;

    try:
        return int(_value)
    except (ValueError, TypeError):
        return None

def form_get_float_safe(form, key):
    _value = form.get(key)
    if _value is None:
        return None;

    _value = _value.replace(",", ".")

    try:
        return float(_value)
    except (ValueError, TypeError):
        return None
