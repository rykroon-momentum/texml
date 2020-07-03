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


class Response(TeXMLElement):
    _name = 'Response'

    def __init__(self):
        super().__init__()


class Dial(TeXMLElement):
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

    _name = 'Dial'

    _nouns = ['Number', 'Sip', 'Conference']


class Number(TeXMLElement):
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
    _name = 'Number'

class Sip(TeXMLElement):
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
    _name = 'Sip'


class Conference(TeXMLElement):
    _attributes = dict(
        beep=[True, False, 'onEnter', 'onExit'],
        muted=[True, False],
        start_conference_on_enter=[True, False],
        end_conference_on_exit=[True, False],
        status_callback=None,
        status_callback_event=['start', 'end', 'join', 'leave'],
        status_callback_method=['GET', 'POST']
    )
    _name = 'Conference'

class Gather(TeXMLElement):
    _attributes = dict(
        action=None,
        finish_on_key=is_digit_pound_star,
        num_digits=None,
        language=languages,
        timeout=lambda i: 1 <= i <= 120
    )
    _name = 'Gather'
    _nouns = ['Say', 'Play']


class Hangup(TeXMLElement):
    _name = 'Hangup'


class Pause(TeXMLElement):
    _attributes = dict(
        length=lambda i: 1 <= i <= 180
    )
    _name = 'Pause'


class Play(TeXMLElement):
    _attributes = dict(
        loop=lambda i: 0 <= i <= 100
    )
    _name = 'Play'


class Record(TeXMLElement):
    _attributes = dict(
        action=None,
        method=['GET', 'POST'],
        finish_on_key=is_digit_pound_star,
        play_beep=[True, False],
        recording_status_callback=None,
        recording_status_callback_method=['GET', 'POST']
    )
    _name = 'Play'


class Redirect(TeXMLElement):
    _attributes = dict(
        method=['GET', 'POST']
    )
    _name = 'Record'


class Reject(TeXMLElement):
    _attributes=dict(
        reason=['rejected', 'busy']
    )
    _name = 'Reject'


class Say(TeXMLElement):
    _attributes = dict(
        voice=['man', 'woman', 'alice'],
        language=languages,
        loop=lambda i: 0 <= i <= 100
    )
    _name = 'Say'