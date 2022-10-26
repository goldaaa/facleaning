from facleaning import cleaning
from facleaning.LanguageCheck import reverse_parse, find_text, fa, en

text = 'این متن توسط goldaaa برای تست نوشته شده است'

reverse_fa = reverse_parse(text, search='fa')       # جستجوی کلمه های فارسی برای تغییر جهت کلمه
print(reverse_fa)
reverse_en = reverse_parse(text, search='en')       # جستجوی کلمه های انگلیسی برای تغییر جهت کلمه
print(reverse_en)

reverse_other_lang = reverse_parse(
    text=text,
    search=lambda word: find_text(word, "[A-Z a-z 1-9 ۱-۹]"),
    reverse_text=True
)       # جستجوی سایر موارد خواسته شده از طریق regex برای تغییر جهت کلمه
print(reverse_other_lang)

print(
    'lang fa word (تست): ', fa('تست'),
    '| lang fa word (goldaaa): ', fa('goldaaa')
)
print(
    'lang en word (تست): ', en('تست'),
    '| lang en word (goldaaa): ', en('goldaaa')
)


print(
    cleaning(
        text=text,
        lang='fa',                  # language fa or ar
        reverse_text=False,         # تغییر جهت کل متن
        reverse_other_char=True,    # تغییر جهت علامت ها
    )
)
