from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

NoSpaceValidator = RegexValidator(
      r' ',
      _('No spaces allowed'),
      inverse_match=True,
      code='invalid_tag',
  )