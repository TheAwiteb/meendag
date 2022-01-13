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

from typing import List, Optional
from .utils import *
from .types import Country, Owner
from .apihelper import countrys, get_name

__all__ = [
    "get_countrys",
    "get_owner",
    "get_country_by_code",
    "get_country_by_name",
    "countrys_filter",
]


def get_countrys() -> List[Country]:
    """Returns all countrys from meendag

    Returns:
        List[country]: countrys, {country_code: country_name}

    ## Example
    ```python
    >>> from meendag import get_countrys
    >>> countrys = get_countrys()
    >>> for country in countrys:
        print(
            f"Country name: {country.name} {country.code}"
        )
    Country name: المملكة العربية السعودية SA
    Country name: الأردن JO
    Country name: الامارات العربية المتحدة AE
    Country name: البحرين BH
    ...
    ```
    """
    return [
        Country(code=code, name=name)
        for code, name in parse_countrys(countrys()).items()
    ]


def get_owner(number: str, country: Country) -> Optional[Owner]:
    """Returns the name of the owner of the number, if any

    Args:
        number (str): The number
        country (Country): Country of number

    Returns:
        Optional[str]: name of the owner of the number, if any

    ## Example
    ```python
    >>> from meendag import get_country_by_code, get_owner
    >>> get_owner("0138823616", get_country_by_code("SA"))
    Owner(name='Intertek', number='0138823616', country=Country(code='SA', name='المملكة العربية السعودية'))
    ```
    """
    name = parse_name(get_name(number, country.code))
    if name:
        return Owner(name=name, number=number, country=country)


def countrys_filter(func) -> Optional[List[Country]]:
    """Filter countrys by `func`

    Args:
        func (Function): function to filter countrys

    Returns:
        Optional[Country]: Country by filter

    ## Example
    ```python
    >>> from meendag import countrys_filter
    >>> print(countrys_filter(lambda country: country.code == "SA"))
    [Country(code='SA', name='المملكة العربية السعودية')]
    ```
    """
    countrys = list(filter(func, get_countrys()))
    if countrys:
        return countrys


def get_country_by_code(country_code: str) -> Optional[Country]:
    """Returns country by country code

    Args:
        country_code (str): country code

    Returns:
        Optional[Country]: country

    ## Example
    ```python
    >>> from meendag import get_country_by_code
    >>> get_country_by_code("SA")
    Country(code='SA', name='المملكة العربية السعودية')
    ```
    """
    func = lambda country: country.code.lower() == country_code.lower()
    if country := countrys_filter(func):
        return country[0]


def get_country_by_name(country_name: str) -> Optional[Country]:
    """Returns country by country name

    Args:
        country_name (str): country name

    Returns:
        Optional[Country]: country

    ## Example
    ```python
    >>> from meendag import get_country_by_name
    >>> get_country_by_name("المملكة العربية السعودية")
    Country(code='SA', name='المملكة العربية السعودية')
    ```
    """
    func = lambda country: country.name == country_name
    if country := countrys_filter(func):
        return country[0]
