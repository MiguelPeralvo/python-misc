#IP address validation for Hackerrank.
#8/2014 - Miguel Peralvo
import re


N=int(input())
assert N<=50 and N>=1

pattern = re.compile(r"""
^
(?P<IPv4>^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$)
|
(?P<IPv6>^([A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$)                                                                                                                                               
""", re.VERBOSE|re.IGNORECASE)

for _ in xrange(N):
    b=str(raw_input())
    assert len(b)<=500
    matching = pattern.match(b)

    if matching:
        print "IPv4" if matching.group("IPv4") else "IPv6" if matching.group("IPv6") else "Neither"
    else:
        print "Neither"
