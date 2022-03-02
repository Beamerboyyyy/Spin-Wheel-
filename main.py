from flask import Flask
from flask import render_template
from flask import request
import time
import random
from flask import g, url_for, redirect

#Edit promocodes here

apromo="XYXCEU"   #5%
bpromo="HKZYTR"  #10%
cpromo="NCAPRW"  #15%
dpromo="LBEPPW"  #25%
epromo="XFPAEW"  #35%
fpromo="QKTBVT"  #50%
promo="Null value"
result=None
degree=0
app = Flask(__name__)
@app.route("/")
def index():
    
    #Edit Probabilities of the events here
    
    a_prob = 5 #5%
    b_prob = 5 #10%
    c_prob = 10 #15%
    d_prob = 20 #25%
    e_prob = 50 #35%
    f_prob=  10 #50%
    
    if (a_prob>100) or (b_prob>100) or (c_prob>100) or (d_prob>100) or (e_prob>100) or (f_prob>100):
            return(render_template('error.html'))

        
    if (a_prob<0) or (b_prob<0) or (c_prob<0) or (d_prob<0) or (e_prob<0) or (f_prob<0):
        return(render_template('error.html'))
    if (a_prob+b_prob+c_prob+d_prob+e_prob+f_prob)!=100:
                return(render_template('error.html'))
    global result
    result=start_roulette(a_prob,b_prob,c_prob,d_prob,e_prob,f_prob)
    print(result)
    global promo
    if result=="5":
        promo=apromo
    if result=="10":
        promo=bpromo
    if result=="15":
        promo=cpromo
    if result=="25":
        promo=dpromo
    if result=="35":
        promo=epromo
    if result=="50":
        promo=fpromo

    print(promo)
    # time.sleep(2)
    return render_template('index.html',degree=degree,rotation_begin=start())

@app.route("/spin",methods=["GET","POST"])
def spin():
    if request.method=="POST":
        return(render_template('spin.html',
        result=result,degree=degree))     
    else:
        return redirect("/")

@app.route("/button",methods=["GET","POST"])
def start():
    if request.method=="POST":
        time.sleep(3)
        return(render_template('end.html',
        result=result,promo=promo))
    else:
       return redirect("/")


def start_roulette(aprob,bprob,cprob,dprob,eprob,fprob):
    rotation=random.randint(2,5)
    global degree
    degree=random.randint(1+(360*rotation),360+(360*rotation))
    if aprob==100:
        return('5')
    elif bprob==100:
        return('10')
    elif cprob==100:
        return('15')
    elif dprob==100:
        return('25')
    elif eprob==100:
        return('35')
    elif fprob==100:
        return('50')
    while True:
        for i in range(aprob):
            if random.randint(0,100)==aprob:
                return('5')
        for i in range(bprob):     
            if random.randint(0,100)==bprob:
                return('10')
        for i in range(cprob):
            if random.randint(0,100)==cprob:
                return('15')
        for i in range(dprob):
            if random.randint(0,100)==dprob:
                return('25')
        for i in range(eprob):
            if random.randint(0,100)==eprob:
                return('35')
        for i in range(fprob):
            if random.randint(0,100)==fprob:
                return('50')

# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)