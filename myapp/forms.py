from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=30)
    description = forms.CharField(label="Descripcion de la Tarea",widget=forms.Textarea)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo del projecto", max_length=30)