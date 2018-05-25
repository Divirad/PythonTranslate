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

##### This text must be shown:
* In the description of the software product (on the About page).
* In the help for the software product.
* On the official website of the software product.
* On all pages or screens where data from the service is used.

##### Requirements for font color:
* The font color of this text must match the font color of the main text.

##### Requirements for font size
* The font size of this text must not be smaller than the font size of the main text.

## What do i need?
![PythonVersion](https://img.shields.io/badge/Python-3.6-green.svg)

the following should be installed with Python 3.6

![PythonVersion](https://img.shields.io/badge/pip-urllib-green.svg)

![PythonVersion](https://img.shields.io/badge/pip-json-green.svg)

![PythonVersion](https://img.shields.io/badge/pip-enum-green.svg)

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

    from pythontranslate import Translator
    from private import APIKEY
    
    translator = Translator(APIKEY) 

___________
#

### Get Languages
##### Function
Returns all supported languages

    translator.get_supported_languages([arraytype], [ui])

##### returns:
    if LANG_GET_TYPE.DICT:
        returns supported languages as dictionary
                
        example:
        {
        'af': 'Afrikaans', 
        'am': 'Amharic', 
        'ar': 'Arabic', 
        ...
        }
                
    elif LANG_GET_TYPE.ARRAY:
        returns supported from-to translations as dictionary
                
        example:
        ['az-ru', 'be-bg', 'be-cs', 'be-de' ...]
            
    elif LANG_GET_TYPE.JSON_ALL:
        returns both as JSON-string
                
        example:
        {
        'dirs': ['az-ru', ...],
        'langs: {'af': 'Afrikaans', ...}
        }   

    
##### Params
* __arraytype:__
    * _Description:_ 
        
            Describes which data will be returned
             
    * _Type:_        
    
            LANG_GET_TYPE (Enum            
        
    * _Template Value:_
    
            LANG_GET_TYPE.JSON_ALL
* __ui:__ 
    * _Description:_ 
    
            In the response, supported languages are listed in the 
            langs field with the definitions of the language codes. 
            Language names are output in the language corresponding 
            to the code in this parameter.
            All the language codes are shown in the list of 
            supported languages.
    * _Type:_  
    
            str
    * _Template Value:_ 
            
            "en"
___________
#

### Detect language
    
##### Function
Detects a language a text is written in.

    translator.detect_language(text, [hint]):

##### returns:
the detected language

    str

##### Params
* __text:__
    * _Description:_
        
            Text to analyze 
    * _Type:_
            
            str
* __hint__:
    * _Description:_
        
            A list which are hints for the API 
            in which language the text is written in  
            example:
            "de, en"
    * _Type:_
            
            str
     
    * _Template Value:_ 
    
            None
_______           
#
            
### Translate
    
##### Function
Detects a language a text is written in.

    translator.translate(text, lang, [format]):
##### returns:
returns the translated array of strings with translations
    
    str[]
##### Params

* __text:__
    * _Description:_
            
            Text to translate
    * _Type:_
    
            str
* __lang:__
    * _Description:_
            
            The translation direction.
            You can set it in either of the following ways:
            As a pair of language codes separated by a hyphen
            (“from”-“to”).
            For example, en-ru indicates translating from English to Russian.
            
            As the target language code
            (for example, ru).
            In this case, the service tries to detect the source language automatically.
    * _Type:_
    
            str
            
* __format:__
    * _Description:_
            
            if PLAIN_TEXT:
                text is in plain text and will be returned in plain text
            elif HTML
                text is in HTML and will be returned in HTML
    * _Type:_ 
    
            FORMAT (Enum)
    * _Template Value:_ 
    
            FORMAT.PLAIN_TEXT
