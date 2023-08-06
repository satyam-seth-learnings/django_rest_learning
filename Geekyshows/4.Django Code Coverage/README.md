[YouTube Video Link](https://youtu.be/f_xiy70g6_0)

[Django Doc Link](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#integration-with-coverage-py)

[Coverage Doc Link](https://coverage.readthedocs.io/en/7.2.7/)

Note- Required [XAMPP](https://www.apachefriends.org/) to run MySQL server

- Generate Coverage Report
```bash
coverage run --source='account' manage.py test account
```

- View Coverage Report
```bash
coverage report
```

- Coverage Report Sample
```bash
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
account\__init__.py                      0      0   100%
account\admin.py                        12      0   100%
account\apps.py                          4      0   100%
account\migrations\0001_initial.py       5      0   100%
account\migrations\__init__.py           0      0   100%
account\models.py                       36      2    94%
account\serializers.py                  27      1    96%
account\test\__init__.py                 0      0   100%
account\test\test_models.py             38      0   100%
account\test\test_serializers.py        35      0   100%
account\test\test_views.py             188      0   100%
account\urls.py                          3      0   100%
account\utils.py                        22      0   100%
account\views.py                       146      8    95%
--------------------------------------------------------
TOTAL                                  516     11    98%
```

- View Coverage Report in HTML format
```bash
coverage html
```