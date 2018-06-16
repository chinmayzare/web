from flask import Flask, render_template, abort, redirect, url_for, escape, request, session, g
import pandas as pd
import os
import holoviews as hv
hv.extension('bokeh', 'matplotlib')
from bokeh.plotting import save
import altair as alt
alt.renderers.enable('notebook')
renderer = hv.renderer('bokeh')
 
df = pd.read_csv('realdata.csv')
df.bsfile = df.bsfile.astype(str)
dataset = hv.Dataset(df)



#Curve function
def Plot(var):
    h = hv.Curve( df, 'sst', var)
    h = h.options(width = 15500, height = 350, line_width = 3, xrotation = 45, tools=['hover'], toolbar= 'left')
    renderer.save(h, 'templates/' + var)
    return 

def PlotBB(var):
    h = hv.Curve( df, 'sst', var)
    df['2SD'] = df[var + '_std'] * 2
    df['p'] = df[var] + df['2SD']
    df['n'] = df[var] - df['2SD']
    h = hv.Curve( df, 'sst', var)
    h1 = hv.Curve( df, 'sst', 'p')
    h2 = hv.Curve( df, 'sst', 'n')
    h3 = h * h1 * h2
    h3 = h3.options(width = 15500, height = 350, border_line_width = 3, xrotation = 45, tools=['hover'], toolbar= 'left')
    renderer.save(h3, 'templates/' + var + '_std')
    return
''' 
 

def PlotBB(var):
    h1 = hv.Curve( df, 'sst', var)
    #df['2SD'] = df[var + '_std'] * 2
    #df['p'] = df[var] + df['2SD']
    #df['n'] = df[var] - df['2SD']
    #h = hv.Curve( df, 'sst', var)
    #h1 = hv.Curve( df, 'sst', 'p')
    #h2 = hv.Curve( df, 'sst', 'n')
    #h3 = h * h1 * h2
    h2 = h1.options(width = 15500, height = 350, xrotation = 45, tools=['hover'], toolbar= 'left')
    renderer.save(h2, 'templates/' + var + '_std')
    return
'''

#all graphs wrt time and other parameters
c = Plot('PM2_Conf_Ring_Pos_Mon')

c = Plot('PM2_DC_Bias_Comp')

c = Plot('PM2_Gas_01_Flow_Mon')

c = Plot('PM2_Gas_02_Flow_Mon')

c = Plot('PM2_Gas_03_Flow_Mon')

c = Plot('PM2_Gas_07_Flow_Mon')

c = Plot('PM2_Gas_09_Flow_In')

c = Plot('PM2_Gas_09_Pressure_Mon')

c = Plot('PM2_LWIND_01')

c = Plot('PM2_LWIND_07')

c = Plot('PM2_ProcChm_Bot_Elec_Temp_Mon')

c = Plot('PM2_ProcChm_ESC_Voltage_In')

c = Plot('PM2_ProcChm_Pressure_Mon')

c = Plot('PM2_RF_27MHz_FwdPwr_In')

c = Plot('PM2_RF_27MHz_Match_LoadCap_Mon')

c = Plot('PM2_RF_27MHz_Match_TuneCap_Mon')

c = Plot('PM2_RF_27MHz_RevPwr_In')

c = Plot('PM2_RF_2MHz_FwdPwr_In')

c = Plot('PM2_RF_2MHz_RevPwr_In')

c = Plot('PM2_Upper_Electrode_Temp_Mon')


#BoullingerBar
b = PlotBB('PM2_Conf_Ring_Pos_Mon')

b = PlotBB('PM2_DC_Bias_Comp')

b = PlotBB('PM2_Gas_01_Flow_Mon')

b = PlotBB('PM2_Gas_02_Flow_Mon')

b = PlotBB('PM2_Gas_03_Flow_Mon')

b = PlotBB('PM2_Gas_07_Flow_Mon')

b = PlotBB('PM2_Gas_09_Flow_In')

b = PlotBB('PM2_Gas_09_Pressure_Mon')

b = PlotBB('PM2_LWIND_01')

b = PlotBB('PM2_LWIND_07')

b = PlotBB('PM2_ProcChm_Bot_Elec_Temp_Mon')

b = PlotBB('PM2_ProcChm_ESC_Voltage_In')

b = PlotBB('PM2_ProcChm_Pressure_Mon')

b = PlotBB('PM2_RF_27MHz_FwdPwr_In')

b = PlotBB('PM2_RF_27MHz_Match_LoadCap_Mon')

b = PlotBB('PM2_RF_27MHz_Match_TuneCap_Mon')

b = PlotBB('PM2_RF_27MHz_RevPwr_In')

b = PlotBB('PM2_RF_2MHz_FwdPwr_In')

b = PlotBB('PM2_RF_2MHz_RevPwr_In')

b = PlotBB('PM2_Upper_Electrode_Temp_Mon')




