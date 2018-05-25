# PythonTranslate.py [![Build Status](https://travis-ci.org/Divirad/PythonTranslate.svg?branch=master)](https://travis-ci.org/Divirad/PythonTranslate)

![PythonVersion](https://img.shields.io/badge/Python-3.6-green.svg) 

A wrapper for [translate.Yandex.com](https://translate.Yandex.com)

Wrapper by Divirad(c)

### Requirements for the use of translation results
   
    According to the Terms of Use for the Yandex.Translate service,
    the text “Powered by Yandex.Translate” must be shown above
    or below the translation result, with a clickable link
    to the page http://translate.yandex.com/.
    Requirements for placing this text

    This text must be shown:
    * In the description of the software product (on the About page).
    * In the help for the software product.
    * On the official website of the software product.
    * On all pages or screens where data from the service is used.
    
    Requirements for font color:
    The font color of this text must match the font color of the main text.

    Requirements for font size
    The font size of this text must not be smaller than the font size of the main text.
    
## Installation
   ![PythonVersion](https://img.shields.io/badge/WARING-Not%20supported%20yet!-darkred.svg) 
   
    pipenv install pythontranslate

## How to use it? 
First you have to get an Api-Key from this Site 

[Get API Key](https://translate.yandex.com/developers/keys)

Keep in mind that it's not safe to upload your API-Key publicly on Github.
We recommend you to save it in an private.py file to import it localy into your project.


##### private.py
    
    # DONT UPLOAD TO GITHUB
    APIKEY = "<your key here>"

After that create an object in your file you want to translate something.

##### main.py 

    from pythontranslate import *
    from private import APIKEY
    
    translator = Translator(APIKEY) 

___________

# And [read the fking wiki](https://github.com/Divirad/PythonTranslate/wiki)
