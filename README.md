<div align="center">
  <h1>Meendag-sdk</h1>
  <p>An unofficial SDK for Meendag.com help you to find name of the owner of the number</p>
  <a href="https://pypi.org/project/meendag/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/meendag?color=9cf">
  </a>
  <a href="https://pypi.org/project/meendag/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/meendag?color=9cf">
  </a>
  <a href="https://www.gnu.org/licenses/agpl-3.0.en.html">
    <img src="https://img.shields.io/pypi/l/meendag?color=9cf&label=License" alt="License">
  </a>
  <br>
  <a href="https://github.com/TheAwiteb/meendag/actions/workflows/release.yml">
    <img alt="Upload Python Package" src="https://github.com/TheAwiteb/meendag/actions/workflows/release.yml/badge.svg">
  </a>
  <br>
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
</div>

<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Requirements">Requirements</a>
    </li>
    <li>
      <a href="#Installation">Installation</a>
      <ul>
        <li><a href="#PyPi">With PyPi</a></li>
        <li><a href="#GitHub">With GitHub</a></li>
      </ul>
    </li>
    <li>
        <a href="#Usage">Usage</a>
        <ul>
            <li><a href="#Get-countrys">Get countrys</a></li>
            <li><a href="#Get-owner">Get owner</a></li>
            <li><a href="#Countrys-filter">Countrys filter</a></li>
            <li><a href="#Get-country-by-code">Get country by code</a></li>
            <li><a href="#Get-country-by-name">Get country by name</a></li>
        </ul>
    </li>
    <li><a href="#Discussions">Discussions</a></li>
    <li><a href="#Issues">Issues</a></li>
    <li><a href="#Security">Security</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>


## Requirements

* [Python](https://Python.org/) >= 3.8

## Installation

### PyPi

```bash
$ pip3 install meendag
```

### GitHub

```bash
$ git clone https://github.com/TheAwiteb/meendag/
$ cd meendag
$ python3 setup.py install
```

## Usage

### Get countrys
```python
from meendag import get_countrys

countrys = get_countrys()

for country in countrys:
	print(
		f"Country name: {country.name} {country.code}"
	)
# Country name: المملكة العربية السعودية SA
# Country name: الأردن JO
# Country name: الامارات العربية المتحدة AE
# Country name: البحرين BH
# ...
```

### Get owner
```python
from meendag import get_country_by_code, get_owner
print(get_owner("0138823616", get_country_by_code("SA")))
# Owner(name='Intertek', number='0138823616', country=Country(code='SA', name='المملكة العربية السعودية'))
```

### Countrys filter
```python
from meendag import countrys_filter
print(countrys_filter(lambda country: country.code == "SA"))
# [Country(code='SA', name='المملكة العربية السعودية')]
```

### Get country by code
```python
from meendag import get_country_by_code
print(get_country_by_code("SA"))
# Country(code='SA', name='المملكة العربية السعودية')
```

### Get country by name
```python
from meendag import get_country_by_name
print(get_country_by_name("المملكة العربية السعودية"))
# Country(code='SA', name='المملكة العربية السعودية')
```

## Discussions
Question, feature request, discuss about meendag [here](https://github.com/TheAwiteb/meendag/discussions)

## Issues
You can report a bug [here](https://github.com/TheAwiteb/meendag/issues)

## Security

If you discover any security related issues.

## License

GNU Affero General Public License (AGPL). Please see [License File](LICENSE) for more information.
