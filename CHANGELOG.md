# Changelog

## 2.0.0-alpha.2 (unreleased)

### WARNING

**Breaking change:** Starting with version the 2.0.0 the category slugs are unique.
While this brings big advantage for simplified category addressing, it can break projects that are containing categories with duplicated slugs.
If your database contains colliding slugs, they will be automatically renamed by the migration.
Three categories with slugs ``foo`` will be renamed to ``foo``, ``foo-1``, ``foo-2``.
If this causes problems in your project, you can rename the categories yourself before running the migration.

- Django 2.1 is no longer supported


## 1.9.4 (2024-04-18)

- Remove dependency on unicode-slugify, use Django builtin function

## 1.9.3 (2024-04-17)

- Update of Django/Python versions.
- Supported versions are now Django 2.1-5.0, Python 3.7-3.12
- Removed code for obsolete versions
- Add support for Django 4.12 new File storage API (STORAGES)

## 1.9.2 (2022-09-22)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.9.1...1.9.2)

### Fixes

- Fix installation from source. [5e0bdeb](https://github.com/jazzband/django-categories/commit/5e0bdebb876ff3b955aae355569ddbde14971490)
    
- Fix installation from source. [5c62a4a](https://github.com/jazzband/django-categories/commit/5c62a4a470450980649928c6f9e5ee443a700760)
    
- Fixed a typo in the pypi publish workflow. [c345618](https://github.com/jazzband/django-categories/commit/c345618eef9b3fd362cc920eb290816300c3eeb7)
    
### New

- Add tests for GenericCollectionInlineModelAdmin. [73142da](https://github.com/jazzband/django-categories/commit/73142dafae57c35ce8bc55db5fe69e3156c9c346)
    
### Other

- [pre-commit.ci] auto fixes from pre-commit.com hooks. [b08da9a](https://github.com/jazzband/django-categories/commit/b08da9aa4777a112d6559619efdb3e8cc2df548d)
    
  for more information, see https://pre-commit.ci
- [pre-commit.ci] auto fixes from pre-commit.com hooks. [4d67f33](https://github.com/jazzband/django-categories/commit/4d67f3372c022cfa6e992fb1b6de68fd94d39f1c)
    
  for more information, see https://pre-commit.ci
### Updates

- Update gen_coll_tabular.html to new Django versions. [d070089](https://github.com/jazzband/django-categories/commit/d0700892c069a6c58c44f61ff4aefada827b67d3)
    


## 1.9.1 (2022-09-21)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.9.0...1.9.1)

### Fixes

- Fixed issues with workflows. [6d55e16](https://github.com/jazzband/django-categories/commit/6d55e16acea8629f1bcea8587f3892ea4bd47c9b)
    
- Fixed bug in the Makefile. [60374fa](https://github.com/jazzband/django-categories/commit/60374fa7f46ef583037bfaf354d7f3431bc30ef5)
    


## 1.9.0 (2022-09-21)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.8.0...1.9.0)

### Fixes

- Fix handling get_table_description in Django 4.1 as well as in DB engines other than sqlite3. [b66777e](https://github.com/jazzband/django-categories/commit/b66777ef708f60f973d333d6e289ca8b101fd553)
    
- Fix "Multiple top-level packages discovered" error with new setuptools. [41d00ff](https://github.com/jazzband/django-categories/commit/41d00ff78a84488dba9f34958d2ffd088e9eb826)
    
- Fixes for Django 4.0. [bd3e807](https://github.com/jazzband/django-categories/commit/bd3e807ac60a9451ab0762ab274ca6534c3cbe16)
    
- Fixed the tests. [45d47ab](https://github.com/jazzband/django-categories/commit/45d47ab6463b5a7deb9392d1cea6df91831c9fc4)
    
- Fixed the MANIFEST.in file. [f470e38](https://github.com/jazzband/django-categories/commit/f470e38cc218ac6eab56ede0de859f9b0ff35060)
    
### New

- Add Django 4.0, Python 3.10, drop Django 1.11 in tox.ini and GitHub actions. [358bbcf](https://github.com/jazzband/django-categories/commit/358bbcf546989ddfec93a2fac283547e10f99cd0)
    
- Added configuration for git user. [e3bed16](https://github.com/jazzband/django-categories/commit/e3bed16a9f5527f2850f5f984d04e177faedb468)
    
- Added ghp-import to requirements. [adf7c78](https://github.com/jazzband/django-categories/commit/adf7c78268520b691085b3b1bd7d6d56e4b04d91)
    
- Added Django to the dev dependencies and docs build. [56a9b4f](https://github.com/jazzband/django-categories/commit/56a9b4f756d948bd0cc40b333b7af13539ff8362)
    
- Adds doc strings for lots of functions. [076debb](https://github.com/jazzband/django-categories/commit/076debb44d6426f05fa804746046b1b0678e7162)
    
- Added TOML support for coverage. [acdae7b](https://github.com/jazzband/django-categories/commit/acdae7b1d4b78ff36bcd3ca07c6b8c251fb23488)
    
- Added requirements to MANIFEST.in. [510b21e](https://github.com/jazzband/django-categories/commit/510b21ee93946b05799766b30c75370e0c4ed1f2)
    
- Added ability to generate a Changelog. [ebefa59](https://github.com/jazzband/django-categories/commit/ebefa59f6eb34776af69e7653cc319d0e4ca1ec6)
    
- Added a .editorconfig file. [0125004](https://github.com/jazzband/django-categories/commit/01250045241b3e4aac9be146c9df11f1a3acccbd)
    
- Added pre-commit configuration and configuration for the tools. [3bfe1ad](https://github.com/jazzband/django-categories/commit/3bfe1ad1313579117bb10921400da68a55a76e0d)
    
- Added XML reporting for code coverage. #164. [5716235](https://github.com/jazzband/django-categories/commit/571623598fb12dbf9fe9f661e3659bf7bc12a037)
    
- Added codecov uploading to Tox. #164. [efd3b0e](https://github.com/jazzband/django-categories/commit/efd3b0e3038d03016ce04c323bef62675399c4ab)
    
- Adds GitHub Actions to run Tox. #164. [3854609](https://github.com/jazzband/django-categories/commit/3854609626d6f280c8e2d6c0dc583cc399cb4a34)
    
- Added contributing documentation. #164. [60669d8](https://github.com/jazzband/django-categories/commit/60669d81b6d0072f567532c8d6cb00ea4856f5db)
    
- Added Jazzband badge to README. [f98f8a1](https://github.com/jazzband/django-categories/commit/f98f8a176111a6adfd621b47fa3fb2089bd7c83f)
    
  Also changed it to Markdown.
### Other

- More Django 4.1 fixes. [d24aab4](https://github.com/jazzband/django-categories/commit/d24aab4d423fa2721461136c07f0d705799e8fe2)
    
- [pre-commit.ci] auto fixes from pre-commit.com hooks. [4f1b9eb](https://github.com/jazzband/django-categories/commit/4f1b9eb0e0c916c250269b575c5cab717174013a)
    
  for more information, see https://pre-commit.ci
- Upgrade Black in pre-commit hook (old version stopped working with click). [192e529](https://github.com/jazzband/django-categories/commit/192e529b5eff9e2df4a04a9e3d33b4deff825789)
    
- Test also in Dango 4.1. [9ffb60f](https://github.com/jazzband/django-categories/commit/9ffb60fa041ab64c37e30b2c54985b85683931e8)
    
- [pre-commit.ci] auto fixes from pre-commit.com hooks. [ac3cd17](https://github.com/jazzband/django-categories/commit/ac3cd17f9e70de3b2ef56bd1dc54bf98c1200eb9)
    
  for more information, see https://pre-commit.ci
- [pre-commit.ci] pre-commit autoupdate. [af2115d](https://github.com/jazzband/django-categories/commit/af2115d7a0fc3d8bfd2e6f264068ab220dbee77b)
    
  **updates:** - https://github.com/timothycrosley/isort → https://github.com/PyCQA/isort

- Adjusted makefile for github action commit. [13b4cdc](https://github.com/jazzband/django-categories/commit/13b4cdc981fe762d4f44d924b089d18f169d6e61)
    
- Debugging the doc generation process. [4d19a7a](https://github.com/jazzband/django-categories/commit/4d19a7a0678965702205f91768d32536b8fa47fe)
    
- Set the django requirement to less than 4. [cd43f6e](https://github.com/jazzband/django-categories/commit/cd43f6e4396ed9604236c7078fa27063425e0fe7)
    
- Installing the dev requirements for doc building. [55be640](https://github.com/jazzband/django-categories/commit/55be640d7aa429e93685548ebf84f39a54893b15)
    
- Marked several files as not executable. [30258ac](https://github.com/jazzband/django-categories/commit/30258ac456baf1d245dbb483ceca1c633893eaa5)
    
- Create requirements.txt for Sphinx. [09d9b59](https://github.com/jazzband/django-categories/commit/09d9b59386f195847db58b7b9e3541abfddc2464)
    
- Use latest version of Sphinx builder image. [57b4d52](https://github.com/jazzband/django-categories/commit/57b4d520a016ab39d043b37487a2fbc679f614d0)
    
- Only build docs using Python 3.9. [482c25f](https://github.com/jazzband/django-categories/commit/482c25f663be48876c4dd0491ba305506ab39b67)
    
- Create python-package.yml. [782431f](https://github.com/jazzband/django-categories/commit/782431f97916b3093884043dabbd199a510a44b9)
    
- Moved some documentation to new places. [8a7f226](https://github.com/jazzband/django-categories/commit/8a7f22618de6822863c6a95e5f055f10e6cd9acd)
    
- [pre-commit.ci] auto fixes from pre-commit.com hooks. [1d7654e](https://github.com/jazzband/django-categories/commit/1d7654e5e138815beb39c62ad14257a57f61b23c)
    
  for more information, see https://pre-commit.ci
- Uodated Makefile to automate the versioning process. [90d154b](https://github.com/jazzband/django-categories/commit/90d154b7435daa3a3946ceb57eeb1bf11e254239)
    
- [pre-commit.ci] auto fixes from pre-commit.com hooks. [5961d6b](https://github.com/jazzband/django-categories/commit/5961d6b80ffcd85e791f7f7c073ae820a1ef985e)
    
  for more information, see https://pre-commit.ci
### Updates

- Updated version replacement. [18aa820](https://github.com/jazzband/django-categories/commit/18aa8201e7e61ffbadd2d0f2eb38b8bf5f1098b8)
    
- Changed changelog generation and version handling. [7b3f540](https://github.com/jazzband/django-categories/commit/7b3f5400a28392df662d690016cc90829da3b4e9)
    
- Update GitHub test config: don't fail fast, use Python 3.10. [653714c](https://github.com/jazzband/django-categories/commit/653714c5bb5d3d13e7c3cd0f95bc62bd9ab62d8b)
    
- Updated the workflow. [82298af](https://github.com/jazzband/django-categories/commit/82298af6bc6683b8a6ae353d5a9e1ce9c626b874)
    
- Remove generated docs and use Sphinx defaults. [ec3e6ba](https://github.com/jazzband/django-categories/commit/ec3e6bab9350e8a6b1248e19f89121dbd4e9a165)
    
- Updated project configurations. [f9a4684](https://github.com/jazzband/django-categories/commit/f9a46848b23b571826f3592ad94031ca60e9e837)
    
  - pre-commit to ignore certain files
  - ignore some documentation errors
- Changed flake8 to use config files. [2d69054](https://github.com/jazzband/django-categories/commit/2d6905486d0c39e27c270df19e540399d1de6781)
    
- Refactored documentation. [8c0c4eb](https://github.com/jazzband/django-categories/commit/8c0c4ebf6ae22c2467dfbc8c1dcdf3f3537a27a3)
    
- Removed the unused get_version call. [4e8002e](https://github.com/jazzband/django-categories/commit/4e8002ecf543cefe37f380768b2d6bd53e317435)
    
- Changed version management to bump2version. [035fdf6](https://github.com/jazzband/django-categories/commit/035fdf693e2304cc48fc2d96170f60706041f400)
    
- Changed the requirements to use chained files. [e377ecc](https://github.com/jazzband/django-categories/commit/e377eccb8cbe3a60a74b2d304514d380d7fcfac6)
    
- Changed codecov uploading pattern. [cacf717](https://github.com/jazzband/django-categories/commit/cacf71737ae2022db013dfebd17c773b16cce81a)
    
- Updated tox to run coverage commands together. [bf8229b](https://github.com/jazzband/django-categories/commit/bf8229b2f2c9fa93d6a7a88f9168a02b0ccc8d66)
    
- Removed Python 3.10 testing until compatibility established. [a1ebb97](https://github.com/jazzband/django-categories/commit/a1ebb970736ad2e91512191fddd84323ae893345)
    
- Updated references to Python 3.10. #164. [d2beca9](https://github.com/jazzband/django-categories/commit/d2beca9c091e7a95a1674da79f84b259c73b4d6a)
    
- Updated gitignore to be more ignorative. [277b491](https://github.com/jazzband/django-categories/commit/277b49134e7a488a21d7431b8fcce682d0e7895e)
    
- Updates URL of the project to Jazzband. #164. [75d2215](https://github.com/jazzband/django-categories/commit/75d221545585bdf0dfa9ae1387341130fc37c303)
    


## 1.8.0 (2020-08-31)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.7.2...1.8.0)

### New

- Add support for Django 3.1. [8337898](https://github.com/jazzband/django-categories/commit/833789891b811fc66ce5ad3fbbbfe07d41417320)
    
  In Django 3.1 the compatibility import of django.core.exceptions.FieldDoesNotExist in django.db.models.fields is removed.

  So we'd have to update the package by replacing:
  from django.db.models.fields import FieldDoesNotExist
  with
  from django.core.exceptions import FieldDoesNotExist
### Other

- Django-mptt 0.11 needed for Django 3.1. [ec89796](https://github.com/jazzband/django-categories/commit/ec89796299dc2f875f415864c98bdfcc6d0d76df)
    
  In Django 3.1 the compatibility import of django.core.exceptions.FieldDoesNotExist in django.db.models.fields is removed. 
  django-mptt should be the latest version (0.11 as of now)
### Updates

- Update the version to 1.8. [3f9109f](https://github.com/jazzband/django-categories/commit/3f9109ffe040ca062930388e86b2c5c8c0ba2d45)
    
- Remove Python 2.7 from the Travis config. [6de15e3](https://github.com/jazzband/django-categories/commit/6de15e36b9593c212f48bffc9a0c7b024c3ff35c)
    
- Update tox tests to run Django 3.1 and removed support for Python 2.7. [7bc44c7](https://github.com/jazzband/django-categories/commit/7bc44c74ff2beb735837217b0b8accb534b91488)
    
## 1.7.2 (2020-05-18)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.7.1...1.7.2)

### Fixes

- Fix #152. [a3a3f81](https://github.com/jazzband/django-categories/commit/a3a3f8106e4c566fd70a913128e202c64df5667e)
    
### Other

- Include missing migration. [3dbc96b](https://github.com/jazzband/django-categories/commit/3dbc96bf3615b085d4bf17e7bc011438a40a4f5d)
    
- Ignore .python-version. [28d1185](https://github.com/jazzband/django-categories/commit/28d118579328df26868ec1595c7676a4bba56555)
    
### Updates

- Update the version to 1.7.2. [2dfbc8e](https://github.com/jazzband/django-categories/commit/2dfbc8ef64ee594b4ee8393e9f294ddc9752a921)
    
- Update publish make task. [40abc68](https://github.com/jazzband/django-categories/commit/40abc68fd708005924b6457c9170ab99ec14fa5d)
    
## 1.7.1 (2020-03-06)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.7.0...1.7.1)

### New

- Add missing migrations. [dd201de](https://github.com/jazzband/django-categories/commit/dd201de641db268d70ca0c04014c0e1fd14bae7d)
    
### Updates

- Update the version to 1.7.1. [ac0f3c3](https://github.com/jazzband/django-categories/commit/ac0f3c39c471efc9981382acbdb0bb8f9d1cf52e)
    
## 1.7.0 (2020-02-04)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.6.1...1.7.0)

### Fixes

- Fixes to Django 3.0. [654dddc](https://github.com/jazzband/django-categories/commit/654dddce81f3957a4c6116740d80c3b9d261d425)
    
### New

- Add newer Django versions to tox.ini. [a88a5f7](https://github.com/jazzband/django-categories/commit/a88a5f78254fef4dfeedca90406208cefeb450c5)
    
### Updates

- Update the version to 1.7. [cd405f4](https://github.com/jazzband/django-categories/commit/cd405f4ba18dcacd08bd6cf0da3a36530907978c)
    
- Update django-mptt. [d7dd985](https://github.com/jazzband/django-categories/commit/d7dd98593a5fec437a64e54395d95b97eb8f45fd)
    
- Update `make publish`. [ddf1330](https://github.com/jazzband/django-categories/commit/ddf13300e9ed122bda7f0f60ee195d1fd4147e2d)
    
## 1.6.1 (2019-06-26)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.6.0...1.6.1)

### Fixes

- Fix Travis so it uses the correct python versions. [7580e6f](https://github.com/jazzband/django-categories/commit/7580e6ff6e447175a37b4b1126df1b5e50665011)
    
- Fix Travis so it works with Python 3.7. [b9dd8fa](https://github.com/jazzband/django-categories/commit/b9dd8fa80a574f337b1f96f10059f91d4ccd7c89)
    
- Fix 'Models aren't loaded yet' warning on import. [61e156b](https://github.com/jazzband/django-categories/commit/61e156b3857c3877b1860b05e212409b94f4ace3)
    
  categories.registration._process_registry was being called in
  categories/__init__.py, but since Django 1.9 it hasn't been possible to
  perform operations with models until the app registry is fully
  loaded. Currently the `AppRegistryNotReady` exception is being caught
  and printed, which means it is never actually executed on load.

  Since this code isn't currently doing anything (other than emitting a
  print() of a warning), I've removed it.
- Fix tests. [abec216](https://github.com/jazzband/django-categories/commit/abec2164f2de3759a1898a61b1d10d080201a573)
    
  Also dropped testing Django 1.10 since django-mptt requires Django>=1.11.
- Fix for TOXENV=py27-lint. [d542684](https://github.com/jazzband/django-categories/commit/d542684e3685f86c02937a0df05449eda18ae041)
    
- Fix for TOXENV=py27-lint. [6aacff3](https://github.com/jazzband/django-categories/commit/6aacff3f4c27ac68ebda14a803bee9f3d70fd5d9)
    
- Fixing model for TOXENV=py36-django110. [579aa2a](https://github.com/jazzband/django-categories/commit/579aa2a8bf3c8ce3bbb3fd0b2a6db66d90fe3ad7)
    
### New

- Adding opts to context for Django version 2 and above. [c53bc77](https://github.com/jazzband/django-categories/commit/c53bc77b8294312f1c571fd1f63a8623581a3027)
    
### Other

- Upgrade build environment to Xenial. [7297154](https://github.com/jazzband/django-categories/commit/72971541f38aa0ea841e4c19e05c16e8073f7e63)
    
  This makes it so Django 2.2 tests should pass
- Switch to tox-travis. [353a6d7](https://github.com/jazzband/django-categories/commit/353a6d7a2279fd8230c3077c29f5fffe3a394274)
    
- Py27-lint test fix. [3993038](https://github.com/jazzband/django-categories/commit/3993038f951f784a527f0174f4ce01fccb92b876)
    
- Test Cases fix. [1dc6d47](https://github.com/jazzband/django-categories/commit/1dc6d473ff9f6a57edde3281e670b5259312ee6d)
    
- Bug Fix : sortable was last argument. [6019c0d](https://github.com/jazzband/django-categories/commit/6019c0dd4f53cdb4bc4a58fa17e7993d8057fbf3)
    
- Django 2.0 support in Admin. [a84bb00](https://github.com/jazzband/django-categories/commit/a84bb00210243ee64fa4523c96af8b71f1fe6467)
    
  TypeError at /admin/categories/category/
  __init__() missing 1 required positional argument: 'sortable_by'
### Updates

- Update the version to 1.6.1. [f9c351b](https://github.com/jazzband/django-categories/commit/f9c351bbddb9f0e212b92bdada4825d79bad2812)
    
- Update Travis build badge. [170498d](https://github.com/jazzband/django-categories/commit/170498d80a68c91f63a0f17ba39250ded2a8691f)
    
- Remove 3.7 from Travis config. [5a4b0a5](https://github.com/jazzband/django-categories/commit/5a4b0a51cc17bec5b69b7052473c4f96b2e9078d)
    
- Remove Python 3.7 for Travis. [ddd7f50](https://github.com/jazzband/django-categories/commit/ddd7f50503ae5936f622568d36276488eb02d67a)
    
  Removing since it doesn't look like it's supported.
- Update travis.yml. [c1a0e3a](https://github.com/jazzband/django-categories/commit/c1a0e3a2884336c344a2b7b8f78efd259984d35c)
    
- Remove skip. [79fec52](https://github.com/jazzband/django-categories/commit/79fec52e9050bbd40831707b574ab3e0342f1a67)
    
- Updated tree editor for typo. [e39b5d2](https://github.com/jazzband/django-categories/commit/e39b5d24a864efcd2f6024263f02cdacf586c075)
    
## 1.6.0 (2018-02-27)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.5.4...1.6.0)

### Other

- Proposes changes based on 366ff74619811505ac73ac5ea2c0096ddab0ac51 and pull request #140 for Django 2.0 to pass CI tests. [a8dc71b](https://github.com/jazzband/django-categories/commit/a8dc71bcb1500ec6e9f8d3c7db304d13fea0b5f7)
    
- Made updates to get everything working with Django 2. [366ff74](https://github.com/jazzband/django-categories/commit/366ff74619811505ac73ac5ea2c0096ddab0ac51)
    
### Updates

- Updated the version. [58ec14f](https://github.com/jazzband/django-categories/commit/58ec14f99bea32e0b279500f0528aa84f370678c)
    
- Updated the Travis CI config. [0e75ba5](https://github.com/jazzband/django-categories/commit/0e75ba5d953d15f796d32eddf1c8a84d03c92801)
    
- Changed from using a string to importing the actual CASCADE function. [f6cd053](https://github.com/jazzband/django-categories/commit/f6cd053f74605937535f06b2fd3a7ad80cc13777)
    
## 1.5.4 (2017-10-12)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.5.3...1.5.4)

### Fixes

- Fix changlist TypeError. Return RequestContext as dict on changelist_view. Based on changes in Django 1.11 (https://docs.djangoproject.com/en/1.11/releases/1.11/#django-template-backends-django-template-render-prohibits-non-dict-context). [926d85a](https://github.com/jazzband/django-categories/commit/926d85a04e4ff0e937e380f591b2ae3b2dd0303e)
    
### Other

- [1.5.4] Made sure example was excluded from packaging. [e770596](https://github.com/jazzband/django-categories/commit/e770596430375fa1dc7732e9cc6cf15568048760)
    
- [1.5.4] Version bump. [0e338c7](https://github.com/jazzband/django-categories/commit/0e338c78d59e9671bd1002204b5ceaf8dcbc68fd)
    
- [-] Updated test settings to test generic relations. [dd23a2d](https://github.com/jazzband/django-categories/commit/dd23a2dba73b25933e1facb2480d54c56f2c2bc9)
    
- [-] Get management commands compatible with Django 1.10+. [9c5ccb8](https://github.com/jazzband/django-categories/commit/9c5ccb8c54208ae101fda7591fd34859a92a3b9e)
    
- [-] Add migrations for simpletext example app. [408e69d](https://github.com/jazzband/django-categories/commit/408e69d010a6b7f55510d8ce0c2929dc1bf9be2b)
    
- [-] Remove old django-cbv reference and adds better error checking in views. [9a71474](https://github.com/jazzband/django-categories/commit/9a71474b152bf0350236665e7bb2d1de750128c9)
    
- [-] Retrieve content types lazily in Generic Relations admin. [5dda534](https://github.com/jazzband/django-categories/commit/5dda5348c004b8d1e2b7416769d2aebd9bd3176a)
    
- [-] Check for a valid session id before trying to save or rollback a transaction. [7fa98fd](https://github.com/jazzband/django-categories/commit/7fa98fd58f59d1fc72cd49499c07070f0ec24bb1)
    
- [-] Added additional test coverage for management commands and views. [63bb31d](https://github.com/jazzband/django-categories/commit/63bb31df408602a4627089ad4233af5a898317a7)
    
- [-] Updated tox and travis configurations to check py2.7 and 3.6 and django 1.8-1.11. [ec4664c](https://github.com/jazzband/django-categories/commit/ec4664c2a3de9e3f075b3a7ea78194e98f691487)
    
- [-] Remove south migrations. [1df724f](https://github.com/jazzband/django-categories/commit/1df724f48d7c4687b87813049cf33f1fc54e64db)
    
- [-] Set decendent_ids to empty list if not saved. [22c5630](https://github.com/jazzband/django-categories/commit/22c5630af244cd4133d7b59d120de7cba2362ebc)
    
- This should have stayed. [254a05d](https://github.com/jazzband/django-categories/commit/254a05d2d41ffbbbe301c770e369559e14fbef2b)
    
- Removing every occurrence of Requestcontext and Context. [829d1cc](https://github.com/jazzband/django-categories/commit/829d1cc522151a9ccc9cbd04e9622ee397be688d)
    
- Django 1.11 compatibility. [af26da6](https://github.com/jazzband/django-categories/commit/af26da610608dc1aedbec93820e7f7b1dd9e72c2)
    
- Support Django 1.11 testing environment. [3c9cb2d](https://github.com/jazzband/django-categories/commit/3c9cb2dec9742230ca480edf3e0c60ae725d0d4a)
    
## 1.5.3 (2017-03-31)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.5.2...1.5.3)

### Fixes

- Fixed a ValueError that happened when trying to save a Category that has a thumbnail. [53b92f3](https://github.com/jazzband/django-categories/commit/53b92f3f0f9198336b0bf3182ecb2f34e46a588f)
    
### Other

- Version bump. [e21c304](https://github.com/jazzband/django-categories/commit/e21c304de1001092d64dec934e371b7caf0e442a)
    
## 1.5.2 (2017-03-29)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.5.1...1.5.2)

### Fixes

- Fixed a unicode error that happens with Python 2.7. [fb0174c](https://github.com/jazzband/django-categories/commit/fb0174c0a81c828d43a564a5747d3c2125e50483)
    
### Other

- Version bump. [5b230ef](https://github.com/jazzband/django-categories/commit/5b230ef4f53d1efb0ff45f76bdfffb4af609dff4)
    
## 1.5.1 (2017-02-17)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.5...1.5.1)

### New

- Added a missing migration. [d5bec42](https://github.com/jazzband/django-categories/commit/d5bec42a092d3dbe79f04d65059b7b31009ea342)
    
### Other

- Version bump. [d71d057](https://github.com/jazzband/django-categories/commit/d71d057a188edd0407fba6f5a01628bb4739d4ca)
    
- Just to be safe - pin it down. [121326d](https://github.com/jazzband/django-categories/commit/121326d3b807b16a13a1ec4f8a2fb5aa663a5418)
    
- Close table tag in templatetag result. [e1d5ed0](https://github.com/jazzband/django-categories/commit/e1d5ed006fbdb34082c749adef2c05741dae2392)
    
  In items_for_tree_result, there's a format_html call which builds HTML via string interpolation. It missed back slash in the closing tag. This commit adds that.
### Updates

- Updated README.rst with svg badge. [9d219eb](https://github.com/jazzband/django-categories/commit/9d219eb7c7ca7decac351f8c916b8b9e9bba5985)
    
## 1.5 (2016-11-14)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.4.3...1.5)

### Other

- Version bump. [47554be](https://github.com/jazzband/django-categories/commit/47554bec2b32bd4229c4328c21bcfb54e131b27c)
    
- PEP8 fixes. [c4f7978](https://github.com/jazzband/django-categories/commit/c4f7978eef0cdf4545f9812cfae3e7b61325bd50)
    
### Updates

- Updated the Travis config to test for Django 1.10. [04739df](https://github.com/jazzband/django-categories/commit/04739dfda987717bf47288d86517bc207246b099)
    
- Updated django-categories to work with Django 1.10. [b2497df](https://github.com/jazzband/django-categories/commit/b2497df2b09cf725ddc57fef0ec5aeca1a1bcfe7)
    
## 1.4.3 (2016-10-21)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.4.2...1.4.3)

### Fixes

- Fixes popup raw_id fields for django versions 8 or greater. [5ad9a2a](https://github.com/jazzband/django-categories/commit/5ad9a2a5cda7afa94a14199c8f78906efbc36751)
    
### Other

- Version bump. [96a0fa0](https://github.com/jazzband/django-categories/commit/96a0fa037fc1999c829f75425ed1e106bd2c9804)
    
## 1.4.2 (2016-04-19)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.4.1...1.4.2)

### Fixes

- Fixed it so display_for_field works with Django 1.8 and 1.9. [30d1eb5](https://github.com/jazzband/django-categories/commit/30d1eb5604c4360dd84b526a3a29a6e024666366)
    
### Other

- Version bump. [ef58cae](https://github.com/jazzband/django-categories/commit/ef58cae61ee8d0c0920302305f019d76896e72fb)
    
## 1.4.1 (2016-03-31)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.4...1.4.1)

### Fixes

- Fixed an exception error that happens when saving a category in the admin. [840ea77](https://github.com/jazzband/django-categories/commit/840ea77f14268d9d8d1558c680533a48148be063)
    
### New

- Added setup.cfg file for creating universal wheel distribution. [f3514b6](https://github.com/jazzband/django-categories/commit/f3514b6e22f9302fad5e68af1ae358fd7d00b3b4)
    
- Added coverage to tox. [1124ec2](https://github.com/jazzband/django-categories/commit/1124ec2a32f1a643b47a2a0926a17b2c10ee129c)
    
- Added some tests to test the admin. [0a1e7db](https://github.com/jazzband/django-categories/commit/0a1e7db9a67a4457efc830ea0cfb60afba1a3b2a)
    
- Added a makefile for common tasks. [6715302](https://github.com/jazzband/django-categories/commit/6715302528b10072a7861f80e7efca1cc3c5830d)
    
### Other

- Version bump. [4c7768f](https://github.com/jazzband/django-categories/commit/4c7768fab2a13e1aabc94a455bb1d99d13982645)
    
- Moved all template settings for the example app into the TEMPLATES Django setting. [f6e7b3f](https://github.com/jazzband/django-categories/commit/f6e7b3f2ff8bb47d5f5f297a203917a8791c2b2d)
    
- Avoid the "Cannot call get_descendants on unsaved Category instances". [410caf8](https://github.com/jazzband/django-categories/commit/410caf8e79b8e03be959fd3aae86a3f30b9801f9)
    ValueError when adding categories in admin interface.
### Updates

- Removed some RemovedInDjango110Warning warnings. [bdb6278](https://github.com/jazzband/django-categories/commit/bdb6278559faccb22ab11471b4634bd3a69de8f2)
    
- Removed contributors from the README since that information is in CREDITS.md. No sense maintaining it two places. [485ff6e](https://github.com/jazzband/django-categories/commit/485ff6e6ddbf3fb2f13b60c72e784834355ca968)
    
- Updated the new in 1.4 information. [06e858b](https://github.com/jazzband/django-categories/commit/06e858bb01d02aa7674f60fd14a65bd8f7b5c0f7)
    
## 1.4 (2016-02-15)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.3...1.4)

### Fixes

- Fixed the max_length setting to use a int instead of a string. [f61e6f6](https://github.com/jazzband/django-categories/commit/f61e6f6f3605326b983110184877e62478844c64)
    
- Fixed a test: file() doesn't work in Python 3, used open() instead. [32144dd](https://github.com/jazzband/django-categories/commit/32144dd77941a9bf892beefc04e89f403c218354)
    
### New

- Added a tox.ini and updated the travis config to work with tox. [78c73d5](https://github.com/jazzband/django-categories/commit/78c73d5b0168e4176c76540f385a77a8d1adfd3c)
    
### Other

- Release 1.4. [1cbc7cf](https://github.com/jazzband/django-categories/commit/1cbc7cf37065b7b2816300b79c4e49120e6c65e5)
    
- Made a bunch of flake8 fixes and also added flake8 testing to Travis and Tox. [64686cd](https://github.com/jazzband/django-categories/commit/64686cdaa836dc4c1eff7ceffe590873c0cc625f)
    
- Switched to using _meta.get_fields() instead of ._meta.get_all_field_names() for compatibility with Django 1.9. [635d055](https://github.com/jazzband/django-categories/commit/635d0550d9c944219c714e23654b866898734937)
    
- Made a fix for backwards compatibility with Python 2. [6f813fd](https://github.com/jazzband/django-categories/commit/6f813fd7a798f20b16cc347e84506a2fbbd5f4e8)
    
- Replaced django.db.models.get_model with django.apps.apps.get_model for future compatibility with Django. [6acea02](https://github.com/jazzband/django-categories/commit/6acea02977d0a0905d5af409829b458100bff76a)
    
- B'' doesn't work under Python 3 in a migration file. [6e54f16](https://github.com/jazzband/django-categories/commit/6e54f1635de30cdd7549445d8c5bbe648d3b5d74)
    
- Switched to importing the correct templatetags that got renamed. [1deb79f](https://github.com/jazzband/django-categories/commit/1deb79f75ba97fd2621132b0ff87feac66d23bce)
    
- Switched form using smart_unicode to smart_text and force_unicode to force_text. [93d97d8](https://github.com/jazzband/django-categories/commit/93d97d805be5ac3e92747cc38c1ddb7c01794bdb)
    
- Switched from using django.db.models.loading.get_model to using django.apps.apps.get_model. [337cca5](https://github.com/jazzband/django-categories/commit/337cca5813fe62a3cfee5c0a426a51777b925ca9)
    
- Upgraded to django-mptt 0.8. [02d6b98](https://github.com/jazzband/django-categories/commit/02d6b984ca1a753d57f5dbd8180d9ded2c3cbbaa)
    
- Switched form using force_unicode to force_text. [87a2209](https://github.com/jazzband/django-categories/commit/87a22098be541fe695149a706804e246394eae0e)
    
- Ran the 2to3 script `2to3 -w .`. [c5c459f](https://github.com/jazzband/django-categories/commit/c5c459fe42a33062961dce041b12e8c29c7b18e3)
    
- Ugettext may cause circular import. [188021e](https://github.com/jazzband/django-categories/commit/188021e568201819b32f211a8ff22de3ea011d76)
    
- Run the test with a different configuration. [8cb979c](https://github.com/jazzband/django-categories/commit/8cb979c0969cc625c6bf9e43fc2144ad4a66127d)
    
- Run the test with a different configuration. [3a238b1](https://github.com/jazzband/django-categories/commit/3a238b17b5d56acf531e9de9c4f05360d7a6c8af)
    
- Use singleton `registry` to import `register_fk` and `register_m2m` since they are members on `Registry` class. [c7344f6](https://github.com/jazzband/django-categories/commit/c7344f6b60a6670e93614b9a8541a67b5ef1a759)
    
### Updates

- Updated admin_tree_list_tags so that EMPTY_CHANGELIST_VALUE has a compatible way of working with Django 1.9 and older versions. [e66df48](https://github.com/jazzband/django-categories/commit/e66df48aab0ad343ffda78492c3984d95f3b29cf)
    
- Updated urls to work without patterns since patterns is being deprecated. [0a5a3ef](https://github.com/jazzband/django-categories/commit/0a5a3efac5613e209573ca9cc0ea74bb8f0e0a90)
    
- Updated settings to remove all the TEMPLATE_* settings and put them into the TEMPLATES dict for Django 1.9 compatibility. [dfc277f](https://github.com/jazzband/django-categories/commit/dfc277f08a2664dd6c9d568f42feaa9042a5679e)
    
- Changed __unicode__ to __str__ on the CategoryBase class for Python 3 compatibility. [600aaef](https://github.com/jazzband/django-categories/commit/600aaef926052e85b49cda38d498c0e11a2826d1)
    
## 1.3 (2015-06-09)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.2.3...1.3)

### Fixes

- Fixes potential double imports in dev and test servers. [dc99eac](https://github.com/jazzband/django-categories/commit/dc99eac19cd20304894259ecdae218953d177b9e)
    
- Fixed a potential issue with double-loading of the dev server. [8dda6ec](https://github.com/jazzband/django-categories/commit/8dda6ec87b911dbdab74eacc1a52aa34decdaf40)
    
- Fixes a conflict with treebeard. They stole the name admin_tree_list. [dd60aeb](https://github.com/jazzband/django-categories/commit/dd60aebf283118762bca17e9aa57b3aef8746855)
    
- Fixed the RemovedInDjango19Warning deprecation warning. [74cc9f8](https://github.com/jazzband/django-categories/commit/74cc9f8346a894b4d50adbf6d9877bde18616f56)
    
- Fixed tests so they run under Django 1.7. [70abc1c](https://github.com/jazzband/django-categories/commit/70abc1c80797faa5df8aa8163c90e671bdd1d897)
    
### New

- Added the fields property with it set to '__all__' in order to not get the RemovedInDjango18Warning. [9822ba8](https://github.com/jazzband/django-categories/commit/9822ba8cbb4de18543ebdacc3338593963bd17a1)
    
### Other

- Version bump to 1.3. [cf79d1b](https://github.com/jazzband/django-categories/commit/cf79d1ba7a1f50894e50cb3c6d7640a6e95f5157)
    
- Defaulting the url prefix to / if it can't find the category tree. [addb0e4](https://github.com/jazzband/django-categories/commit/addb0e410fb23cb2dd712bfd1fde2b0b5fbafcea)
    
- Version 1.3b8: Fixes some migrations. [7f8e303](https://github.com/jazzband/django-categories/commit/7f8e303a956d462cecb048f5d033e0f721c5484f)
    
- Version 1.3b7 - fixes registration when there is no app config. [02780ba](https://github.com/jazzband/django-categories/commit/02780ba2a11272abc01166a4bb0a3c94f92fad79)
    
- Version bump to 1.3b6. [e841de7](https://github.com/jazzband/django-categories/commit/e841de7acad1e49d521850a3d6643892d9c9c850)
    
- Version bump to 1.3b5. [7cc0c99](https://github.com/jazzband/django-categories/commit/7cc0c9987e80679adb5a9dc012c1b9af8276463a)
    
- Dramatically refactored how migrations are performed to work with Django 1.7. [acff7f0](https://github.com/jazzband/django-categories/commit/acff7f02a344a63cc5b5d32adc70fd4f470787f4)
    
- Removing outdated settings and updating outdated files. [7c73bd5](https://github.com/jazzband/django-categories/commit/7c73bd51c42f7b4aed982659118270b104dad827)
    
- Version bump to 1.3b4. [6eb306d](https://github.com/jazzband/django-categories/commit/6eb306d715c9ea34ae2c95368195b52ecd2d2d52)
    
- Changing migration dependency of contenttypes to 0001_initial for support for Django 1.7. [c6b7cdd](https://github.com/jazzband/django-categories/commit/c6b7cdd52087936eb80f89a62d86e4c09101e095)
    
- Version bump to 1.3b1. [87f9859](https://github.com/jazzband/django-categories/commit/87f985992bef328ca7fc35740044d4cc1281e638)
    
- Small fixes in some fields. [69bf632](https://github.com/jazzband/django-categories/commit/69bf632a034067b8e109670739a6f41ab9d437b4)
    
- [-] Missed some migrations. [678e845](https://github.com/jazzband/django-categories/commit/678e84504d1d5c121b987eff6e246ac5b6a0082d)
    
- [-] Fixed some tree editor and generic collection issues. [4f51f96](https://github.com/jazzband/django-categories/commit/4f51f96d5c4c3f16cf4984b477c393e3df301849)
    
- [-] Migrations updates. [e0676d4](https://github.com/jazzband/django-categories/commit/e0676d4f25ceaf0b612a788a0715abf65bcbb4c2)
    
- [-] 1.6/1.7/1.8 compatiable changes (WIP). [a6443ad](https://github.com/jazzband/django-categories/commit/a6443ada8555621c5088332c2a3f114da12e95f5)
    
- I18n: add french translation. [ab31c29](https://github.com/jazzband/django-categories/commit/ab31c293508d56c127a072078bd3358d6bfee0cd)
    
### Updates

- Updates the existing migration to south_migrations. [28ef4d5](https://github.com/jazzband/django-categories/commit/28ef4d5565cd0cf1527d7b8a537e9f217c3a70ba)
    
- Renamed get_query_set to get_queryset to get Django categories to work in Django 1.7. I'm not sure of a good way to make this work in Django 1.6. [58abcc7](https://github.com/jazzband/django-categories/commit/58abcc7401d8d0b9e57644443790c138d5f18e22)
    
## 1.2.3 (2015-05-05)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.2.2...1.2.3)

### Fixes

- Fix unicode slug issue. [703a036](https://github.com/jazzband/django-categories/commit/703a036bf58bc51f1f7d69c2400f3205eb1a222c)
    
### Other

- Version 1.2.3: Added a new way to register models manually. [b75f112](https://github.com/jazzband/django-categories/commit/b75f11213cd19598dd40b5f16a000c2a0a0be4b5)
    
- Bootstrap class on table (important for django-suit). [f02e06e](https://github.com/jazzband/django-categories/commit/f02e06ea99df6cd007d9819b1995d643444d7d8d)
    
- Using custom model in CategoryDetailView. [451af0e](https://github.com/jazzband/django-categories/commit/451af0e05457b92d685cfcb9e12e3f33a979f1da)
    
### Updates

- Update requirements. [588815a](https://github.com/jazzband/django-categories/commit/588815acc3dadaec6dd34d3918ae5a5e0df20d50)
    
## 1.2.2 (2013-07-07)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.2.1...1.2.2)

### Fixes

- Fixing migration script for adding fields. [7096d8a](https://github.com/jazzband/django-categories/commit/7096d8a3ebb2456f233c40fb564c5fd351624a8a)
    
### Other

- Version 1.2.2. [a254fe9](https://github.com/jazzband/django-categories/commit/a254fe9087d50f08c421dd040c40b0c528481d7d)
    
- Italian localization. [6c3d305](https://github.com/jazzband/django-categories/commit/6c3d305c11a89e55b177f3fddd8ee8f8d22bd049)
    
- Version 1.2.1: Fixed i18n and failing test in Django 1.4. [a232b8e](https://github.com/jazzband/django-categories/commit/a232b8e6e3a4c6379187da0816f300947c199a0a)
    
- Load I18N templatetags. [1d01494](https://github.com/jazzband/django-categories/commit/1d01494ff58213eaa782c3a1e65ad641c9276c50)
    
## 1.2.1 (2013-03-22)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.2...1.2.1)

### Other

- Version 1.2.1: Fixed i18n and failing test in Django 1.4. [a5181a4](https://github.com/jazzband/django-categories/commit/a5181a44fa5a39648a1ea2a4309f780af8f86c34)
    
## 1.2 (2013-03-20)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.1.3...1.2)

### Fixes

- Fixing a few minor Django 1.5 incompatibilities. [c6f122d](https://github.com/jazzband/django-categories/commit/c6f122d72433596b13bb027d86340b41cf0cc574)
    
- Fix for Django 1.5: {% url %} parameter needs to be quoted. [8ce56e8](https://github.com/jazzband/django-categories/commit/8ce56e8190b5a47019ed2436a7b2f88cf6de3ab7)
    
- Fixing a merge conflict. [0be7d5e](https://github.com/jazzband/django-categories/commit/0be7d5e41f375cee7cc4e23ffcbc380745bcb1b2)
    
- Fixed an exception error. [f55f131](https://github.com/jazzband/django-categories/commit/f55f131655a63f85ecf7b62dc51dc5dbb62fcef0)
    
  Fixed an exception error that occurs when an empty form is submitted for apps that are created using categories.base.CategoryBase.
### New

- Added admin settings documentation. [073b09a](https://github.com/jazzband/django-categories/commit/073b09a7b338fa19048509cdcdf6e4792cc18a92)
    
- Added customization of admin fieldsets. [0f2f24d](https://github.com/jazzband/django-categories/commit/0f2f24d2ce17017d8077bc5fc32081e7f54821a6)
    
### Other

- Version bump 1.2. [63eefee](https://github.com/jazzband/django-categories/commit/63eefeeaf1bfc4dfe90903e03348ee78c617c247)
    
- Updating the admin template to support the latest django admin code. [7232937](https://github.com/jazzband/django-categories/commit/7232937014bce06434ee17c393e82a1639be2c8d)
    
- I18n. [89c7333](https://github.com/jazzband/django-categories/commit/89c733330617c9964ac8e25469274a4dbcb3eda2)
    
- German translation. [591680a](https://github.com/jazzband/django-categories/commit/591680a24e8d9de657b6df83bcaf55b865f95edb)
    
- 1.5 compat: remove adminmedia templatetag calls. [1d7463d](https://github.com/jazzband/django-categories/commit/1d7463db2a1b7e4922a05a8c1278edbce9cc690d)
    
  See https://docs.djangoproject.com/en/1.5/releases/1.5/#miscellaneous
- Made it so django-categories works with Django 1.5 and Grappelli 2.4.4. [6956516](https://github.com/jazzband/django-categories/commit/69565161ff304d7039544fe8a52c0660d818ecb3)
    
- Version bump to 1.1.4. [96748af](https://github.com/jazzband/django-categories/commit/96748afeb4b83df49b45f5f470e5ef517cc8ef8d)
    
- Simplified the assignment of the IS_GRAPPELLI_INSTALLED variable. [8a621e9](https://github.com/jazzband/django-categories/commit/8a621e9d145be2b187ccd09bd6a96e421cc5ea4e)
    
- Made updates so django-categories works with django-grappelli. [85fb208](https://github.com/jazzband/django-categories/commit/85fb2083bbfd9ce4251d89dbe23471d7bc39c936)
    
### Updates

- Update categories/templatetags/category_tags.py. [fb6fb4e](https://github.com/jazzband/django-categories/commit/fb6fb4e6f513d0452622863b058e34c717157f5a)
    
  Added NoneType check to display_drilldown_as_ul on line 188 to fix NoneType error.
- Update categories/templatetags/category_tags.py. [59c3e27](https://github.com/jazzband/django-categories/commit/59c3e27134e05e876b1b72ab544b3535b07b483f)
    
  Added str() to line 49 to fix an error where .strip("'\"") in get_category is getting called on a non-string category_string.
- Update categories/templatetags/category_tags.py. [bdb1d68](https://github.com/jazzband/django-categories/commit/bdb1d68beac20f02eab986a50b6cfe0fc1026b01)
    
  Added str() to line 49 to fix an error where .strip("'\"") in get_category is getting called on a non-string category_string.
- Updated the code so it will work with or without Grappelli installed. [ff6043d](https://github.com/jazzband/django-categories/commit/ff6043d2b3f6c90db7c01178aac57f9175698f3d)
    
## 1.1.3 (2012-08-29)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.1.2...1.1.3)

### Other

- To satisfy a very demanding and owly jsoa, I removed an unused variable. :P. [123459e](https://github.com/jazzband/django-categories/commit/123459eec1b9fcea8cdf0d84b05d935b86db5848)
    
- Updating the signal registration to check for south first and fail silently. [0d16716](https://github.com/jazzband/django-categories/commit/0d167164a1b3ca2ac25be2ded4b5187428e66289)
    
- Version bump to 1.1.3. [2b4512b](https://github.com/jazzband/django-categories/commit/2b4512beaef0968f741547d7aff635294eb94bbd)
    
- Moved the registration of the signal to models.py where it will get executed. [c522ae6](https://github.com/jazzband/django-categories/commit/c522ae6d9642a7c3e64444e0dc9c577ac9155faa)
    
### Updates

- Refactored the migration script to use the syncdb signal. The post_migrate signal only fires for south-managed apps, so it isn't as useful. [e41623b](https://github.com/jazzband/django-categories/commit/e41623b4ade8236971c93e5f5bd4489df49d64b1)
    
## 1.1.2 (2012-08-18)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.1...1.1.2)

### Fixes

- Fixed a bug in the compatibility layer. [d33d9f9](https://github.com/jazzband/django-categories/commit/d33d9f9c552a54b3e81c2700d64edaad2bb748de)
    
### New

- Added travisci. [5f1b280](https://github.com/jazzband/django-categories/commit/5f1b280fa46513e20ef9347368f5b25919fac296)
    
### Other

- Version bump to 1.1.2. [18ab6a4](https://github.com/jazzband/django-categories/commit/18ab6a49a15f63ac23c6cb2963a3096d880aa2f3)
    
- Can't use the m2m tests because it conflicts with the fk tests. [0467d30](https://github.com/jazzband/django-categories/commit/0467d3043428e025138e634a03d74be0a52add74)
    
- Placing some south imports into try blocks. [8be19c8](https://github.com/jazzband/django-categories/commit/8be19c893a9bd1f43f751e5681acf953aa1fe14e)
    
- Capitalizing the various REGISTRY settings. [7fa53a7](https://github.com/jazzband/django-categories/commit/7fa53a7003d6442a1d5caba8d735e7bb277ca56d)
    
- Version bump to 1.1.1 final!. [e0212bb](https://github.com/jazzband/django-categories/commit/e0212bb0304c3142e89eca3dd2d7f509b22535e6)
    
- Version bump to 1.1.1. [7d34853](https://github.com/jazzband/django-categories/commit/7d3485309db916973cf997b892ebce7c0cf7607c)
    
- Minor tweak to tempatetag tests. [8f202fa](https://github.com/jazzband/django-categories/commit/8f202fa9e34b8cc8a9f109e94503f2583a098bbd)
    
- TravisCI stuff. [64936c8](https://github.com/jazzband/django-categories/commit/64936c81ce82236bf9a8fae5a4634d11be7e7475)
    
### Updates

- Refactored the registration of fields from __init__ to a new module. [d63828e](https://github.com/jazzband/django-categories/commit/d63828ebf6799de0e453337950c38193a5e0730a)
    
  It also makes it easier to test.
## 1.1 (2012-07-13)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.0.3...1.1)

### Fixes

- Fixed an incorrect include in the example. [53a203a](https://github.com/jazzband/django-categories/commit/53a203aad20826ec96ba28ea5ed06869ac3437ec)
    
- Fixed some Django 1.4 cosmetic issues. [86d9b37](https://github.com/jazzband/django-categories/commit/86d9b376e1167f5605706108b13651abfc8818df)
    
- Fixes Pull Request #37 Adds notification in the readme regarding issue with South version 0.7.4. [2a501a3](https://github.com/jazzband/django-categories/commit/2a501a39a2fed168efd07c714867ea6d464e11d0)
    
- Fixed format error. [0fa751b](https://github.com/jazzband/django-categories/commit/0fa751b7871a41d783dd34723944c9387f25dcf7)
    
- Fixes issue #40 Checks for instance of CategoryBase instead of Category. [d1edc78](https://github.com/jazzband/django-categories/commit/d1edc78d74621c23a388778d49c14ba572cf046f)
    
  There are still some template tags that won't work with subclasses. Need a better solution for those tags.
### New

- Added Brad Jasper to the credits and updated Jonathan's github account. [b4a2dbe](https://github.com/jazzband/django-categories/commit/b4a2dbef75ab85578adf99491b928db410510d98)
    
- Added queryset parameter to ChangeList.get_ordering(). [60907de](https://github.com/jazzband/django-categories/commit/60907deaf7ed6484555acfe8d54210da6932d7c3)
    
### Other

- Template tags now work with any derivative of CategoryBase. Recognizes the "using" param to specify the model to use. [3a71754](https://github.com/jazzband/django-categories/commit/3a71754a6ae615aa1e987756dd6b110c0dc4da1c)
    
- Pep8 cleanup. [0d254ec](https://github.com/jazzband/django-categories/commit/0d254eca63f59a7610e7d52cf5cae1b5aac00dff)
    
- Sorry, typo in documentation. [9aa6ce7](https://github.com/jazzband/django-categories/commit/9aa6ce705832ddc4c8f5c937052a1e7ad3da8b87)
    
- Documented the upgrade path from 1.0.2 and 1.0.3 plus a small migration to keep things in sync. [8e1ee59](https://github.com/jazzband/django-categories/commit/8e1ee5972200a3e90b664b86514221ba17e85efc)
    
- Stylistic fixes and docs. [bb544e3](https://github.com/jazzband/django-categories/commit/bb544e303464eaa270cc90a21f26f1ccaedcde05)
    
- Make it optional to register in admin. [12859ad](https://github.com/jazzband/django-categories/commit/12859ad902bbbcfe51f2271660283e1c5c597a24)
    
- Use ugettext_lazy. [97df742](https://github.com/jazzband/django-categories/commit/97df7427a94ef194a16f44f056f9996382043142)
    
- Bunped version to 1.0.4 final. [b49c8d1](https://github.com/jazzband/django-categories/commit/b49c8d1814f5887c4fe71fd5262be53aeec0316d)
    
- Minor fix to example app. [0e7e7bb](https://github.com/jazzband/django-categories/commit/0e7e7bbbf45ee520318cec03cef2b1565a410c77)
    
- Version bump to 1.0.4b2. [3074728](https://github.com/jazzband/django-categories/commit/3074728ac324a6060a63237254b71823101a6c29)
    
### Updates

- Updated read me and version bump to 1.1. [e588f33](https://github.com/jazzband/django-categories/commit/e588f33c990ba1e42e3e1d6ab62a3d272ae1dabc)
    
- Updated and rendered docs. [234bc9f](https://github.com/jazzband/django-categories/commit/234bc9f96369e633999c3a07e87fafcae3ebfdb3)
    
- Update to template tags to include ways to retrieve an object from a model other than Category. [fa470df](https://github.com/jazzband/django-categories/commit/fa470df0a7435b27de4f680423b498afe03f2fd7)
    
- Updated the credits to add Iacopo Spalletti. [b4d07bf](https://github.com/jazzband/django-categories/commit/b4d07bfb9ee49c6d39d1c802d1a3d53a180105d9)
    
- Updated CREDITS, docs and bumped version to 1.0.5. [895a503](https://github.com/jazzband/django-categories/commit/895a503eda147061e7c22303ccd717464e2c4872)
    
## 1.0.3 (2012-03-28)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.0.1...1.0.3)

### Fixes

- Fixed another migration	. [5a878c0](https://github.com/jazzband/django-categories/commit/5a878c06b6c94ffff35adeccb47fc44bc4a20a3f)
    
### New

- Adding additional migrations to fix potential data corruption when renaming the foreign key	. [3ee569a](https://github.com/jazzband/django-categories/commit/3ee569a0606efa4840e4328c1711faf9cdd48c55)
    
### Other

- Version bump to 1.0.3. [ce13a18](https://github.com/jazzband/django-categories/commit/ce13a1878f462bbb11141e4de33b17a5fb7249ab)
    
- Altering the #10 migration as it caused strange behavior with data. [43f7ff7](https://github.com/jazzband/django-categories/commit/43f7ff768dbd30fa21365ffd59b7bb8a65267373)
    
## 1.0.1 (2012-03-09)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.0.2...1.0.1)

### Other

- Importing get_model directly from the loading module appears to fix certain edge cases. Version bump to 1.0.2. [d2f5d4d](https://github.com/jazzband/django-categories/commit/d2f5d4da3f9dbdf16a317d4462226de3d7f60205)
    
## 1.0.2 (2012-03-06)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/1.0...1.0.2)

### Fixes

- Fixed how the activate/deactivate methods in the admin fetched their models. [6ce2a49](https://github.com/jazzband/django-categories/commit/6ce2a49d2ed4074b24d4be56a578f7169354ed00)
    
- Fix for django 1.4 compatibility. [f3cc72a](https://github.com/jazzband/django-categories/commit/f3cc72a76b1fe6a44eadaede03365808d98abe2c)
    
### Other

- Updating doc rendering to 1.0.2. [fe20c70](https://github.com/jazzband/django-categories/commit/fe20c70eb2ee08a2b536428b08a6c529054d2a5c)
    
- Version bump to 1.0.2. [79afb07](https://github.com/jazzband/django-categories/commit/79afb07ced024852f8e28310cadf8af04b6c4ca4)
    
### Updates

- Removed an errant print statement. [d194974](https://github.com/jazzband/django-categories/commit/d1949746350d9b02013de668ad299d6d49a889e6)
    
## 1.0 (2012-02-15)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.9...1.0)

### New

- Added compatibility with Django 1.4. [7f48b70](https://github.com/jazzband/django-categories/commit/7f48b70478fd75e22b376f04c730794f48bd091b)
    
- Addresses issue #27; updated musicgenres.json. [f6c06a2](https://github.com/jazzband/django-categories/commit/f6c06a2bf6e8748bd55c72020f9a21fa785e5a53)
    
### Other

- Updating docs to correct and simplify the simple custom categories instructions. [3965ee2](https://github.com/jazzband/django-categories/commit/3965ee2fa9e098ff0e7ddbe9c8efe5916ae5955f)
    
- Version bump to 1.0b2. [8abf984](https://github.com/jazzband/django-categories/commit/8abf9840c15fa6d372630d2b5b1f822d0dec44d7)
    
- The admin prior to 1.4 requires a different result from get_ordering. [6d44ee2](https://github.com/jazzband/django-categories/commit/6d44ee2d62c202534e0cbad6d643785929b6517d)
    
- Formally fixes #1 by adding the ability to specify a transliteration function. [97c14b1](https://github.com/jazzband/django-categories/commit/97c14b19ea941b57929a74bee39e97b456c48d41)
    
- Allow the setting of a SLUG_TRANSLITERATOR to convert non-ASCII characters to ASCII characters. [96a3f61](https://github.com/jazzband/django-categories/commit/96a3f61928003866d30788a37c9a50c5f8e5458b)
    
- Version bump to 1.0b1. [65ef584](https://github.com/jazzband/django-categories/commit/65ef584cf475c8c83c3381a410a78f1a971e247b)
    
- Also fixes #30 by including the editor's media. [88e1a49](https://github.com/jazzband/django-categories/commit/88e1a4990e3ed3184ff18e614e12b42c82ca27d1)
    
- Test of the CategoryBase class subclassed without extras. [7120668](https://github.com/jazzband/django-categories/commit/7120668df6252dc725de04f0e184ac6a182f85d8)
    
- Moved the base models to base.py and did a few PEP8 cleanups. [768291d](https://github.com/jazzband/django-categories/commit/768291d72024a40c04919064172a8ac07bf2a8a0)
    
- This fixes #31. [7428f87](https://github.com/jazzband/django-categories/commit/7428f873949be650d53a53dd0a568f721df4405a)
    
  * Uses the incorrect version segment. Although it works in 1.4a1, it is not perfect.
- Moved the base classes to a new file to isolate them. [3b0cf8d](https://github.com/jazzband/django-categories/commit/3b0cf8da4c2c37787b86bd5c7c04c0f33aafe9ae)
    
- Extracted a base class for categories to allow other apps to make their own independent category-style models. [fdf968f](https://github.com/jazzband/django-categories/commit/fdf968fb6e0aead56b877f483bfd9d110798e2f4)
    
  * Updated for django-mptt 0.5.2
  * Fixed typo in the CategoryRelation field in that the foreign key is called 'story'
  * Made the order field non-null and default to 0
  * Changed the parent foreign key a TreeForeignKey (for 0.5.2)
  * Changed requirements to mptt>=0.5.2
  * Added a migration for model changes.
### Updates

- Removed the __init__ method for the treechange list. Don't need it and it varies too much by django version. Version bump to 1.0final. [5487447](https://github.com/jazzband/django-categories/commit/5487447260b39fc420613f27f23bef88a96220de)
    
- Updated documentation for 1.0b1. [09175c7](https://github.com/jazzband/django-categories/commit/09175c7ef45f3eaa351a44834a36bcb852bab742)
    
- Refactored the admin into a base class for subclasses. [c69047d](https://github.com/jazzband/django-categories/commit/c69047d2596f90111dafcca197b280f83571ca49)
    
- Updated migrations to include a data migration. [3cfc812](https://github.com/jazzband/django-categories/commit/3cfc8124104a5a075902c843782a7f960b8c9f85)
    
- Updated the default view caching to 600, which is the django default instead of forcing the views to NEVER cache at all. [84f84e1](https://github.com/jazzband/django-categories/commit/84f84e10c83023a7015ac1368b0141b4e8dfbf3d)
    
## 0.8.9 (2012-02-06)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.7...0.8.9)

### Fixes

- Fixes issue #30; includes static directory when packaged. [2ea3d23](https://github.com/jazzband/django-categories/commit/2ea3d2337e4726ef6ce106cbf2371aedf3adc156)
    
### Other

- Moved the editor app so its inside the categories app. [07f698c](https://github.com/jazzband/django-categories/commit/07f698c63803a724f5c9f75a80943198ff682f23)
    
### Updates

- Updated the docs. [9cc23f5](https://github.com/jazzband/django-categories/commit/9cc23f59b43118bb372bb544e7527bad8fdc1864)
    
## 0.8.7 (2012-01-05)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.6...0.8.7)

### Other

- Version bump to 0.8.7. [f6502f4](https://github.com/jazzband/django-categories/commit/f6502f45a3a3a1b14a151d198be3d4e85c1d342c)
    
### Updates

- Changed behavior of (de)activating an item within the change form:. [416898d](https://github.com/jazzband/django-categories/commit/416898d2a5f1663706f9d764f8d5278b4b4e35a9)
    
  Instead of changing all descendants' active status to the current item's, it will only change the descendants' active status if the item is False.

  As it makes sense to have an item active, but its children inactive, it doesn't make sense that an item is inactive, but its descendants are active.

  This doesn't change the activate/deactivate admin actions. They will always  affect an item and its descendants.
## 0.8.6 (2012-01-03)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.5...0.8.6)

### Fixes

- Fixes #13 : Documented installation and re-rendered the docs. [7a9ee67](https://github.com/jazzband/django-categories/commit/7a9ee6785b71aa4672ccb9ee825f0234a44bb2e1)
    
- Fix missing imports. [798d20d](https://github.com/jazzband/django-categories/commit/798d20da3d4fa922358b1dfd632a63f5a95aa213)
    
### New

- Added a django/jQuery stub for previous versions of Django. [690111e](https://github.com/jazzband/django-categories/commit/690111e1baeb0fc4f61edbf2034d89c39da337d4)
    
- Added David Charbonnier to the credits. [38255ba](https://github.com/jazzband/django-categories/commit/38255bafbde7ba3551041714f057c18f8718d618)
    
### Other

- Bumped the version number to 0.8.6 and altered the get_version a bit. [06713d7](https://github.com/jazzband/django-categories/commit/06713d780375c4891c5a116f81f8c1be86e98511)
    
- Altered the field type of the alternate url field from URL to Char. This allows relative urls, instead of full urls. [6f6241c](https://github.com/jazzband/django-categories/commit/6f6241c2642766754520e7a6797140efe9da64f6)
    
  Added a migration in case the database complains. Really doesn't do anything on that level
## 0.8.5 (2011-11-03)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.4...0.8.5)

### Fixes

- Fixes issue #26 by limiting the slug to the first 50 characters. [e0365e8](https://github.com/jazzband/django-categories/commit/e0365e838260a1387517e218cab7df9c57cc06df)
    
### Other

- Version Bump to 0.8.5. [40f4d19](https://github.com/jazzband/django-categories/commit/40f4d19b82c2ec75ca8e5395b8c5df02bba38374)
    
## 0.8.4 (2011-10-14)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.3...0.8.4)

### New

- Added a version check to support Django 1.1 in a core Django function. [586fefe](https://github.com/jazzband/django-categories/commit/586fefed7918b7edea955801e8460fff6990f3ae)
    
### Other

- Bumped version to 0.8.4. [c035945](https://github.com/jazzband/django-categories/commit/c0359454ec51f7fbe08eb4caa6d76d444ef24f82)
    
## 0.8.3 (2011-10-13)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.2...0.8.3)

### Other

- Version bump to 0.8.3. [432fcca](https://github.com/jazzband/django-categories/commit/432fccae1201856a9dead7856690258b46dd8375)
    
- Activate and Deactivate of a child no longer (de)activates their parent. [ac11741](https://github.com/jazzband/django-categories/commit/ac117419bac47808b93b8c49980388ab33cad95a)
    
  The query set includes the entire hierarchy. So manually get the categories based on the selected items. Then do them and their children
### Updates

- Remove the delete action from the available actions. [a883e69](https://github.com/jazzband/django-categories/commit/a883e69451d057fe19f8f3990618fcd9f6a6800b)
    
## 0.8.2 (2011-09-05)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8.1...0.8.2)

### Fixes

- Fix Issue #25 : The override of __getitem__ was causing issues with analysis of query sets,. [e4f3e93](https://github.com/jazzband/django-categories/commit/e4f3e9384882fcacf083e4f0231450d8fb1fb313)
    
### Other

- Version bump to 0.8.2. [fdbb084](https://github.com/jazzband/django-categories/commit/fdbb08431e4b3d8bc1c45ea2c5972da0d881becb)
    
### Updates

- Updated docs adding usage in templates and rendered. [c676fc1](https://github.com/jazzband/django-categories/commit/c676fc1c8dbc92afaef9760f022b7bde5e9db076)
    
## 0.8.1 (2011-08-29)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.8...0.8.1)

### Fixes

- Fixes a bug trying to set active on decendants before object is saved. [2a0b476](https://github.com/jazzband/django-categories/commit/2a0b4768a319c19a8c05b32868e4c3198a26d8ee)
    
### Other

- Bumped version to 0.8.1. [801d269](https://github.com/jazzband/django-categories/commit/801d269c4167b0a3ac45e27bcfa11b46a14872bf)
    
## 0.8 (2011-08-22)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.7.2...0.8)

### New

- Added to the README. [4450a91](https://github.com/jazzband/django-categories/commit/4450a91477a49a00a0ab5a1e9fad3b65186508f1)
    
- Added an active flag for models. [3e8a10a](https://github.com/jazzband/django-categories/commit/3e8a10ad4ea535c00289e8d808cbc41ad2481985)
    
### Other

- Re-rendered the docs to reflect 0.8. [a937dfd](https://github.com/jazzband/django-categories/commit/a937dfdcf11136b0847db3ea6ce878e8701cd2b0)
    
- Version bump. [bcd38da](https://github.com/jazzband/django-categories/commit/bcd38da7663ebf8be9ada6f5cf751536a7d6645c)
    
### Updates

- Improved Category import. [3fe5004](https://github.com/jazzband/django-categories/commit/3fe50040c381b79c11a887bbb97b8b1a5f70ac2e)
    
## 0.7.2 (2011-08-19)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.7.1...0.7.2)

### New

- Added a check in migrate_app to see if the app is a string or not. [7cb7482](https://github.com/jazzband/django-categories/commit/7cb74829ea296a23386eff50496c4d5223c79906)
    
### Other

- Pruning the example project. [6f3a925](https://github.com/jazzband/django-categories/commit/6f3a925ed50a4de8a7c643a840ad853b2f74fedd)
    
- Version bump to 0.7.2. [8d0b5f9](https://github.com/jazzband/django-categories/commit/8d0b5f942b1e02ff7d808960c84718981557c379)
    
- PEP 8 formatting. [4d4793d](https://github.com/jazzband/django-categories/commit/4d4793db36fcb3f38e407341f01214b58af5add8)
    
- Ensure that the slug is always within the 50 characters it needs to be. [5a74525](https://github.com/jazzband/django-categories/commit/5a745254466024d3d6a932e74d152a4ed069beb9)
    
### Updates

- Updated the get_version function to be PEP 386 compliant and version bump to 0.7.2b1. [309accf](https://github.com/jazzband/django-categories/commit/309accf3e0ca8affa346ff0d1bec193fb6f99780)
    
- Refactored the editor to become Django 1.1.1 compatible and some PEP8 formatting. [e7fad27](https://github.com/jazzband/django-categories/commit/e7fad278d12048dc743ee4ca2034f5d43b687d5d)
    
- Changed the DatabaseError import to be more compatible. [4107cdd](https://github.com/jazzband/django-categories/commit/4107cdd125c6f4e9840dbc48a63c03d65e4da8e0)
    
- Updated the readme. [1cb208c](https://github.com/jazzband/django-categories/commit/1cb208c9ac48cd983be252dee3d1eb5ebf80a54b)
    
## 0.7.1 (2011-08-03)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.7...0.7.1)

### Other

- Version bump to 0.7.1. [4d3fdb0](https://github.com/jazzband/django-categories/commit/4d3fdb0ba98105c52e8ebb318720ee5324afbe47)
    
- Due to settings, the migration for the category relations table never would be created. This fixes it. [3b6d469](https://github.com/jazzband/django-categories/commit/3b6d469b89971d1ca35027a84a0cdbde4ad171fb)
    
## 0.7 (2011-08-02)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.6...0.7)

### Fixes

- Fixed a typo in the docs. [66b0f5b](https://github.com/jazzband/django-categories/commit/66b0f5bda10352e017747443aaa7ff5fdb1e9bfa)
    
### New

- Added a setting for the JAVASCRIPT_URL to make placement of the genericcollections.js file easier. [7bdfb32](https://github.com/jazzband/django-categories/commit/7bdfb32474ca01c17738a53ac47f32fa52131480)
    
- Added compatibility with Django 1.1 by adding missing methods for editor and bumped version to 0.7beta2. [e922506](https://github.com/jazzband/django-categories/commit/e922506fd969c8029fcd0e1262fd02652d599df9)
    
- Added a get_latest_objects_by_category template tag. Might be useful. [d3cbb62](https://github.com/jazzband/django-categories/commit/d3cbb62b5d5342a9db77389498e0d7bf9ad509d0)
    
- Added the ability to add the appropriate fields to a table if configured after an initial syncdb. [fdc025d](https://github.com/jazzband/django-categories/commit/fdc025d812a8559e9426758d30b322aa3e6bfcfd)
    
- Added an alternate url field to the model. [cedd54e](https://github.com/jazzband/django-categories/commit/cedd54e85d92c7a9bca0846cf7b2a0e10f5a3a0a)
    
### Other

- Final version: 0.7. [fa6e2f1](https://github.com/jazzband/django-categories/commit/fa6e2f1153ce351b4a1fcda4d50bc4fd71a2b29c)
    
- Forgot to add the alternate_url to the admin. [b1ad054](https://github.com/jazzband/django-categories/commit/b1ad0547594baf37e8539aeaf09baf340e1e86dd)
    
- Altered the inline template to display the content_object instead of the __unicode__ of the middle table. [6aae69b](https://github.com/jazzband/django-categories/commit/6aae69b0150c9ce805a910c60242a74c2eaa61d8)
    
- Ooops, found a bug in the javascript. [e8154f0](https://github.com/jazzband/django-categories/commit/e8154f0abd508967c40dab1dba47a194b613f32d)
    
- Updating the documentation. [ed4db03](https://github.com/jazzband/django-categories/commit/ed4db03c7ddeb20fde5f7951ea9895f2aadca42f)
    
- [Fixes issue #23] Changes the way the tree shows items when searched. Doesn't hide them in the template. [d48be41](https://github.com/jazzband/django-categories/commit/d48be41dd3227628a1f30ca09bfc791cc9ec8bf6)
    
- Ignoring the example/media/ directory. [e257bd6](https://github.com/jazzband/django-categories/commit/e257bd6db8ad2492dcca5bd4067e8a5d42a4f291)
    
- Bumping the version to 0.7beta1. [28bb8e5](https://github.com/jazzband/django-categories/commit/28bb8e53fdedfa217e404b975017abccfa8b6be0)
    
### Updates

- Updated and rendered docs. [66e67a0](https://github.com/jazzband/django-categories/commit/66e67a07f490f4afb8ea35fc0d8db9a0f2cc3547)
    
- Refactored the registry into a registry of models and fields. This will make it easier for migrations. [7e83b12](https://github.com/jazzband/django-categories/commit/7e83b12a41e12c4c5ac9824d557eb8d7acdf96ff)
    
- Updated the gitignore for venv file. [7beb29a](https://github.com/jazzband/django-categories/commit/7beb29af805b3c336dd29dac8f1e1634255ac3fe)
    
- Deleted old migration scripts since they were migrated to south. [89e3307](https://github.com/jazzband/django-categories/commit/89e3307117c09ad06925251e4b054aaddc2e67b2)
    
## 0.6 (2011-05-18)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.5.2...0.6)

### Fixes

- Fixed a problem in the new admin creation where it wouldn't properly filter out the category fields by model. [d90dccd](https://github.com/jazzband/django-categories/commit/d90dccda01ce23f03ab6488166abccb407943adb)
    
- Fixed the deprecated settings int he example app. [7d29584](https://github.com/jazzband/django-categories/commit/7d295843aa71165b5fd61c536e16a76f2d0d5309)
    
- Fixing stashing conflict. [9528f97](https://github.com/jazzband/django-categories/commit/9528f971c97e9f560457dafb84fadb6c2cb8bc81)
    
- Fixed small errors in templatetags documentation and docstrings. [1100ad3](https://github.com/jazzband/django-categories/commit/1100ad3c507fab8a22442938561f0a0670dccb35)
    
- Fixed wrong var name in import_categories command. [cda1d0f](https://github.com/jazzband/django-categories/commit/cda1d0fd5e3044fc58813d510563e086b126736d)
    
- Fixed the homepage in the setup.py. [8e0e49a](https://github.com/jazzband/django-categories/commit/8e0e49a28109ac63841da04c7ed80a6dc516ce8a)
    
### New

- Added a Deprecation warning for CATEGORIES_RELATION_MODELS. [05a55fe](https://github.com/jazzband/django-categories/commit/05a55fea7d3b21e5e875aad8b90213f0af0e21ec)
    
- Adding South migrations. [8e843fb](https://github.com/jazzband/django-categories/commit/8e843fbcd1afea4a47d67e71a63b7c0c4b1c421b)
    
- Added some specialized functions for relations. [0fa7402](https://github.com/jazzband/django-categories/commit/0fa7402f1d4a89476390ddc2934c57a467fff00e)
    
- Added a class based view for the detail page of a model related to a category. [76d7461](https://github.com/jazzband/django-categories/commit/76d7461e434cfd13f4a73f37fdd511ed8c97feae)
    
- Added a view that list items of specific model that are related to the current category. [c89c954](https://github.com/jazzband/django-categories/commit/c89c954001df23654129b19d1554a1a6a780fc00)
    
- Added a class based CategoryDetailView that should be functionally identical to the original function based view. [1070cb7](https://github.com/jazzband/django-categories/commit/1070cb7daeefe0bd367588003758d03fc0b5da17)
    
- Add optional thumbnail model field. [1ac5ae0](https://github.com/jazzband/django-categories/commit/1ac5ae0a095fea5761a3eeca1251b2bdd7d06429)
    
### Other

- Final doc rendering. [7681919](https://github.com/jazzband/django-categories/commit/768191968ae4f16f190bc5a1a2ed6b1271895435)
    
- Version bump to 0.6. [6f26261](https://github.com/jazzband/django-categories/commit/6f26261c50d0b60ba8833d7186156d268f989fd7)
    
- Enabled new registry in the example app for testing. [fa2b680](https://github.com/jazzband/django-categories/commit/fa2b680c148589a9be7ac3195b4ea08f0ddd08f3)
    
- The registry default settings needs to be an empty dict, not list. [97c45e7](https://github.com/jazzband/django-categories/commit/97c45e702f38c225132717abcedf19d4763ba579)
    
- Enable registering of models in settings. [4e8f490](https://github.com/jazzband/django-categories/commit/4e8f490714b78e82436073e724960b56b441bdfa)
    
- [FIXED Issue #17] Refactored how the HTML is rendered, removing the checkbox from the <a> tag and pulling the parent checkbox from the row class. [70e758e](https://github.com/jazzband/django-categories/commit/70e758ea2e90d00fdbacb1a3bf10da8e629fe06b)
    
- Putting registry outside of the try block. [141f753](https://github.com/jazzband/django-categories/commit/141f753a951fc29a108f608e2aa055e1c7e79ab7)
    
- Version bump to 0.6beta4. [7639d95](https://github.com/jazzband/django-categories/commit/7639d95721751b2bbb67b27150b62a3b51451fd8)
    
- Updating settings for Django 1.3. [93cd476](https://github.com/jazzband/django-categories/commit/93cd476c57600d5a84468b8109d6eeaeff6b786e)
    
- Version bump to 0.6beta3. [3d91ff1](https://github.com/jazzband/django-categories/commit/3d91ff1fafee0c371bd56370ecafc15fa9777e32)
    
- Ah, the wonders of copying and pasting. Fixed some errors resulting from it. [64dd94a](https://github.com/jazzband/django-categories/commit/64dd94aa43d37f501b128811962226bb8af4fbe6)
    
- Version bump to 0.6beta2. [d64ad65](https://github.com/jazzband/django-categories/commit/d64ad65a7c4318d9d85f9ae77a4bcc166a6b70ba)
    
- Clean up per pylint. [32b5451](https://github.com/jazzband/django-categories/commit/32b5451c1593639cd31471a3bd2af67aae3391a9)
    
- Some Docs. [081d2ab](https://github.com/jazzband/django-categories/commit/081d2ab0b8161c953cc283553fe74b5b5201e4b0)
    
- Allow for using django-cbv in Django 1.2.x. [4081fe8](https://github.com/jazzband/django-categories/commit/4081fe820430c4c310bb967f7c0b1b837abc7933)
    
- Slight refactor of the default settings to clean it up. [4ce5a9e](https://github.com/jazzband/django-categories/commit/4ce5a9e297c5655e022472cbb32f93a28c347d2e)
    
- Filled out all contributors. [8d46659](https://github.com/jazzband/django-categories/commit/8d466591d550d78b7592912c082f2bf25f73897b)
    
- Moved path to category code into its own function to make reuse easier. [0b20115](https://github.com/jazzband/django-categories/commit/0b201156e016e490c9403d32c2559604cc4b5bdc)
    
- Make admin js relative to MEDIA_URL. [7119ca8](https://github.com/jazzband/django-categories/commit/7119ca87e6b57a3d179c23f3577aaacd42bf7427)
    
- Bumped the version for this branch. [3542b01](https://github.com/jazzband/django-categories/commit/3542b019c528d975cd106ba0ef727f946d0e49f8)
    
- Make the initial state of the editor tree an app setting with collapsed as the default. [858a356](https://github.com/jazzband/django-categories/commit/858a356e42744dfd55625b1cd5aeb0bcc4074191)
    
- Real change I needed to make: return, not pass!. [e8b7aec](https://github.com/jazzband/django-categories/commit/e8b7aeca8facbbcbcfab201e77781f88c58d6f53)
    
### Updates

- Updated docs. [441dbcd](https://github.com/jazzband/django-categories/commit/441dbcde744b34ed08ae671d9da7d3f99ae573d2)
    
- Updated README. [7474cb0](https://github.com/jazzband/django-categories/commit/7474cb0e516ecdabc4ffe369fe38cc3327e6f46f)
    
- Updated some of the setup info. [1ad18ec](https://github.com/jazzband/django-categories/commit/1ad18ecb5c178598879756628b10288e7baede26)
    
- Refactored the thumbnail from imagefield to filefield. [efe3cdd](https://github.com/jazzband/django-categories/commit/efe3cdd06b24f433352f393afc3effa99b4090a4)
    
  Why? ImageField causes hits to storage to fill out certain fields. Added a storage class and width/height fields so it is possible to scale the thumbnails and store them somewhere besides the filesystem.
- Remove 'to' from kwargs in CategoryM2MField and CategoryFKField. 'to' is already specified, and causes errors when running unit tests. [29ab094](https://github.com/jazzband/django-categories/commit/29ab0943c5b67240d0ed0271b4efd2d947ad497b)
    
## 0.5.2 (2011-02-14)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.5.1...0.5.2)

### Updates

- Removed the raising of an exception when it finds a model that is already registered. and bumped the version to 0.5.2. [47ddf73](https://github.com/jazzband/django-categories/commit/47ddf73b717c3b68f89d70c1bfc10232e42ada7a)
    
## 0.5.1 (2011-02-14)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.5...0.5.1)

### Other

- Bumped version number to 0.5.1. [f142f1a](https://github.com/jazzband/django-categories/commit/f142f1a77c375a51778db90fdeb3b6e98ae48c07)
    
- The test for importing checks the first child. With two children either could be 1st, so remove one. [89646a6](https://github.com/jazzband/django-categories/commit/89646a6ceee4361966c9a61c632affe8ee7d14a2)
    
- Need to delete all the objects before each test because the import checks its work. [2bfe753](https://github.com/jazzband/django-categories/commit/2bfe7534280ef3b4c47f13f4f82410867e5bd726)
    
- Checking for raising the correct exception and moved the strings used in the test to a list of strings. [31f1bfe](https://github.com/jazzband/django-categories/commit/31f1bfef8dce51065dcc07d9894964a972de743e)
    
- Got rid of the debugging print statements. [74d9910](https://github.com/jazzband/django-categories/commit/74d9910a4c3ea506dd199d049276d187dcf39ab8)
    
### Updates

- Updated the test to test a new template tag, not the old one. [efc4b93](https://github.com/jazzband/django-categories/commit/efc4b9339a4c2f2b8f59ffb20e2d01b69304be0f)
    
- Changed the import to import from category_import. [6aad1c4](https://github.com/jazzband/django-categories/commit/6aad1c44cc45519e107e57c6465144d0c3f3878f)
    
## 0.5 (2011-01-20)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.4.8...0.5)

### New

- Added contributors to the readme for proper recognition. [93086cf](https://github.com/jazzband/django-categories/commit/93086cf1ec6e9261b63f49eb848398dc812af98c)
    
- Added logic to skip adding categories that are already defined for a modeladmin. [246c18d](https://github.com/jazzband/django-categories/commit/246c18d4e65a1dc841be2f6bd100625505f2f7cf)
    
- Added additional fields to the display_list. [781f9d0](https://github.com/jazzband/django-categories/commit/781f9d02d50fee13c10aa3a959ba15f364105f52)
    
- Adding a new import and alphabetizing them (OCD, I know). [df83dd2](https://github.com/jazzband/django-categories/commit/df83dd2ee5c59aa9873bb75e760e892bf914383e)
    
- Added a new template tag to override the painting of the admin rows. [d093d06](https://github.com/jazzband/django-categories/commit/d093d06b400185402b84e48d0661dca6c95902ef)
    
- New template and media. [bb4a7b0](https://github.com/jazzband/django-categories/commit/bb4a7b0f2bf8a0514a356f5214b3a34544f4d967)
    
- Added a placeholder for Django. [a841d7f](https://github.com/jazzband/django-categories/commit/a841d7f063db89bc615a920b624aa901f9bf1b43)
    
- Adding a new version of TreeTable with a few minor changes to support row repainting. [ae49c9d](https://github.com/jazzband/django-categories/commit/ae49c9d066b4541509f979328ad8eb105d6c0620)
    
### Other

- Bumped the version to 0.5. [57081cd](https://github.com/jazzband/django-categories/commit/57081cdd6f4b919d5c4dcbd6bd94fabf1809424c)
    
- STATIC_URL seems to be returning as None even when not defined. [4632d43](https://github.com/jazzband/django-categories/commit/4632d436fd799c35a58d421345207832cf322093)
    
- ModelAdmin re-register now skips modeladmins without fieldsets already defined. [44508e0](https://github.com/jazzband/django-categories/commit/44508e060616025d145637deb0b1bbc652a919fe)
    
  Was causing a "TypeError at /current/url/: unsupported operand type(s) for +: 'NoneType' and 'tuple'"
- Got rid of the with_stories keyword for the category detail view. [7058ccd](https://github.com/jazzband/django-categories/commit/7058ccd35a7ed18ad61cddc023b51b6b00d275e6)
    
- Revised the README to get it up-to-date. [732c5f8](https://github.com/jazzband/django-categories/commit/732c5f8163b49301b73b4399693d0573c85abf34)
    
- Long trees cause a performance hit if the initial state is expanded. Changing to "collapsed". [381d438](https://github.com/jazzband/django-categories/commit/381d438635e6a23ddf72a9309cfca5282d56902d)
    
- Getting rid of unused code in the treeeditor. [9d92b0d](https://github.com/jazzband/django-categories/commit/9d92b0d3a7578a989b969daa1592cb8eeabda547)
    
- Ignoring a few more things. [5dfc710](https://github.com/jazzband/django-categories/commit/5dfc71035758b3ba73b598071f6b2617079086d3)
    
- Made the media delivery work. [c55e56e](https://github.com/jazzband/django-categories/commit/c55e56e48f2fa78ab86853e44c1b0c11f7602ed5)
    
- What's that doing there?. [6a112a4](https://github.com/jazzband/django-categories/commit/6a112a4a84406434151db3452f20e219f3db2987)
    
- Now that Django has a getchangelist function, we don't need to hack anymore. [039ba1f](https://github.com/jazzband/django-categories/commit/039ba1f72eb100a31d6fe3d1ee74f477169ee1a8)
    
- Don't need to set that EDITOR_MEDIA_PATH any more. [d1bf06b](https://github.com/jazzband/django-categories/commit/d1bf06b39f54fab1be466d45460c9f3fd15ee7d8)
    
- Reworked the template to initialize the correct javascript and use the result_tree_list. [7f0e93f](https://github.com/jazzband/django-categories/commit/7f0e93f7d367749a33d4e74133c3381e198b9e43)
    
- Got rid of hotlinking settings and changed the EDITOR_MEDIA_PATH. [f7faa54](https://github.com/jazzband/django-categories/commit/f7faa54620492b1fe4c34269c4bbd6bde42a0424)
    
- Unstashing the previous changes. [4fbed62](https://github.com/jazzband/django-categories/commit/4fbed625c42627c4b066ccf59a161ed5012e16a2)
    
### Updates

- Renamed 'media' directories to 'static' to work with the django 1.3 staticfiles app. [e5deb3f](https://github.com/jazzband/django-categories/commit/e5deb3f41f36d08a2e180f2d5baa82c181ded47a)
    
- Removed duplicate slash from EDITOR_MEDIA_PATH setting. [8f8bc6e](https://github.com/jazzband/django-categories/commit/8f8bc6eb96f50c24ccffa3aea9e9cdc3e508cfa3)
    
- Updated the documentation!. [b2dec54](https://github.com/jazzband/django-categories/commit/b2dec5416fe1b74bd612058664cebd3e43e0ea7f)
    
- Updated the docstrings of the template tags and added breadcrumbs. [afe9d20](https://github.com/jazzband/django-categories/commit/afe9d204c84bfdba660e30a021ec3022826893e9)
    
- Refactored the templates to extend a categories/base.html. [91227ed](https://github.com/jazzband/django-categories/commit/91227edccf31d20291d2b65d2e700b3da481f4ce)
    
- Renamed the README to indicate it is a reST file. [b5edbdc](https://github.com/jazzband/django-categories/commit/b5edbdcccbea0eb6032ad5c90c8a28639ccf1754)
    
- Removed some unused cruft from the TreeEditor class. [b5c6482](https://github.com/jazzband/django-categories/commit/b5c6482ffa6d01dbd1d380407ae0375b1fe38c01)
    
- Deleted an unused template. [d027b75](https://github.com/jazzband/django-categories/commit/d027b752f2a3346877b9ceb4c98c15172823663f)
    
- Removed unused code files. [6693d8d](https://github.com/jazzband/django-categories/commit/6693d8dad3089881d2f8fddd1893461bf291bbfd)
    
- Removed all the old, unused templates. [1e546b6](https://github.com/jazzband/django-categories/commit/1e546b6309642a1d2ed9ab65bb68cc4f1dceb82b)
    
- Removed all the old media. [80755c7](https://github.com/jazzband/django-categories/commit/80755c79e3a584f8b89f9a26fb5c4d2a46c5e662)
    
## 0.4.8 (2010-12-10)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.4.5...0.4.8)

### Fixes

- Fixing bug #6 per primski. Adds the correct fields into the admin instead of both. [e1b53ae](https://github.com/jazzband/django-categories/commit/e1b53aefcb167a649c93da94cd5c7fc97d559867)
    
### New

- Added a Meta class for proper plural naming. [a240fef](https://github.com/jazzband/django-categories/commit/a240fef9502d305f8364811e5205f9dd6ae19d25)
    
### Other

- Bumped the version. [3abddf2](https://github.com/jazzband/django-categories/commit/3abddf2db23c2e769fc36c6c523f63df84b050a7)
    
- PyPI didn't like the license metadata. [11768c2](https://github.com/jazzband/django-categories/commit/11768c29877cdfd6234b779da282ef67eaa29188)
    
- Upped version to 0.4.7. [1b8511a](https://github.com/jazzband/django-categories/commit/1b8511a244db6f7fc4adb0f286ffea49e8a7c5fe)
    
- Upped requirements to django-mptt 0.4.1. [66b6345](https://github.com/jazzband/django-categories/commit/66b634505b7db4bcb6408684139cc2c8a5b40eca)
    
- Bumped versino to 0.4.6. [754abe9](https://github.com/jazzband/django-categories/commit/754abe98cbddee75749790b042cafdfa737f6637)
    
### Updates

- Updated the requirements to django-mptt 0.4.2. [70365f6](https://github.com/jazzband/django-categories/commit/70365f636bb65ffc6541bb5e6042a61757115fd3)
    
- Modified Category model to work with django-mptt 0.4. [04da4c0](https://github.com/jazzband/django-categories/commit/04da4c0bdddadc28a9536fdfc443d21bed75173d)
    
## 0.4.5 (2010-10-07)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.4.6...0.4.5)

## 0.4.6 (2010-10-07)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.4.4...0.4.6)

### Fixes

- Fix fieldsets assignment, issue 3. [502c50d](https://github.com/jazzband/django-categories/commit/502c50d9c827e68fd21a19ec9a14dcc45cff6832)
    
### Other

- Bumped versino to 0.4.6. [754abe9](https://github.com/jazzband/django-categories/commit/754abe98cbddee75749790b042cafdfa737f6637)
    
- Category string, fixes issue 2. [027569f](https://github.com/jazzband/django-categories/commit/027569f691d7164a08aabbfd5d8f2adcd46f34ef)
    
- Checks for parent if given enough path bits, version bump. [09b1cda](https://github.com/jazzband/django-categories/commit/09b1cda4b5aab49f8dfae9f9e11a5dd3bb175a18)
    
## 0.4.4 (2010-05-28)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.4.2...0.4.4)

### New

- Added the extra templates. [507700b](https://github.com/jazzband/django-categories/commit/507700b69dc153b67b0fee0f42d5b270f448427c)
    
- Added extra context to view func. [10177e3](https://github.com/jazzband/django-categories/commit/10177e3d2e083dad76036744f505c4141496aeb6)
    
### Other

- Redid docs with new template. [e5f8baf](https://github.com/jazzband/django-categories/commit/e5f8bafd0b6fac624f148600ac717edb4276f9f6)
    
- Tweaked the setup.py and manifest for a better result. [0427902](https://github.com/jazzband/django-categories/commit/042790279deeb03a716a19849ad6b2e67960a9cf)
    
- Finished the doc refactoring and generated the docs. [908db01](https://github.com/jazzband/django-categories/commit/908db01e46c93ec205db136b2003e65a69b92923)
    
- Bumped version. [dfc3082](https://github.com/jazzband/django-categories/commit/dfc30820fef4ea6d611ee527871a06eb7b1b0131)
    
- Require a trailing slash at the end of urls. [67a272b](https://github.com/jazzband/django-categories/commit/67a272b09bce97ffa3bf69f1d98230c7cd00c3e3)
    
- Safe mptt registration. [ab6b48c](https://github.com/jazzband/django-categories/commit/ab6b48c9d94ff9ecd0b96fbe2f126f1732d299d0)
    
### Updates

- Refactoring docs into doc_src and docs. [3e6944d](https://github.com/jazzband/django-categories/commit/3e6944de65bcb6d81febd0ebf58a8b9d2c5a8a70)
    
## 0.4.2 (2010-04-28)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.4...0.4.2)

### Fixes

- Fixing jquery issues. [605cbec](https://github.com/jazzband/django-categories/commit/605cbece20911879322becf7664c8e45712147b3)
    
### Other

- Fied my typo for settings url. [d453d4a](https://github.com/jazzband/django-categories/commit/d453d4a410ac0b34e08d1d44dba9d6b9bd45fe88)
    
### Updates

- Updated the version number. [920c0e2](https://github.com/jazzband/django-categories/commit/920c0e2e989ffbeb7481f0eb52adf8ea289763c2)
    
## 0.4 (2010-04-23)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.3...0.4)

### New

- Added the necessary files to test the generic relations. [c5759a1](https://github.com/jazzband/django-categories/commit/c5759a17c64aef0765297a324be89cfa851d023e)
    
- Added generic relation stuff into categories. [9e1717f](https://github.com/jazzband/django-categories/commit/9e1717f3f792204af3d09d30799168d2f30aa961)
    
### Updates

- Renamed sample to example because that is what every other one is called, damnit. [2faa6c8](https://github.com/jazzband/django-categories/commit/2faa6c81801ac507256d387062d0d71da756fa07)
    
## 0.3 (2010-04-23)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.2.2...0.3)

### New

- Added metadata to the model for seo stuff. [031c328](https://github.com/jazzband/django-categories/commit/031c32854caf4c8776543e70030fec714eb5340a)
    
### Updates

- Changed the requirements from mptt in our repository to mptt-2 in pypi. [0b27adc](https://github.com/jazzband/django-categories/commit/0b27adc2a5ef8104b65088ec959fcbfb1c742a48)
    
## 0.2.2 (2010-04-08)
[Compare the full difference.](https://github.com/jazzband/django-categories/compare/0.2.1...0.2.2)

### New

- Added better setup.py pieces. Getting ready to push to our PyPi. [c1c2a72](https://github.com/jazzband/django-categories/commit/c1c2a72115f48a77ac0b480c8c7c2f799f25d4dc)
    
### Other

- Switched to setuptools/distribute. [c479cc6](https://github.com/jazzband/django-categories/commit/c479cc6ad95fcb41ce37edf69bb1acc8b08ad572)
    
- Removing docs for piece I deleted previously. [53372a6](https://github.com/jazzband/django-categories/commit/53372a60a94eddc12d74bd48ef44953920ce02c3)
    
### Updates

- Changed the requirements to have mptt just greater than 0.2. [50bf7e1](https://github.com/jazzband/django-categories/commit/50bf7e189616938a8220e310378c9398531be6fa)
    
- Deleted code referencing something I deleted earlier. [fdeb2fc](https://github.com/jazzband/django-categories/commit/fdeb2fc14e854394fb1e88ad73df09e902f0942a)
    
## 0.2.1 (2010-04-06)

### Fixes

- Fixed a typo in the setup.py and wrapped the other django import in __init__.py so you could call get_version without having django installed. Also increased the version number to 0.2.1. [8a5c137](https://github.com/jazzband/django-categories/commit/8a5c137eb62c036138eb6f7a62b977176e7f0ea1)
    
- Fixed the get_absolute_url for the Categories model and fixed up the view as well. [e1da454](https://github.com/jazzband/django-categories/commit/e1da454beea4b051211d346c8bbf1aabfae476d7)
    
- Fixing up and updating the usage. [76d60d2](https://github.com/jazzband/django-categories/commit/76d60d286db74e61d43b8f45632298ee997d15cb)
    
- Fixed up the readme to include some goals. [1a38fa2](https://github.com/jazzband/django-categories/commit/1a38fa27fe70f67be4a7eaf858c05daf7c9b5ca4)
    
- Fixed most of the tests. [13154fd](https://github.com/jazzband/django-categories/commit/13154fd3cadc38c9d45d15130e70e5de32d7c175)
    
- Fixed a wrong relative path with the jsi18n admin script. [0aedad9](https://github.com/jazzband/django-categories/commit/0aedad941f4a0bf4b3ac8d63d091f739546b10c3)
    
- Fixed a bad merge. [409b7b8](https://github.com/jazzband/django-categories/commit/409b7b86f5ec5ab9baf32956556c44e6fc9f7ee2)
    
### New

- Added some docs and testing apps. [81d07c8](https://github.com/jazzband/django-categories/commit/81d07c859d7291ea167b8c1d1f92d65a37c33e75)
    
- Added a caching setting to vary the amount of time the view is cached. [b0468cc](https://github.com/jazzband/django-categories/commit/b0468cc8e4088405df3af6f52123ba5226d1ce45)
    
- Added missing templates for category traversal. [06d3352](https://github.com/jazzband/django-categories/commit/06d335238a870b1416846f5cbc829918e1389a18)
    
- Added an app to test categories against. [486ffec](https://github.com/jazzband/django-categories/commit/486ffec34f89824f75080cc54a437cc65442396d)
    
- Added some registration notes to start the docs. [0ec1fa7](https://github.com/jazzband/django-categories/commit/0ec1fa7332297789845465ca45395dd1d15c56d9)
    
- Added registry, hacked admin w/ new templates for category editor. [c6f2699](https://github.com/jazzband/django-categories/commit/c6f269985ee97a690fa73130f12fb13d935706c3)
    
- Added ability to register fields to models. [ff92ac9](https://github.com/jazzband/django-categories/commit/ff92ac9771bdb591d55145e56ffe71e3891ff403)
    
- Added registry, hacked admin w/ new templates for category editor. [c4c1b30](https://github.com/jazzband/django-categories/commit/c4c1b30aeece9e67acfbc85468b995972b4cefc6)
    
- Added an optional setting to allow the slug to be changed. [58a2280](https://github.com/jazzband/django-categories/commit/58a2280c2b6cbe533be420f69257fe7cfab716a8)
    
- Added a new templatetag to retrieve the top level categories. [e69cfe9](https://github.com/jazzband/django-categories/commit/e69cfe96277a3d160679202d9e25a05fd815b34f)
    
- Added views. [c3b26df](https://github.com/jazzband/django-categories/commit/c3b26df0da254d301318d32e75011ad0c77eecd7)
    
- Added new documentation. [a7fa144](https://github.com/jazzband/django-categories/commit/a7fa144a8c6dd223980880a6b977c135ffcb7386)
    
- Added a description field. [598a418](https://github.com/jazzband/django-categories/commit/598a418a0f5d6126dc1dc8122e9be2ab6b7f025b)
    
- Added some sample config to see it work. [2e9cba2](https://github.com/jazzband/django-categories/commit/2e9cba224cfe46a72c3ec078a4d559679abd6e52)
    
- Added a template for the template tags. [8830d92](https://github.com/jazzband/django-categories/commit/8830d92f8e735e9442317cb7e340a367e6467bf1)
    
- Added a demo file of music genres. [084e408](https://github.com/jazzband/django-categories/commit/084e4089e000301471597e68618c9820e6df6f5e)
    
- Added tests for templatetags. [f30b836](https://github.com/jazzband/django-categories/commit/f30b8362c628c0f2f33b031f656741f009a0734a)
    
- Added some testing fixtures. [6557c64](https://github.com/jazzband/django-categories/commit/6557c644cd0b49712402a70c6e3149f6b8d9df6d)
    
- Added some tests for category importing. [5d9ceb4](https://github.com/jazzband/django-categories/commit/5d9ceb480b8e74e881437080d4510904bbc15ddf)
    
- Added a command to import categories from a file. [413e756](https://github.com/jazzband/django-categories/commit/413e756a0a9b73406851aae78cdfbb542d6f823d)
    
- Added the editor templates. [38979d4](https://github.com/jazzband/django-categories/commit/38979d463c36d07ea1b808d892baf1c3158a7e30)
    
- Added to the gitignore. [b48f5d2](https://github.com/jazzband/django-categories/commit/b48f5d2c0f3eb6c31c9077913e21335a789db7ec)
    
- Added template for category detail. [8bebe9b](https://github.com/jazzband/django-categories/commit/8bebe9bfc8b26f3677bff399af4d2d4487dd331b)
    
- Added urls and views for category detail. [9a9f39d](https://github.com/jazzband/django-categories/commit/9a9f39db184fc0f7479d0ad7096376ecfc7b9666)
    
- Added in support materials. [ece93fd](https://github.com/jazzband/django-categories/commit/ece93fd92d75a3cc0bd82e786cf777b8871c55f9)
    
### Other

- Tiered template heirarchy. [30ad968](https://github.com/jazzband/django-categories/commit/30ad968c3926488de6db15de2c99220c9baa0853)
    
- Attempt at hacking a through table (field errors). [0ca025d](https://github.com/jazzband/django-categories/commit/0ca025d76374816feba61351e4b9f20276414563)
    
- Altered the registration naming so more than one field could be registered for a model. [487a0a4](https://github.com/jazzband/django-categories/commit/487a0a4f2388611b053749ed7e45283eb5f30fd7)
    
- Finished the debugging and changed the logic. [9c05799](https://github.com/jazzband/django-categories/commit/9c057997141df7aef07c7a2e76005cc932b1f261)
    
- Cats. [16ad805](https://github.com/jazzband/django-categories/commit/16ad8057e3d7f414931acaca5abc9dde50a0d63a)
    
- Ignoring the docs/_build directory. [4573a37](https://github.com/jazzband/django-categories/commit/4573a37b14f4d449e0272e36e8b95d67cb2b8648)
    
- Upped the version and separated the editor. [6c24d2f](https://github.com/jazzband/django-categories/commit/6c24d2ff6580d2dbc78dcbee3e26d7301b61d7d5)
    
- Tweaked the description and example of the template tag. [a8a91de](https://github.com/jazzband/django-categories/commit/a8a91de6fac7097398c7ab0778d97a15a9b59748)
    
- Getting the admin interface working. [01c6cf3](https://github.com/jazzband/django-categories/commit/01c6cf38c57c40a3487f0d3e92b14030a3900b07)
    
- Removing unneeded files. [603352c](https://github.com/jazzband/django-categories/commit/603352c84f7d6f7e13d570e538644d10c249ab20)
    
- Started the docs. [1f9cc91](https://github.com/jazzband/django-categories/commit/1f9cc91cabb48fb595ffbb10bd2af4c2cf41084f)
    
- Moving media files around. [8deaaa2](https://github.com/jazzband/django-categories/commit/8deaaa2002781e5c5f0d7a507840e4d3c0632910)
    
- Removing mentions of FEINCMS to make it more generic. [9d4d59c](https://github.com/jazzband/django-categories/commit/9d4d59cb2a85aa9b0a5586ba404bb818c67ebe73)
    
- Split the editor into a separate app. [40f5471](https://github.com/jazzband/django-categories/commit/40f5471abd512ee4db7eddce780b4b49bcc7cd68)
    
- Moved media around, modified the editor template and removed .egg-info. [0d32def](https://github.com/jazzband/django-categories/commit/0d32deffb0373160b0a938a0dfc9f6c73c71644c)
    
- Made sure the models and admin looked right and worked with Stories. [fc2ae67](https://github.com/jazzband/django-categories/commit/fc2ae672e68e5503bd8f50b81262e0b8297a3dec)
    
- Making sure everything is in the repo. [8d48c8c](https://github.com/jazzband/django-categories/commit/8d48c8c04235d3273dcf32f74f05dcb24ed63cb7)
    
- Getting ready to move to a remote repository. [94a0a41](https://github.com/jazzband/django-categories/commit/94a0a41443bae0b1fe87e1d8139d8987a0cbf792)
    
- Initial import. [e39e575](https://github.com/jazzband/django-categories/commit/e39e575ce0c92a3700a9552726800eb0aab93641)
    
### Updates

- Modified the setup.py to get the latest version from the code and the long_description fro the README.txt file. [4700b26](https://github.com/jazzband/django-categories/commit/4700b268eb65bad6b21e07414d01a058ec825189)
    
- Removed the special many2many models. The user interface was just too odd to implement. [7dfb2da](https://github.com/jazzband/django-categories/commit/7dfb2da26777fdf53907d8ce0c7a5520ac84cc0a)
    
- Removed some tabs. [69ef59d](https://github.com/jazzband/django-categories/commit/69ef59d178778f839b4a470f5cdba2506376dd8c)
    
- Changed the disclosure triangle to be a unicode character instead of the images. [59cf711](https://github.com/jazzband/django-categories/commit/59cf711b66576b753c9c23f40705c301b155001c)
    
- Removed the permalink decorator to make the absoluteurl work. [2f3b1da](https://github.com/jazzband/django-categories/commit/2f3b1dacbfd5b04a57f7c0f6d1ec4041ba99bbee)
    
- Removed a strange typo. [176edd7](https://github.com/jazzband/django-categories/commit/176edd7736f84513d4cc201265c2425d10741c1e)
    
- Removed some unneeded media files. [7ca8f90](https://github.com/jazzband/django-categories/commit/7ca8f904ab9f9affd541a5077d0aa96ebed16d59)
    
- Updated tree editor view. [facd3bf](https://github.com/jazzband/django-categories/commit/facd3bf294b9181e3ae8e0e5193d48bc0fe2fdee)
    
- Changed the packages part to be just 'categories' instead of 'django-categories'. [d03c2f2](https://github.com/jazzband/django-categories/commit/d03c2f29bdae7b94aa0936a816f498d2b51db167)
    
