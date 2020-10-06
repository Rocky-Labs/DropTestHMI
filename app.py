import csv
import os
import sqlite3 as sql
import sys
import time
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

sys.path.append("..")
from MachineMotion import *

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class FormClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    SAP = db.Column(db.Integer)
    Employee = db.Column(db.String)
    HeightFromHome = db.Column(db.Integer)
    TestSuccess = db.Column(db.String)
    date_Created = db.Column(db.DateTime, default= datetime.now)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/btnDefaultProcess', methods=['POST'])
def btnDefaultProcess():
    btn_default = request.form['btn_default']

    mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)

    print("--> Removing software stops")
    mm.releaseEstop()
    print("--> Resetting systems")
    mm.resetSystem()


    axis = 1                                       #The axis that you'd like to move
    speed = 700                                    #The max speed you'd like to move at
    acceleration = 500                             #The constant acceleration and decceleration value for the move
    position = btn_default                                 #The absolute position you'd like to move to
    mechGain = MECH_GAIN.timing_belt_150mm_turn    #The mechanical gain of the actuator on the axis
    mm.configAxis(axis, MICRO_STEPS.ustep_8, mechGain)

    # Configure movement speed, acceleration and then move
    mm.emitSpeed(speed)
    mm.emitAcceleration(acceleration)
    mm.emitAbsoluteMove(axis, position)
    print("Axis " + str(axis) + " is moving towards position " + str(position) + "mm")
    mm.waitForMotionCompletion()
    print("Axis " + str(axis) + " is at position " + str(position) + "mm")

    return jsonify({'error': 'range btn complete'})

@app.route('/SliderProcess', methods=['POST'])
def SliderProcess():
    btn_range = request.form['btn_range']

    mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)

    print("--> Removing software stops")
    mm.releaseEstop()
    print("--> Resetting systems")
    mm.resetSystem()


    axis = 1                                       #The axis that you'd like to move
    speed = 700                                    #The max speed you'd like to move at
    acceleration = 500                             #The constant acceleration and decceleration value for the move
    position = btn_range                                 #The absolute position you'd like to move to
    mechGain = MECH_GAIN.timing_belt_150mm_turn    #The mechanical gain of the actuator on the axis
    mm.configAxis(axis, MICRO_STEPS.ustep_8, mechGain)

    # Configure movement speed, acceleration and then move
    mm.emitSpeed(speed)
    mm.emitAcceleration(acceleration)
    mm.emitAbsoluteMove(axis, position)
    print("Axis " + str(axis) + " is moving towards position " + str(position) + "mm")
    mm.waitForMotionCompletion()
    print("Axis " + str(axis) + " is at position " + str(position) + "mm")

    return jsonify({'error': 'range btn complete'})


@app.route('/btnUpProcess', methods=['POST'])
def btnUpProcess():
    btn_up = request.form['btn_up']

    mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)

    print("--> Removing software stops")
    mm.releaseEstop()
    print("--> Resetting systems")
    mm.resetSystem()


    axis = 1                                       #The axis that you'd like to move
    speed = 700                                    #The max speed you'd like to move at
    acceleration = 500                             #The constant acceleration and decceleration value for the move
    position = btn_up                                 #The absolute position you'd like to move to
    mechGain = MECH_GAIN.timing_belt_150mm_turn    #The mechanical gain of the actuator on the axis
    mm.configAxis(axis, MICRO_STEPS.ustep_8, mechGain)

    # Configure movement speed, acceleration and then move
    mm.emitSpeed(speed)
    mm.emitAcceleration(acceleration)
    mm.emitAbsoluteMove(axis, position)
    print("Axis " + str(axis) + " is moving towards position " + str(position) + "mm")
    mm.waitForMotionCompletion()
    print("Axis " + str(axis) + " is at position " + str(position) + "mm")

    return jsonify({'error': 'Up btn complete'})

@app.route('/btnDownProcess', methods=['POST'])
def btnDownProcess():
    btn_down = request.form['btn_down']

    mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)

    print("--> Removing software stops")
    mm.releaseEstop()
    print("--> Resetting systems")
    mm.resetSystem()


    axis = 1                                       #The axis that you'd like to move
    speed = 700                                    #The max speed you'd like to move at
    acceleration = 500                             #The constant acceleration and decceleration value for the move
    position = btn_down                                 #The absolute position you'd like to move to
    mechGain = MECH_GAIN.timing_belt_150mm_turn    #The mechanical gain of the actuator on the axis
    mm.configAxis(axis, MICRO_STEPS.ustep_8, mechGain)

    # Configure movement speed, acceleration and then move
    mm.emitSpeed(speed)
    mm.emitAcceleration(acceleration)
    mm.emitAbsoluteMove(axis, position)
    print("Axis " + str(axis) + " is moving towards position " + str(position) + "mm")
    mm.waitForMotionCompletion()
    print("Axis " + str(axis) + " is at position " + str(position) + "mm")
    return jsonify({'error': 'Down btn complete'})

@app.route('/DropProcess', methods=['POST'])
def DropProcess():
    try:
        #di1 = request.form['di1']
        #di2 = request.form['di2']
        mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)
        time.sleep(0.5)
        # Toggles the output pins on all connected IO Modules
        detectedIOModules = mm.detectIOModules()
        for IO_Name, IO_NetworkID in detectedIOModules.items():
        #writePins ={"Pin 1":0, "Pin 2":1}
        
            mm.digitalWrite(IO_NetworkID, 1, 0)
            time.sleep(1)
            mm.digitalWrite(IO_NetworkID, 0, 1)
            time.sleep(1)
        #return jsonify({'error': 'Drop complete'})
    except Exception as e:
        return render_template('505.html')
       

@app.route('/CloseProcess', methods=['POST'])
def CloseProcess():
    di1 = request.form['di1']
    di2 = request.form['di2']
    mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)
    time.sleep(0.5)
        # Toggles the output pins on all connected IO Modules
    detectedIOModules = mm.detectIOModules()
    for IO_Name, IO_NetworkID in detectedIOModules.items():
        #writePins ={"Pin 1":0, "Pin 2":1}

        mm.digitalWrite(IO_NetworkID, 0, 0)
        time.sleep(1)
        mm.digitalWrite(IO_NetworkID, 1, 1)
        time.sleep(1)
    #return jsonify({'error': 'Close Complete'})
 

@app.route('/formProcess', methods=['POST'])
def formProcess():
    item1 = request.form['item1']
    EmpName = request.form['EmployeeName']
    TestS = request.form['Test']
    

    if item1 and EmpName and TestS:
        userForm = FormClass(SAP=item1, Employee = EmpName, HeightFromHome = 100, TestSuccess = TestS)
        db.session.add(userForm)
        db.session.commit()
        # Export data into CSV file
        conn=sql.connect('db.sqlite3')
       # print ("Exporting data into CSV............")
        cursor = conn.cursor()
        cursor.execute("select * from form_class")
        with open("DropTest_log.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            #csv_writer.writerow(['col1','col2','col3'])
            csv_writer.writerow([i[0] for i in cursor.description])

            csv_writer.writerows(cursor)
        
        dirpath = os.getcwd() + "/employee_data.csv"
        print ("Data exported Successfully into {}".format(dirpath))
        return jsonify({'item1':item1, 'Test':TestS})

    return jsonify({'error': 'Missing Data'})
@app.errorhandler(505)
def Problem505(e):
    return render_template('505.html'), 505

