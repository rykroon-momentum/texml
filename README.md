# texml
Telnyx TeXML library

## Example

```
from texml import ResponseElement, SayElement, DialElement, NumberElement

r = ResponseElement()
s = SayElement("Thank you for calling Telnyx. Please hold.")
d = DialElement()
n = NumberElement("+13129457420")

d.append(n)
r.append(s)
r.append(d)

print(str(r))
```

### Result
```
<Response>
  <Say>Thank you for calling Telnyx. Please hold.</Say>
  <Dial>
    <Number>+13129457420</Number>
  </Dial>
</Response>
```