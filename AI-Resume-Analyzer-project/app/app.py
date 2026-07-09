from flask import Flask, redirect, render_template, session, request, url_for, jsonify
from db import Base, sessionLocal, engine
from models import User, Report
import models
import PyPDF2
import docx
import json
from Ai_setup import resume_analyzer

app = Flask(__name__)
app.secret_key = "0812"
Base.metadata.create_all(bind=engine)






# Home
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/signup")






# Signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST": 
        db = sessionLocal()
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        new_user = User(
            username=username,
            email=email,
            password_hash=password
        )

        db.add(new_user)
        db.commit()
        db.close()
        return redirect("/login")
    return render_template("signup.html")  



# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":  
        db = sessionLocal()
        email = request.form.get("email")
        password = request.form.get("password")


        user = db.query(User).filter(User.email == email, User.password_hash == password).first()
        db.close()

        if user:
            session['user'] = user.email  
            session['username'] = user.username  
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password!"
            
    return render_template("login.html") 



#Dashboard
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")
        
    result = None
    resume_text = ""
    
    if request.method == "POST":   
        user_goal = request.form.get("role")   
        form_text = request.form.get("resume") 
        file = request.files.get("file")       

       
        if file and file.filename != "": 
            if file.filename.endswith(".pdf"):
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    resume_text += page.extract_text() or ""
                    
            elif file.filename.endswith(".docx"):
                doc = docx.Document(file)  
                for para in doc.paragraphs:
                    resume_text += para.text + "\n"
        
      
        else:
            resume_text = form_text

       
        if resume_text and user_goal:
           
            result = resume_analyzer(resume_text, user_goal)
            
          
            db = sessionLocal()
            user = db.query(User).filter_by(email=session['user']).first()
            
    
            report_content = json.dumps(result) if isinstance(result, (dict, list)) else str(result)
            
       
            report = Report(
                user_id=user.id,
                resume=resume_text,     
                role=user_goal,         
                result=report_content   
            )
            db.add(report)
            db.commit()
            db.close()
                
    return render_template("dashboard.html", user=session.get("username"), result=result)




# History        
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")
        
    db = sessionLocal()
    user = db.query(User).filter_by(email=session["user"]).first()
    raw_reports = db.query(Report).filter_by(user_id=user.id).all()
    db.close()
    
    reports_data = []
    for report in raw_reports:
        try:
          
            parsed_result = json.loads(report.result)
        except Exception:
           
            parsed_result = {"skills": [], "missing_skills": [], "roadmap": {}, "interview_questions": []}
            
        reports_data.append({
            "role": report.role,
            "data": parsed_result 
        })
    
    return render_template('history.html', reports=reports_data)




#AI Chat Montor
@app.route('/chat', methods=["GET", "POST"])
def chat():
    if "user" not in session:
        return redirect("/login")
        
    if request.method == "POST":
   
        data = request.get_json() or {}
        user_message = data.get("message")
        
        if not user_message:
            return jsonify({"error": "Message content is empty"}), 400
            
        try:
           
            chat_prompt = f"The user is asking about career fields, skills, or roadmap alignment: {user_message}"
            ai_response = resume_analyzer(chat_prompt, "Skills and Field Mentorship")
            
            return jsonify({"response": ai_response})
        except Exception as e:
            return jsonify({"error": f"Chat Engine Error: {str(e)}"}), 500
            
    return render_template("interview-quesion.html", user=session.get("username"))

# Forgot Password
@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_pass():
    if request.method == "POST":
        db = sessionLocal()
        email = request.form.get("email")
        new_password = request.form.get("password")

        user = db.query(User).filter(User.email == email).first()
        
        if user:
            user.password_hash = new_password  
            db.commit()
            db.close()
            return "Password successfully reset!"
        else:
            db.close()
            return "Error: You are not registered with this email!"

    return render_template("forget-password.html")

# Logout
@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user" , None)  
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)