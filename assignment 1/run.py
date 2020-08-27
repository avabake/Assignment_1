from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/officer')
def officer():
    return render_template('officer.html')

@app.route('/officer/<year>')
def officerYear(year):
    return render_template('officer.html')
    max_value = 0.2




@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/camera/<year>')
def cameraYear(year):
    return render_template('camera.html')
    max_value = 0.2


    # retrieve and calculate auckland value
    con = sqlite3.connect('data/pnorthland.db')
    cur = con.execute('SELECT {} FROM pnorthland'.format(year))
    tickets = list(cur)[0][0]
    nor = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/pauckland.db')
    cur = con.execute('SELECT {} FROM pauckland'.format(year))
    tickets = list(cur)[0][0]
    auc = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/pwaikato.db')
    cur = con.execute('SELECT {} FROM pwaikato'.format(year))
    tickets = list(cur)[0][0]
    wai = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/pbayofplenty.db')
    cur = con.execute('SELECT {} FROM pbayofplenty'.format(year))
    tickets = list(cur)[0][0]
    bay = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/peastern.db')
    cur = con.execute('SELECT {} FROM peastern'.format(year))
    tickets = list(cur)[0][0]
    eas = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/pcentral.db')
    cur = con.execute('SELECT {} FROM pcentral'.format(year))
    tickets = list(cur)[0][0]
    man = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/pwellington.db')
    cur = con.execute('SELECT {} FROM pwellington'.format(year))
    tickets = list(cur)[0][0]
    wel = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/ptasman.db')
    cur = con.execute('SELECT {} FROM ptasman'.format(year))
    tickets = list(cur)[0][0]
    tas = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/pcanterbury.db')
    cur = con.execute('SELECT {} FROM pcanterbury'.format(year))
    tickets = list(cur)[0][0]
    can = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/psouthern.db')
    cur = con.execute('SELECT {} FROM psouthern'.format(year))
    tickets = list(cur)[0][0]
    sou = tickets / max_value * 100 / 100
    con.close()




    # camera
    con = sqlite3.connect('data/Cnorthland.db')
    cur = con.execute('SELECT {} FROM Cnorthland'.format(year))
    tickets = list(cur)[0][0]
    cnor = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/Cauckland.db')
    cur = con.execute('SELECT {} FROM Cauckland'.format(year))
    tickets = list(cur)[0][0]
    cauc = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/Cwaikato.db')
    cur = con.execute('SELECT {} FROM Cwaikato'.format(year))
    tickets = list(cur)[0][0]
    cwai = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/Cbayofplenty.db')
    cur = con.execute('SELECT {} FROM Cbayofplenty'.format(year))
    tickets = list(cur)[0][0]
    cbay = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/Ceastern.db')
    cur = con.execute('SELECT {} FROM Ceastern'.format(year))
    tickets = list(cur)[0][0]
    ceas = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/Ccentral.db')
    cur = con.execute('SELECT {} FROM Ccentral'.format(year))
    tickets = list(cur)[0][0]
    cman = tickets / max_value * 100 / 100
    con.close()

    con = sqlite3.connect('data/Cwellington.db')
    cur = con.execute('SELECT {} FROM Cwellington'.format(year))
    tickets = list(cur)[0][0]
    cwel = tickets / max_value * 100 / 100
    con.close()




    nor_tickets = 0.089479
    nor = nor_tickets / max_value * 100 / 100

    wai_tickets = 0.094288
    wai = wai_tickets / max_value * 100 / 100

    bay_tickets = 0.011918
    bay = bay_tickets / max_value * 100 / 100

    eas_tickets = 0.114043
    eas = eas_tickets / max_value * 100 / 100

    man_tickets = 0.111946
    man = man_tickets / max_value * 100 / 100

    wel_tickets = 0.135693
    wel = wel_tickets / max_value * 100 / 100

    tas_tickets = 0.030456
    tas = tas_tickets / max_value * 100 / 100

    can_tickets = 0.081584
    can = can_tickets / max_value * 100 / 100

    sou_tickets = 0.198442
    sou = sou_tickets / max_value * 100 / 100

    return render_template('officer.html',
    northland=nor,
    auckland=auc,
    waikato=wai,
    bayofplenty=bay,
    eastcost=eas,
    manawatu=man,
    wellington=wel,
    tasman=tas,
    canterbury=can,
    southern=sou,)

    return render_template('camera.html',
    northland=cnor,
    auckland=cauc,
    waikato=cwai,
    bayofplenty=cbay,
    eastcost=ceas,
    manawatu=cman,
    wellington=cwel,
    tasman=ctas,
    canterbury=ccan,
    southern=csou,)
