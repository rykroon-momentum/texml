from texmlelement import TeXMLElement

languages = [
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
]

#Returns True if the string is only comprised of digits [0-9], '#', or '*'
is_digit_pound_star = lambda s: all([c.isdigit() or c in ('#', '*') for c in s])

def between(min, max):
    def func(x):
        return min <= x <= max
    return func


class Response(TeXMLElement):
    _name = 'Response'

    def __init__(self):
        super().__init__()


class Dial(TeXMLElement):
    _name = 'Dial'
    _attributes = dict(
        action=None,
        method=['GET', 'POST'],
        caller_id=None,
        hangup_on_star=[True, False],
        record=[
            'do-not-record', 
            'record-from-answer', 
            'record-from-ringing', 
            'record-from-answer-dual', 
            'record-from-ringing-dual'
        ],
        recording_status_callback=None,
        recording_status_callback_method=['GET', 'POST'],
        recording_status_callback_event=[
            'in-progress', 
            'completed', 
            'absent'
        ]
    )
    _nouns = ['Number', 'Sip', 'Conference']


class Number(TeXMLElement):
    _name = 'Number'
    _attributes = dict(
        status_callback=None,
        status_callback_event=[
            'initiated', 
            'ringing', 
            'answered', 
            'completed'
        ],
        status_callback_method=['GET', 'POST'],
        url=None,
        method=['GET', 'POST'],
        send_digits=lambda s: s.isdigit()
    )
    

class Sip(TeXMLElement):
    _name = 'Sip'
    _attributes = dict(
        status_callback=None,
        status_callback_event=[
            'initiated', 
            'ringing', 
            'answered', 
            'completed'
        ],
        status_callback_method=['GET', 'POST'],
        url=None,
        method=['GET', 'POST']
    )  


class Conference(TeXMLElement):
    _name = 'Conference'
    _attributes = dict(
        beep=[True, False, 'onEnter', 'onExit'],
        muted=[True, False],
        start_conference_on_enter=[True, False],
        end_conference_on_exit=[True, False],
        status_callback=None,
        status_callback_event=['start', 'end', 'join', 'leave'],
        status_callback_method=['GET', 'POST']
    )
    

class Gather(TeXMLElement):
    _name = 'Gather'
    _attributes = dict(
        action=None,
        finish_on_key=is_digit_pound_star,
        num_digits=None,
        language=languages,
        timeout=between(1, 120)
    )
    _nouns = ['Say', 'Play']


class Hangup(TeXMLElement):
    _name = 'Hangup'


class Pause(TeXMLElement):
    _name = 'Pause'
    _attributes = dict(
        length=between(1, 180)
    )


class Play(TeXMLElement):
    _name = 'Play'
    _attributes = dict(
        loop=between(0, 100)
    )


class Record(TeXMLElement):
    _name = 'Play'
    _attributes = dict(
        action=None,
        method=['GET', 'POST'],
        finish_on_key=is_digit_pound_star,
        play_beep=[True, False],
        recording_status_callback=None,
        recording_status_callback_method=['GET', 'POST']
    )


class Redirect(TeXMLElement):
    _name = 'Record'
    _attributes = dict(
        method=['GET', 'POST']
    )


class Reject(TeXMLElement):
    _name = 'Reject'
    _attributes=dict(
        reason=['rejected', 'busy']
    )


class Say(TeXMLElement):
    _name = 'Say'
    _attributes = dict(
        voice=['man', 'woman', 'alice'],
        language=languages,
        loop=between(0, 100)
    )