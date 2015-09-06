# `emcee_functools`

Convenience function helpers for `emcee`.

## Example usage:

```python
from emcee_functools import func_signature, Fixed, Variable

@func_signature(a=Fixed(), b=Variable())
def lnprob(**params):
    a = params['a']
    b = params['b']

    lnp = lnprob(**params)
    if np.isfinite(lnp):
        return 0.  # Placeholder, should actually return a probability here...

    return -np.inf
```
