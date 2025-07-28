from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Basit kullanıcı verisi
kullanici_veritabani = {
    "admin": "1234",
    "melih": "melih123",
    "umur40":"616616"
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/giris', methods=['POST'])
def giris():
    kullanici_adi = request.form['kullanici_adi']
    sifre = request.form['sifre']
    
    # Giriş doğrulama
    if kullanici_adi in kullanici_veritabani and kullanici_veritabani[kullanici_adi] == sifre:
        return render_template('welcome.html', kullanici=kullanici_adi)
    else:
        return "Hatalı giriş! Lütfen tekrar deneyin."

if __name__ == '__main__':
    app.run(debug=True)
