from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/energi')
def energi():
    return render_template('energi.html')

@app.route('/<size>')
def lampu(size):
    return render_template(
                            'lampu.html', 
                            size=size
                           )

@app.route('/<size>/<lights>')
def elektronik(size, lights):
    return render_template(
                            'elektronik.html',                           
                            size = size, 
                            lights = lights                           
                           )

@app.route('/<size>/<lights>/<device>')
def akhir(size, lights, device):
    return render_template('akhir.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )

@app.route('/forum')
def forum():
    return render_template('forum.html')


@app.route('/submit', methods=['POST'])
def submit_forum():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    with open('forum.txt', 'a',) as f:
        f.write(name + '\1')
        f.write(email + '\1')
        f.write(address + '\1')
        f.write(date + '\1')

    return render_template('hasil_forum.html', 
                           name=name,
                           email=email,
                           address=address,
                           date=date,
                           )

app.run(debug=True)