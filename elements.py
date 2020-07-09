from texmlelement import TeXMLElement
from options import between, is_digit_pound_star, METHODS, LANGUAGES


class Response(TeXMLElement):
    _name = 'Response'

    def __init__(self):
        super().__init__()


class Dial(TeXMLElement):
    _name = 'Dial'
    _attributes = dict(
        action=None,
        method=METHODS,
        caller_id=None,
        hangup_on_star=(True, False),
        record=(
            'do-not-record', 
            'record-from-answer', 
            'record-from-ringing', 
            'record-from-answer-dual', 
            'record-from-ringing-dual'
        ),
        recording_status_callback=None,
        recording_status_callback_method=METHODS,
        recording_status_callback_event=(
            'in-progress', 
            'completed', 
            'absent'
        )
    )
    _nouns = ('Number', 'Sip', 'Conference')


class Number(TeXMLElement):
    _name = 'Number'
    _attributes = dict(
        status_callback=None,
        status_callback_event=(
            'initiated', 
            'ringing', 
            'answered', 
            'completed'
        ),
        status_callback_method=METHODS,
        url=None,
        method=METHODS,
        send_digits=lambda s: s.isdigit()
    )
    

class Sip(TeXMLElement):
    _name = 'Sip'
    _attributes = dict(
        status_callback=None,
        status_callback_event=(
            'initiated', 
            'ringing', 
            'answered', 
            'completed'
        ),
        status_callback_method=METHODS,
        url=None,
        method=METHODS
    )  


class Conference(TeXMLElement):
    _name = 'Conference'
    _attributes = dict(
        beep=(True, False, 'onEnter', 'onExit'),
        muted=(True, False),
        start_conference_on_enter=(True, False),
        end_conference_on_exit=(True, False),
        status_callback=None,
        status_callback_event=('start', 'end', 'join', 'leave'),
        status_callback_method=METHODS
    )
    

class Gather(TeXMLElement):
    _name = 'Gather'
    _attributes = dict(
        action=None,
        finish_on_key=is_digit_pound_star,
        num_digits=None,
        language=LANGUAGES,
        timeout=between(1, 120)
    )
    _nouns = ('Say', 'Play')


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
        method=METHODS,
        finish_on_key=is_digit_pound_star,
        play_beep=(True, False),
        recording_status_callback=None,
        recording_status_callback_method=METHODS
    )


class Redirect(TeXMLElement):
    _name = 'Record'
    _attributes = dict(
        method=METHODS
    )


class Reject(TeXMLElement):
    _name = 'Reject'
    _attributes=dict(
        reason=('rejected', 'busy')
    )


class Say(TeXMLElement):
    _name = 'Say'
    _attributes = dict(
        voice=('man', 'woman', 'alice'),
        language=LANGUAGES,
        loop=between(0, 100)
    )