# -*- coding: utf-8 -*-

# Copyright (C) 2005-2009 Osmo Salomaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Names and ISO 639 codes for languages and conversions between them."""

import aeidon
import os

_languages = {}


def code_to_name(code):
    """
    Convert ISO 639 `code` to localized language name.

    Raise :exc:`LookupError` if `code` not found.
    """
    return aeidon.i18n.dgettext("iso_639", _languages[code])

def _init_languages():
    """Initialize the dictionary mapping codes to names."""
    import xml.etree.ElementTree as ET
    path = "/usr/share/xml/iso-codes/iso_639.xml"
    if not os.path.isfile(path):
        # Use local, possibly outdated copy, only as a fallback.
        path = os.path.join(aeidon.DATA_DIR, "iso-codes", "iso_639.xml")
    for element in ET.parse(path).findall("iso_639_entry"):
        code = element.get("iso_639_1_code", None)
        name = element.get("name", None)
        if code is not None and name is not None:
            _languages[code] = name

def is_valid(code):
    """Return ``True`` if `code` is a valid ISO 639 language code."""
    return (code in _languages)


_init_languages()
