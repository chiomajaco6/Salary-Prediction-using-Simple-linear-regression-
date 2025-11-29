from django.shortcuts import render
from django import forms
import joblib
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'salary_model.pkl')
model = joblib.load(model_path)

# Create the form
class ExperienceForm(forms.Form):
    years_experience = forms.FloatField(label='Years of Experience')

# Create the view
def predict_salary(request):
    prediction = None
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            years = form.cleaned_data['years_experience']
            prediction = model.predict([[years]])[0]
    else:
        form = ExperienceForm()
    return render(request, 'predictor/predict.html', {'form': form, 'prediction': prediction})
