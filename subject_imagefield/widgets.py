from django.forms.widgets import ClearableFileInput


class SubjectImageInput(ClearableFileInput):
    template_name = 'subject_imagefield/widgets/subject_image.html'
