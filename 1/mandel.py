import numpy as np
import matplotlib.pyplot as plt
#from functools import lru_cache
#@lru_cache(maxsize = 10000)
def mandelbrot( h,w, maxit=50 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.9:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**3 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 20                        # avoid diverging too much

    return divtime
plt.imshow(mandelbrot(300,300))
plt.show()

