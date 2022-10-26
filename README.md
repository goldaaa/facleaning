# facleaning

Improved display of persian text

Download
--------

Installation through pypi.

    pip install facleaning --user

You can also install from this repository.

    git clone https://github.com/goldaaa/facleaning.git

Then, install the library with

    python setup.py install


Importing
---------

Import kivyir commands, menus, and the shell

    from facleaning import cleaning
    from facleaning.LanguageCheck import reverse_parse, find_text, fa, en
 

Commands
--------

Commands that can be used

    from facleaning.LanguageCheck import reverse_parse, find_text, fa, en
    
    text = 'این متن توسط goldaaa برای تست نوشته شده است'

    reverse_parse(text, search='fa')  # جستجوی کلمه های فارسی برای تغییر جهت کلمه

    reverse_parse(text, search='en')  # جستجوی کلمه های انگلیسی برای تغییر جهت کلمه
    
    
    # Search for other items requested via regex to change the direction of the word 
    # جستجوی سایر موارد خواسته شده از طریق regex برای تغییر جهت کلمه
    reverse_parse(
        text=text,
        search=lambda word: find_text(word, "[A-Z a-z 1-9 ۱-۹]"),
        reverse_text=True
    )
    
    test_fa = (
        'lang fa word (تست): ', fa('تست'),
        '| lang fa word (goldaaa): ', fa('goldaaa')
    )
    test_en = (
        'lang en word (تست): ', en('تست'),
        '| lang en word (goldaaa): ', en('goldaaa')
    )


    from facleaning import cleaning
    cleaning(
        text=text,
        lang='fa',                  # language fa or ar
        reverse_text=False,         # Change the direction of the entire text | تغییر جهت کل متن
        reverse_other_char=True,    # Change direction of signs | تغییر جهت علامت ها
    )


If you are interested in financial support, you can send a message through Gmail if you have any questions.

اگر قصد حمایت مالی یا سوال دارید می توانید از طریق جیمیل پیام ارسال کنید.

gmail: goldaaa.program@gmail.com

[github facleaning](https://github.com/goldaaa/facleaning)
