MailChimp API v2.0 Python Example Application
=============================================
An example application utilizing our [official python API wrapper](https://pypi.python.org/pypi/mailchimp). The purpose of the app is to demo setting up the wrapper in a common environment, make some basic API calls against our API, and consume/display the results. This will not necessarilly show an example of every available method or the numerous permutations of each. For that, the developer will be expected to refer to the [the API v2 docs](http://apidocs.mailchimp.com/api/2.0/) and wrapper source to test calls. This, however, should provide a simple framework to kickstart testing.

Community
---------
Unlike our [official API wrapper](https://pypi.python.org/pypi/mailchimp) which is generated and thus non-conducive to pull requests, we'll be happy to consider them to:

* update existing examples
* add new basic functionality, especially for calls that you've found non-trivial
* foster best practices for the language

Just please remember this is intended as a beginner's demo, so please try to keep things organized and [K.I.S.S.](http://en.wikipedia.org/wiki/KISS_principle).

Installation
------------
### The Django one

* Clone the repo or download the example code and put it ... somewhere.
* then these commands will get you setup in a virtualenv

```
$ pip install virtualenv
$ virtualenv mcapi_example_env
$ source mcapi_example_env/bin/activate
$ pip install Django==1.4.5
$ django-admin.py startproject --extension=py,json --template=/path/to/django_in_the_repo mcapi_example
$ cd mcapi_example
$ pip install -r requirements.txt
```
Then:

* edit `mcapi_python_example/utils.py` and enter your api key
* run `python manage.py runserver`
* point your browser at http://127.0.0.1:8000/


