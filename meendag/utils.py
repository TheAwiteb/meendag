# meendag - An unofficial SDK for Meendag.com help you to find name of the owner of the number
# Copyright (C) 2022 - Awiteb <awiteb@hotmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from requests import Response
from bs4 import BeautifulSoup as bs4
from typing import Dict, Optional

__all__ = [
    "parse_countrys",
    "parse_name",
]


def parse_countrys(response: Response) -> Dict[str, str]:
    """Return countrys from response

    Args:
        response (Response): Response have the countrys

    Returns:
        Dict[str, str]: countrys, {country_code: country_name}
    """
    soup = bs4(response.content, "html.parser")
    countrys = {
        lang.attrs["value"]: lang.text
        for lang in soup.find(attrs={"name": "countryCode"}).find_all("option")
    }
    return countrys


def parse_name(response: Response) -> Optional[str]:
    """Return name from response

    Args:
        response (Response): Response have the name

    Returns:
        Optional[str]: name if any
    """
    soup = bs4(response.content, "html.parser")
    name = soup.find(class_="contactName").text.strip()

    if name != "ما لقيت الرقم معليش":
        return name
