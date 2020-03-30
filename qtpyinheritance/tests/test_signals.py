import collections

import qtpy
from qtpy import QtCore

import qtpyinheritance.signals


print(qtpy.QT_VERSION, qtpy.API_NAME)


class BaseA(QtCore.QObject):
    signal_a = QtCore.Signal(str)

    @QtCore.Slot(str)
    def slot_a(self, value):
        print('slot a', value)
        self.call_info['slot_a'].append(value)


class BaseB(QtCore.QObject):
    signal_b = QtCore.Signal(str)

    @QtCore.Slot(str)
    def slot_b(self, value):
        print('slot b', value)
        self.call_info['slot_b'].append(value)


class Cls(BaseA, BaseB):
    locals().update(**qtpyinheritance.signals.inherit(BaseA, BaseB))

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.call_info = collections.defaultdict(lambda: [])

    @QtCore.Slot(str)
    def slot_c(self, value):
        print('slot c', value)
        self.call_info['slot_c'].append(value)

    @QtCore.Slot(str)
    def slot_b(self, value):
        self.call_info['cls_slot_b'].append(value)
        super().slot_b('super call' + value)


def test_simple(qtbot):
    obj = Cls()
    obj.signal_a.connect(obj.slot_a)
    obj.signal_a.connect(obj.slot_c)
    obj.signal_b.connect(obj.slot_b)
    obj.signal_b.connect(obj.slot_c)
    obj.signal_a.emit('-sig-a-')
    obj.signal_b.emit('-sig-b-')
    ci = obj.call_info
    assert ci['slot_a'] == ['-sig-a-']
    assert ci['cls_slot_b'] == ['-sig-b-']
    assert ci['slot_b'] == ['super call-sig-b-']
    assert ci['slot_c'] == ['-sig-a-', '-sig-b-']