#WEBSITE FLASK

app = Flask(__name__)

app.secret_key = os.urandom(24)

'''
@app.route('/')
def index():
    return redirect(url_for('login'))
''' 
 
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
#g is a global variabl which checks for proper user every time

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'bepositive':
            session['user'] = request.form['username']
            return redirect(url_for('source'))
      
    return render_template('Login.txt')
 
@app.route("/logout")  
def logout():
    session.pop('user', None)
    redirect(url_for('login'))
    return 

#IMPORTANT PAGE 

@app.route("/contact") 
def contact():
    return render_template('contact.txt')

@app.route('/data')
def data():
    if g.user:
        return df.to_html() #render_template('data.txt')

#Main
@app.route("/source") 
def source():
    if g.user:
        return render_template('source.txt')    
    

@app.route("/LRC12A")  
def LRC12A():
    if g.user:
        return render_template('LRC12A.txt')

@app.route("/LRC12B")  
  
def LRC12B():
    
    return render_template('underdevlopment.txt')

@app.route("/LRC12C")

def LRC12C():
    
    return render_template('underdevlopment.txt')


@app.route("/LRC12A/DC")  
def LRC12ADC():
    
    return render_template('PM2_DC_Bias_Comp.html')

@app.route("/LRC12A/DCBB")  
def LRC12CDCBB():
    
    return render_template('PM2_DC_Bias_Comp_std.html')



@app.route("/LRC12A/W7")  
def LRC12W7():
    
    return render_template('PM2_LWIND_07.html')

@app.route("/LRC12A/W7S")  
def LRC12W7S():
    
    return render_template('PM2_LWIND_07_std.html')


@app.route("/LRC12A/TM")  
def LRC12TM():
    
    return render_template('PM2_ProcChm_Bot_Elec_Temp_Mon.html')

@app.route("/LRC12A/TMS")  
def LRC12TMS():
    
    return render_template('PM2_ProcChm_Bot_Elec_Temp_Mon_std.html')


@app.route("/LRC12A/VI")  
def LRC12AVI():
    
    return render_template('PM2_ProcChm_ESC_Voltage_In.html')

@app.route("/LRC12A/VIS")  
def LRC12CVIS():
    
    return render_template('PM2_ProcChm_ESC_Voltage_In_std.html')


@app.route("/LRC12A/PM")  
def LRC12PM():
    
    return render_template('PM2_ProcChm_Pressure_Mon.html')

@app.route("/LRC12A/PMS")  
def LRC12CDPMS():
    
    return render_template('PM2_ProcChm_Pressure_Mon_std.html')


@app.route("/LRC12A/27FPI")  
def LRC12FPI():
    
    return render_template('PM2_RF_27MHz_FwdPwr_In.html')

@app.route("/LRC12A/27FPIS")  
def LRC12CFPIS():
    
    return render_template('PM2_RF_27MHz_FwdPwr_In_std.html')


@app.route("/LRC12A/LCM")  
def LRC12LCM():
    
    return render_template('PM2_RF_27MHz_Match_LoadCap_Mon.html')
 
@app.route("/LRC12A/LCMS")  
def LRC12CLCMS():
    
    return render_template('PM2_RF_27MHz_Match_LoadCap_Mon_std.html')


@app.route("/LRC12A/TCM")
def LRCADC():
    
    return render_template('PM2_RF_27MHz_Match_TuneCap_Mon.html')

@app.route("/LRC12A/TCMS")  
def LRC1():
    
    return render_template('PM2_RF_27MHz_Match_TuneCap_Mon_std.html')


@app.route("/LRC12A/RPI")  
def LRC27RP():
    
    return render_template('PM2_RF_27MHz_RevPwr_In.html')

@app.route("/LRC12A/RPIS")  
def LRC12CRVS():
    
    return render_template('PM2_RF_27MHz_RevPwr_In_std.html')


@app.route("/LRC12A/2INFP")  
def LRC12INFP():
    
    return render_template('PM2_RF_2MHz_FwdPwr_In.html')

@app.route("/LRC12A/2INFPS")  
def LRC12INFPS():
    
    return render_template('PM2_RF_2MHz_FwdPwr_In_std.html')


@app.route("/LRC12A/RF2")  
def LRC12AD():
    
    return render_template('PM2_RF_2MHz_RevPwr_In.html')

@app.route("/LRC12A/RF2s")  
def LRC12CDCB():
    
    return render_template('PM2_RF_2MHz_RevPwr_In_std.html')


@app.route("/LRC12A/UET")  
def LRC12UC():
    
    return render_template('PM2_Upper_Electrode_Temp_Mon.html')

@app.route("/LRC12A/UETs")  
def LRC12CUET():
    return render_template('PM2_Upper_Electrode_Temp_Mon_std.html')



if __name__ == "__main__":
    app.run(debug=True,port=5000)
    