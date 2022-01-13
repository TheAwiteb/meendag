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

from pydantic import BaseModel

__all__ = ["Country", "Owner"]


class Country(BaseModel):

    code: str
    """ Country code """

    name: str
    """ Country name """


class Owner(BaseModel):

    name: str
    """ Owner name """

    number: str
    """ Owner number """

    country: Country
    """ Country of number """
