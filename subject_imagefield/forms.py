from django.forms.fields import ImageField
from .widgets import SubjectImageInput
from .config import get_config


class SubjectImageFormField(ImageField):
    widget = SubjectImageInput

    def __init__(self, subject_location_field=None, *args, **kwargs):
        self.subject_location_field = subject_location_field
        return super(SubjectImageFormField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(SubjectImageFormField, self).widget_attrs(widget)
        attrs['subject_location_field'] = self.subject_location_field
        attrs['preview_width'] = get_config('PREVIEW_WIDTH')
        return attrs
