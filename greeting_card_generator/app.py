from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        
        name = request.form['name']
        age = int(request.form['age'])
        cardtype = request.form['cardtype']

        message = ""
        img_url = ""

        if cardtype == "new_year":
            message = f"Happy New Year {name.title()}"
            img_url = "https://ak.picdn.net/shutterstock/videos/4073554/thumb/3.jpg?ip=x480"

        elif cardtype == "birthday":
            message = f"Happy {age} Birthday {name.title()}!"
            img_url = "https://wallpaperaccess.com/full/782910.jpg"

        elif cardtype == "christmas":
            message = f"Merry Christmas {name.title()}!"
            img_url = "https://c4.wallpaperflare.com/wallpaper/987/738/395/new-year-cookies-christmas-christmas-wallpaper-preview.jpg"

        return render_template('index.html', message=message, img_url=img_url)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)