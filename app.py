'''
	AIM4 - Flask - [A] Basic - [05] Post Method
	
	Orbit Future Academy - AI Mastery - KM Batch 4
	Tim Deployment
	2023
'''

# =[Modules dan Packages]========================
from flask import Flask,render_template,request
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================
app = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def beranda():
	return render_template('index.html')

@app.route('/halo',methods = ['POST', 'GET'])
def halo():
	if request.method == 'POST':
		nama_text = request.form.get('nama', '')
		return render_template("halo.html",nama = nama_text)
	else:
		nama_text = "Tanpa Nama"
		return render_template("halo.html",nama = nama_text)

# =[Main]========================================
if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()