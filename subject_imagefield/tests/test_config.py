from django.test import TestCase
from subject_imagefield.config import get_config


class ConfigTestCase(TestCase):
    def setUp(self):
        pass

    def test_default_preview_width_retrieved(self):
        """ If not specified a default preview width is retrieved """
        with self.settings(SUBJECT_IMAGEFIELD=None):
            self.assertEqual(get_config('PREVIEW_WIDTH'), 300)

    def test_overridden_preview_width_retrieved(self):
        """ If specified the given preview width is retrieved """
        with self.settings(SUBJECT_IMAGEFIELD={'PREVIEW_WIDTH': 1000}):
            self.assertEqual(get_config('PREVIEW_WIDTH'), 1000)
