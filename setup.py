from setuptools import setup, find_packages

long_description = "README.md"
setup(
    name='pythontranslate',
    version='0.0.2',
    author='divirad',
    author_email='divirad@gmx.de',
    description='Translate your stuff free and online with translate.yandex.com',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/Divirad/PythonTranslate',
    license='MIT',
    packages = find_packages(),
    zip_safe=False)