# InfoLesson
[![Build Status](https://travis-ci.org/UlstuLyceum/InfoLesson.svg?branch=develop)](https://travis-ci.org/UlstuLyceum/InfoLesson)

Main branch - develop.

### Configuration 
To set configuration for local usage:
1. `cp example_config.py local_config.py`
2. Edit *local_config.py*


### Run the project
Execute `python -m infolesson` to start project

## Code check 
Run from the root of the project
1. ```black infolesson```. Codestyle check
2. ```isort -rc infolesson```. Imports check
3. ```pylint infolesson ```. PEP8 check

Before merging your changes, the pull request will indicate whether your code has passed these checks or not.
(Pylint only checks your code for errors) 


## To add new changed: 
1. Create new branch `git branch new_cool_feature`
2. Go to this branch `git checkout new_cool_feature`
3. Do cool commits just with `git commit`
4. After all the commits push on github with `git push origin new_cool_feature`
5. Create Pull request on GitHub. Merge your changes to develop

## Downloading on local pc:
1. `git clone https://github.com/summer-school-2019/money-bot.git`
2. `python3.7 -m virtualenv .venv` Setting new virtualenv
3. `source .venv/bin/activate` - *nix
   `.venv/bin/activate.exe` - windows (but that's not accurate)
4. `pip install -r requirements.txt`

## Prerequirements

### Black
Format your code itself. After installation go to
`Tools -> External Tools -> Black/isort`
 
Instructions for installing black:
[here](https://github.com/psf/black#pycharmintellij-idea) 

![black config](https://i.ibb.co/cgnr7Cr/image.png)


### Isort
Sort imports in your code itself.


![isort config](https://i.ibb.co/sVn0MFT/image.png)
