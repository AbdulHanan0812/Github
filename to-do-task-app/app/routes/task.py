from flask import Blueprint, request, render_template, session, redirect, flash, url_for
from app import db
from app.models import Task

task_bp = Blueprint('task', __name__)


@task_bp.route("/", methods=['GET', 'POST'])
def view_task():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    task_list = Task.query.all()
    # 🌟 FIXED: 'task=task_list' ki jagah 'tasks=task_list' kar diya hai
    # Taake aapke HTML table ka {% for single_task in tasks %} wala loop sahi chal sake
    return render_template("task.html", tasks=task_list)
    


@task_bp.route("/add", methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    title = request.form.get("title")  
    if title:
        new_task = Task(title=title, status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash("Your Task Added Successfully", 'success')
    return redirect(url_for('task.view_task'))


@task_bp.route('/toggle/<int:task_id>', methods=['POST', 'GET'])  
def status_toggle(task_id):
    if 'user' not in session:
        return redirect(url_for("auth.login"))
        
    task = db.session.get(Task, task_id)  
    if task:
        if task.status == "Pending":
            task.status = "working"
        elif task.status == 'working':
            task.status = 'done'
        else:
            task.status = 'Pending'
        db.session.commit()    
    return redirect(url_for('task.view_task'))
    

@task_bp.route("/clear/<int:task_id>", methods=['POST', 'GET'])
def clear_task(task_id):
    if 'user' not in session:
        return redirect(url_for("auth.login"))
        
    task = db.session.get(Task, task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Your Task Deleted Successfully", 'success')
    return redirect(url_for("task.view_task"))