def between(min, max):
    """
        Returns a function that returns True when a number, x, 
        is between the min and the max, otherwise False
    """
    def func(x):
        return min <= x <= max
    return func


def is_digit_pound_start(string):
    """
        Returns True if all the characters in the string are comprised
        of digits [0-9], pound ( # ) or star ( * ), otherwise False
    """
    return all([char.isdigit() or char in ('#', '*') for char in string])


METHODS = ('GET', 'POST')


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

