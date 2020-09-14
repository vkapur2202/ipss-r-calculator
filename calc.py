from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange
from flask import Flask, render_template, flash

import emoji

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class CalculatorForm(FlaskForm):
  hemoglobin = IntegerField('Hemoglobin', validators=[DataRequired(), NumberRange(min=4, max=20, message='Out of range')])
  neutrophil = IntegerField('Absolute Neutrophil Count', validators=[DataRequired(), NumberRange(min=0, max=15, message='Out of range')])
  platelet = IntegerField('Platelets', validators=[DataRequired(), NumberRange(min=0, max=2000, message='Out of range')])
  bone_marrow_blast = IntegerField('Bone Marrow Blasts', validators=[DataRequired(), NumberRange(min=0, max=30, message='Out of range')])
  cytogenic_category = RadioField('Cytogenetic Category',
    choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Intermediate', 'Intermediate'), ('Poor', 'Poor'), ('Very Poor', 'Very Poor')], validators=[DataRequired()])
  submit = SubmitField('Calculate Prognosis')

def getCytogenicScore(category):
  if category == "very good":
    return 0
  elif category == "good":
    return 1
  elif category == "intermediate":
    return 2
  elif category == "poor":
    return 3
  elif category == "very poor":
    return 4

def getBoneMarrowScore(perc):
  if perc <= 2:
    return 0
  elif 2 < perc and perc < 5:
    return 1
  elif 5 <= perc and perc <= 10:
    return 2
  else:
    return 3

def getHemoglobinScore(val):
  if val >= 10:
    return 0
  elif 8 <= val and val < 10:
    return 1
  else:
    return 1.5

def getPlateletScore(plat):
  if plat >= 100:
    return 0
  elif plat < 100 and plat >= 50:
    return 0.5
  else:
    return 1

def getANCScore(anc):
  if anc >= 0.8:
    return 0
  else:
    return 0.5

def getRiskCategory(riskScore):
  if riskScore <= 1.5:
    return "Very Low"
  elif riskScore > 1.5 and riskScore <= 3:
    return "Low"
  elif riskScore > 3 and riskScore <= 4.5:
    return "Intermediate"
  elif riskScore > 4.5 and riskScore <= 6:
    return "High"
  else:
    return "Very High"

def getTotalScore(attributeArr):
  a = getCytogenicScore(attributeArr[4]) 
  b = getBoneMarrowScore(attributeArr[3]) 
  c = getPlateletScore(attributeArr[2]) 
  d = getANCScore(attributeArr[1]) 
  e = getHemoglobinScore(attributeArr[0])
  return a + b + c + d + e


@app.route('/', methods=['GET', 'POST'])
def calculate():
  form = CalculatorForm()
  error = None
  if form.validate_on_submit():
    total_score = getTotalScore([form.hemoglobin.data, form.neutrophil.data, form.platelet.data, form.bone_marrow_blast.data, form.cytogenic_category.data.lower()])
    risk_category = getRiskCategory(total_score)
    flash("IPSS-R Score: " + str(total_score))
    if risk_category == "High" or risk_category == "Very High":
      flash("IPSS-R Category: " + risk_category + " " + emoji.emojize(":ambulance:"))
    else:
      flash("IPSS-R Category: " + risk_category)

  elif form.errors:
    error = 'Invalid Input. Please check your input and try again.'
  return render_template('calcinator.html', form = form, error = error)

if __name__ == "__main__":
    app.run()