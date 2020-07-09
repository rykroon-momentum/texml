

def between(min, max):
    def func(x):
        return min <= x <= max
    return func


#Returns True if the string is only comprised of digits [0-9], '#', or '*'
is_digit_pound_star = lambda s: all([c.isdigit() or c in ('#', '*') for c in s])

GET_OR_POST = ('GET', 'POST')


LANGUAGES = (
    "arb",
    "cmn-CN",
    "cy-GB",
    "da-DK",
    "de-DE",
    "en-AU",
    "en-GB",
    "en-GB-WLS",
    "en-IN",
    "en-US",
    "es-ES",
    "es-MX",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "is-IS",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "nb-NO",
    "nl-NL",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "sv-SE",
    "tr-TR"
)

