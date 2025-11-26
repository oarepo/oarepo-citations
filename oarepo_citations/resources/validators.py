"""Validators for citation parameters."""

import re
from babel import Locale
from babel.core import UnknownLocaleError
from citeproc_styles import get_style_filepath
from citeproc_styles.errors import StyleNotFoundError
from werkzeug.exceptions import BadRequest


def validate_style(style):
    """Validate CSL style parameter.
    
    :param style: Style name to validate
    :returns: Validated style name
    :raises: BadRequest if style is invalid
    """
    if not style:
        return None
    
    # Style names should only contain alphanumeric characters, hyphens, and underscores
    if not re.match(r'^[a-zA-Z0-9_-]+$', style):
        raise BadRequest("Invalid style parameter: only alphanumeric characters, hyphens, and underscores allowed")
    
    # Verify the style exists
    try:
        get_style_filepath(style.lower())
    except StyleNotFoundError as e:
        raise BadRequest(f"Invalid style parameter: style '{style}' not found") from e
    
    return style


def validate_locale(locale):
    """Validate locale parameter.
    
    :param locale: Locale string to validate (e.g., 'en-US', 'cs-CZ')
    :returns: Validated locale string
    :raises: BadRequest if locale is invalid
    """
    if not locale:
        return None
    
    # Try to parse with Babel to ensure it's a valid locale
    # Babel accepts both '-' and '_' as separators
    try:
        # Try parsing with hyphen separator first
        if '-' in locale:
            Locale.parse(locale, sep='-')
        elif '_' in locale:
            Locale.parse(locale, sep='_')
        else:
            # Just language code
            Locale.parse(locale)
    except (UnknownLocaleError, ValueError) as e:
        raise BadRequest("Invalid locale parameter.") from e
    
    return locale
