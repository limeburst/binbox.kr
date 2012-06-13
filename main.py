from flask import Flask, render_template, url_for

import subprocess
import random

app = Flask(__name__)

fonts = ['bubble', 'digital', 'small', 'smscript']

userlist = [
            ('root', 'the evangelist', 'http://not.binbox.kr/'),
            ('realax', 'the pokemon', 'http://realax.binbox.kr/'),
            ('noah', 'the ark of knowledge', 'http://hona.kr/'),
            ('(sy, m)', 'the dull philosopher', 'http://eil.me/'),
            ('rwt', 'binbox 2012', 'http://rwt.binbox.kr/'),
            ('jang', 'binbox 2012', 'http://jang.binbox.kr/'),
            ('link', 'binbox 2012', 'http://link.binbox.kr/'),
            ('corvina', 'binbox 2012', 'http://corvina.binbox.kr/'),
            ('porsis', 'binbox 2012', 'http://porsis.binbox.kr/'),
            ('jay', 'binbox 2012', 'http://jay.binbox.kr/'),
            ('duddls', 'binbox 2012', 'http://duddls.binbox.kr/'),
            ('nevir', 'binbox 2012', 'http://nevir.binbox.kr/'),
            ('moon', 'binbox 2012', 'http://moon.binbox.kr/'),
            ('tts', 'binbox 2012', 'http://tts.binbox.kr/'),
            ('among', 'binbox 2012', 'http://among.binbox.kr/'),
            ('ooga', 'binbox 2012', 'http://ooga.binbox.kr/'),
            ('akiddie', 'binbox 2012', 'http://akiddie.binbox.kr/'),
           ]

sites = [
        'http://binbox.kr/',
        'http://not.binbox.kr/',
        'http://realax.binbox.kr/',
        'http://rwt.binbox.kr/',
        'http://jang.binbox.kr/',
        'http://link.binbox.kr/',
        'http://corvina.binbox.kr/',
        'http://porsis.binbox.kr/',
        'http://jay.binbox.kr/',
        'http://duddls.binbox.kr/',
        'http://nevir.binbox.kr/',
        'http://moon.binbox.kr/',
        'http://tts.binbox.kr/',
        'http://among.binbox.kr/',
        'http://ooga.binbox.kr/',
        'http://akiddie.binbox.kr/',
        'http://hona.kr/',
        'http://sy.hona.kr/',
        'http://eil.me/',
        'http://hot.nerds.kr/',
        ]


@app.route('/')
def welcome():
    command = 'figlet -f {0} BINBOX'.format(random.choice(fonts))
    figlet = subprocess.check_output(command, shell=True)
    return render_template('welcome.html', logo=figlet)

@app.route('/users/')
def users():
    command = 'figlet -f {0} BINBOX'.format(random.choice(fonts))
    figlet = subprocess.check_output(command, shell=True)
    return render_template('users.html', logo=figlet, users=userlist)

@app.route('/faq/')
def faq():
    command = 'figlet -f {0} BINBOX'.format(random.choice(fonts))
    figlet = subprocess.check_output(command, shell=True)
    return render_template('faq.html', logo=figlet)

@app.route('/vhosts/')
def vhosts():
    command = 'figlet -f {0} BINBOX'.format(random.choice(fonts))
    figlet = subprocess.check_output(command, shell=True)
    return render_template('vhosts.html', logo=figlet, sites=sites)

@app.route('/talks/')
def talks():
    command = 'figlet -f {0} BINBOX'.format(random.choice(fonts))
    figlet = subprocess.check_output(command, shell=True)
    talklist = [
                ('2011-03-05', 'root', 'Introduction to BINBOX',    url_for('static', filename='2011-03-05-introduction-to-binbox.pdf')),
                ('2011-05-07', 'root', 'Dip Into Python',           url_for('static', filename='2011-05-07-dip-into-python.pdf')),
                ('2011-07-09', 'root', 'Simple Algorithms',         url_for('static', filename='2011-07-09-simple-algorithms.pdf')),
                ('2011-09-17', 'root', 'BINBOX Toys',               url_for('static', filename='2011-09-17-binbox-toys.pdf')),
                ('2011-11-09', 'root', 'Practical Python',          url_for('static', filename='2011-11-09-practical-python.pdf')),
               ]
    return render_template('talks.html', logo=figlet, talks=talklist)

@app.route('/status/')
def status():
    command = 'figlet -f {0} BINBOX'.format(random.choice(fonts))
    figlet = subprocess.check_output(command, shell=True)
    uptime = subprocess.check_output('uptime', shell=True)
    return render_template('status.html', logo=figlet, uptime=uptime)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
