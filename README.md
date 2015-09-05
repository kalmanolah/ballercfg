BallerCFG - a totally baller configuration loader
=================================================

BallerCFG is a totally baller configuration file loader which can deal with
multiple formats/directories at the same time.

Currently supported formats include:

* YAML
* JSON
* INI/CFG

Please note that only Python3 is supported.

## Installation

```
pip3 install -U git+https://github.com/kalmanolah/ballercfg.git
```

## Usage

```python
from ballercfg import ConfigurationManager


##
## Load a single configuration file
##
cfg = ConfigurationManager.load('path/to/cfg/file.yaml')

##
## Load multiple configuration files by masking
##
cfg = ConfigurationManager.load('path/to/cfg/*')

##
## Load multiple directories, combined with masks
##
cfg = ConfigurationManager.load(['path/to/cfg/*', '/etc/app/cfg/*'])

##
## Grabbing data from your configuration files
## Example YAML structure:
##
##     config:
##         db:
##             user:  'db-user'
##
value = cfg.get('config.db.user')
# or
value = cfg.get('config.db')['user']

##
## Grabbing data from your configuration files, with defaults
##
value = cfg.get('config.db.user', 'default-user')
```

##License

MIT license.

```
The MIT License (MIT)

Copyright (c) 2014-2015 Kalman Olah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
