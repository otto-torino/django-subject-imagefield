from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.utils.translation import gettext_lazy as _

from .forms import SubjectImageFormField
from .widgets import SubjectImageInput


class SubjectImageFieldFile(ImageFieldFile):
    @property
    def subject_perc_position(self):
        if self.field.subject_location_field and getattr(
                self.instance, self.field.subject_location_field):
            (cX, cY) = getattr(self.instance,
                               self.field.subject_location_field).split(',')

            return {
                'x': int(cX),
                'y': int(cY)
            }
        return None

    @property
    def subject_position(self):
        perc = self.subject_perc_position
        if perc:
            return {
                'x': self.width * perc.get('x') // 100,
                'y': self.height * perc.get('y') // 100
            }
        return None

    @property
    def sorl(self):
        """ shortcut property to use with sorl-thumbnmail crop featur e"""
        position = self.subject_perc_position
        if position:
            x = position.get('x')
            y = position.get('y')
            # also need -0
            return '%s%% %s%%' % (x, y)
        return '50% 50%'


class SubjectImageField(models.ImageField):
    attr_class = SubjectImageFieldFile

    def __init__(self,
                 verbose_name=None,
                 name=None,
                 width_field=None,
                 height_field=None,
                 subject_location_field=None,
                 **kwargs):
        self.width_field, self.height_field = width_field, height_field
        self.subject_location_field = subject_location_field
        super(SubjectImageField, self).__init__(verbose_name, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(SubjectImageField, self).deconstruct()
        if self.subject_location_field:
            kwargs['subject_location_field'] = self.subject_location_field
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        d = kwargs
        # override widget
        d.update({
            'widget':
            SubjectImageInput,
            'form_class':
            SubjectImageFormField,
            'help_text':
            _('Drag the circle or click on the image to set the image subject'
              ),
            'subject_location_field':
            self.subject_location_field
        })
        return super(SubjectImageField, self).formfield(**d)
