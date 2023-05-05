要在 Django 项目中使用 Behave 进行测试，您需要遵循以下步骤：

1. 安装 Behave 和 Django-Behave-Runner：

```
pip install behave django-behave
```

2. 在您的 Django 项目的 `settings.py` 文件中，将 `'django_behave.runner.djangotestrunner'` 添加到您的测试运行器,还有INSTALLED_APPS：

```python
INSTALLED_APPS = [
     ...
    'behave_django',
]

TEST_RUNNER = 'behave_django.runner.BehaviorDrivenTestRunner'
```

3. 在您的 Django manage.py平行创建一个名为 `features` 的目录，该目录将包含您的功能文件和步骤定义。

例如，在名为 `myapp` 的应用程序中：

```
myapp/
    features/
        steps/
            __init__.py
            myapp_steps.py
        myapp.feature
        environment.py
```

4. 编写功能文件 (`.feature`)。功能文件使用 Gherkin 语言编写，描述了应用程序的期望行为。例如，在 `myapp.feature` 中：

```
Feature: MyApp feature

  Scenario: Basic test
    Given I have a basic Django application
    When I run a test
    Then the test should pass
```

5. 编写对应的步骤定义。在 `myapp/features/steps/myapp_steps.py` 文件中，您需要定义与功能文件中描述的步骤匹配的 Python 函数。

```python
from behave import given, when, then

@given('I have a basic Django application')
def step_given_i_have_a_basic_django_application(context):
    pass

@when('I run a test')
def step_when_i_run_a_test(context):
    pass

@then('the test should pass')
def step_then_the_test_should_pass(context):
    pass
```

6. 运行测试：

```
python manage.py test myapp
```

# 例子：
myapp_steps.py：
```python
from behave import given, when, then
from django.test import Client
from user.models import User
from django.contrib.auth.hashers import make_password
import random
import string

def random_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "@example.com"

@given('a user is logged in')
def step_given_a_user_is_logged_in(context):
    # Create a test user and log them in
    User.objects.filter(name='admin-test').delete()
    context.user = User.objects.create(name='admin-test', email=random_email(), password=make_password('123456'))
    context.client = Client()  # Initialize Django test client
    response = context.client.post('/user/login/', {'username': 'admin-test', 'password': '123456'})
    assert response.status_code == 302

@when('the user accesses their cart')
def step_when_the_user_accesses_their_cart(context):
    # Access the cart page
    response = context.client.get('/order/cart/')
    context.cart_response = response

@then('the cart should be displayed with the correct products and quantities')
def step_then_the_cart_should_be_displayed_with_the_correct_products_and_quantities(context):
    # Check the cart response
    assert context.cart_response.status_code == 200

@when('the user accesses their order history')
def step_when_the_user_accesses_their_order_history(context):
    # Access the order history page
    context.order_response = context.client.get('/order/')

@then('the order history should display the correct orders with product information')
def step_then_the_order_history_should_display_the_correct_orders_with_product_information(context):
    # Check the order history response
    assert context.order_response.status_code == 200

```
myapp.feature：
```python
Feature: Cart and Order Management

Scenario: Accessing the Cart
Given a user is logged in
When the user accesses their cart
Then the cart should be displayed with the correct products and quantities

Scenario: Accessing Orders
Given a user is logged in
When the user accesses their order history
Then the order history should display the correct orders with product information
```

environment.py：
```python
from behave import fixture, use_fixture
from django.test import RequestFactory
from django.test.runner import DiscoverRunner
import sys
import os
from django import setup
from django.urls import reverse
from django.test import RequestFactory
from django.conf import settings

def before_all(context):
    settings.DEBUG = False
    context.factory = RequestFactory()

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# 将项目根目录添加到sys.path
if project_root not in sys.path:
    sys.path.append(project_root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shop.settings'
setup()

@fixture
def django_test_runner(context):
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()
    context.request_factory = RequestFactory()
    yield
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()

def before_all(context):
    use_fixture(django_test_runner, context)
```

最后在manage.py所在目录执行behave就行了

以下是返回结果：
![example]([https://raw.githubusercontent.com/用户名/my-repo/master/example.png](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230505125939.png))



