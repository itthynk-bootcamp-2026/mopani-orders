# loyalty.py - written in 2011 for Python 2.7. Nobody remembers how it works.
import string

def calc_points(orders):
    pts = 0
    for i in range(0, len(orders)):
        o = orders[i]
        if o.has_key('amount') and o['amount'] <> None:
            if o['amount'] > 500:
                pts = pts + int(o['amount'] / 10) * 2
            else:
                pts = pts + int(o['amount'] / 10)
    print "points: %d" % pts
    return pts

def tier(pts):
    if pts >= 1000: return 'GOLD'
    elif pts >= 300: return 'SILVER'
    else: return 'BRONZE'
