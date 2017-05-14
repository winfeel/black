#-------------------------------------------------------------------------------
# Name:        Black-Scholes Calculator w/ Dividend
# Created:     05/12/2017
# Licence:     UC Berkeley
#-------------------------------------------------------------------------------

from scipy import stats
import math

def black_scholes (cp, s, k, t, v, rf, div):
        """ Price an option using the Black-Scholes model.
        s: initial stock price
        k: strike price
        t: expiration time
        v: volatility
        rf: risk-free rate
        div: dividend
        cp: +1/-1 for call/put
        """

        d1 = ((math.log(s/k)+(rf-div+0.5*math.pow(v,2))*t))/(v*math.sqrt(t))
        d2 = d1 - v*math.sqrt(t)
        n1 = stats.norm.cdf(cp*d1)
        n2 = stats.norm.cdf(cp*d2)

        optprice = (cp*s*math.exp(-div*t)*stats.norm.cdf(cp*d1)) - (cp*k*math.exp(-rf*t)*stats.norm.cdf(cp*d2))
        return optprice,d1,d2,n1,n2
