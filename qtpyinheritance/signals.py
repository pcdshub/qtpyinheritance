import inspect
import functools

from qtpy import QtCore


def should_inherit(obj, *, signals=True, slots=True):
    '''
    Check a single object to see if it should be inherited

    Parameters
    ----------
    obj : any
        The object itself
    signals : bool, optional
        Include signals
    slots : bool, optional
        Include slots
    '''
    try:
        if signals and isinstance(obj, QtCore.Signal):
            return True
        if slots and callable(obj) and hasattr(obj, '__pyqtSignature__'):
            return True
    except Exception:
        ...
    return False


def inherit(*superclasses, signals=True, slots=True, predicate=None):
    '''
    "Inherit" signals and slots from superclasses

    Parameters
    ----------
    *superclasses
        The superclasses of the class
    signals : bool, optional
        Include signals
    slots : bool, optional
        Include slots
    predicate : callable, optional
        Further filter potential values based on the given predicate, which
        should have a signature of ``predicate(cls, attr, obj)``.

    Returns
    -------
    clsdict : dict
        A dictionary of {attr: obj} that should be used to update the class
        body.
    '''
    temp_class = type('temp_class', superclasses, {})
    result = {}
    check = functools.partial(should_inherit, signals=signals, slots=slots)
    for cls in reversed(temp_class.mro()[1:]):
        for attr, obj in inspect.getmembers(cls, predicate=check):
            if predicate is None or predicate(cls, attr, obj):
                result[attr] = obj
    return result
