from .texmlelement import TeXMLElement
from .options import between, is_digit_pound_star, METHODS, LANGUAGES


class ResponseElement(TeXMLElement):
    _tag = 'Response'
    _nouns = (
        'Dial',
        'Number',
        'Sip',
        'Conference',
        'Gather',
        'Hangup',
        'Pause',
        'Play',
        'Record',
        'Redirect',
        'Reject',
        'Say'
    )

    def __init__(self):
        super().__init__()


class DialElement(TeXMLElement):
    _tag = 'Dial'
    _attrs = dict(
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


class NumberElement(TeXMLElement):
    _tag = 'Number'
    _attrs = dict(
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

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)
    

class SipElement(TeXMLElement):
    _tag = 'Sip'
    _attrs = dict(
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

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)


class ConferenceElement(TeXMLElement):
    _tag = 'Conference'
    _attrs = dict(
        beep=(True, False, 'onEnter', 'onExit'),
        muted=(True, False),
        start_conference_on_enter=(True, False),
        end_conference_on_exit=(True, False),
        status_callback=None,
        status_callback_event=('start', 'end', 'join', 'leave'),
        status_callback_method=METHODS
    )

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)
    

class GatherElement(TeXMLElement):
    _tag = 'Gather'
    _attrs = dict(
        action=None,
        finish_on_key=is_digit_pound_star,
        num_digits=None,
        language=LANGUAGES,
        timeout=between(1, 120)
    )
    _nouns = ('Say', 'Play')


class HangupElement(TeXMLElement):
    _tag = 'Hangup'


class PauseElement(TeXMLElement):
    _tag = 'Pause'
    _attrs = dict(
        length=between(1, 180)
    )


class PlayElement(TeXMLElement):
    _tag = 'Play'
    _attrs = dict(
        loop=between(0, 100)
    )

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)


class RecordElement(TeXMLElement):
    _tag = 'Play'
    _attrs = dict(
        action=None,
        method=METHODS,
        finish_on_key=is_digit_pound_star,
        play_beep=(True, False),
        recording_status_callback=None,
        recording_status_callback_method=METHODS
    )


class RedirectElement(TeXMLElement):
    _tag = 'Record'
    _attrs = dict(
        method=METHODS
    )

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)


class RejectElement(TeXMLElement):
    _tag = 'Reject'
    _attrs=dict(
        reason=('rejected', 'busy')
    )


class SayElement(TeXMLElement):
    _tag = 'Say'
    _attrs = dict(
        voice=('man', 'woman', 'alice'),
        language=LANGUAGES,
        loop=between(0, 100)
    )

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)