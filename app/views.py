
from app import app
from flask import request, send_file, render_template, redirect, url_for, session as user

@app.route('/project.html')
def project():
    return render_template('project.html') 

@app.route('/contact.html')
@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/aboutpage.html')
def aboutpage():
    return render_template('aboutpage.html') 

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html') 

@app.route("/", methods=['POST', 'GET'])
@app.route('/website.html')
def website():
    return render_template('website.html')