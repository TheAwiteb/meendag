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

from requests import request, Response


url = "https://meendag.com/"
lookup_page = url + "lookup"

__all__ = ["countrys", "get_name"]


def send_request(url: str, method: str, **kwargs) -> Response:
    """Return response of `url` with `method` and pyload `kwargs`

    Args:
        url (str): Url you want send request to it
        method (str): Method of request `GET` `POST` Extra

    Returns:
        Response: The response
    """
    method = method.upper()
    response = request(
        method,
        url,
        params=kwargs if method == "GET" else None,
        data=None if method == "GET" else kwargs,
    )
    return response


def countrys() -> Response:
    """Returns countrys response

    Returns:
        Response: countrys response
    """
    return send_request(url, method="GET")


def get_name(number: str, country_code: str) -> Response:
    """Return response of lookup page

    Args:
        number (str): The number
        country_code (str): The country code

    Returns:
        Response: response of lookup page
    """
    return send_request(
        lookup_page, method="POST", num=number, countryCode=country_code
    )
