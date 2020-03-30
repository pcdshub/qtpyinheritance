from qtpy import QtWidgets

import qtpyinheritance.properties
from qtpyinheritance.properties import forward_property, forward_properties


def test_forward_properties(qtbot):
    class MyClass(QtWidgets.QFrame):
        def __init__(self, parent=None):
            super().__init__(parent=parent)
            self.label = QtWidgets.QLabel()

        locals().update(**forward_properties(
            locals_dict=locals(),
            attr_name='label',
            cls=QtWidgets.QLabel,
            superclasses=[QtWidgets.QFrame]
        ))

    assert isinstance(MyClass.label_font,
                      qtpyinheritance.properties.PassthroughProperty)
    assert isinstance(MyClass.label_minimized,
                      qtpyinheritance.properties.ReadonlyPassthroughProperty)

    obj = MyClass()
    assert hasattr(obj, 'label_text')
    obj.label_text
    obj.label_text = 'a'
    assert hasattr(obj, 'label_font')
    obj.label_minimized


def test_forward_property(qtbot):
    class MyClass(QtWidgets.QFrame):
        def __init__(self, parent=None):
            super().__init__(parent=parent)
            self.label = QtWidgets.QLabel()

        label_text = forward_property('label', QtWidgets.QLabel, 'text')
        label_minimized = forward_property('label', QtWidgets.QLabel,
                                           'minimized')

    assert isinstance(MyClass.label_text,
                      qtpyinheritance.properties.PassthroughProperty)
    assert isinstance(MyClass.label_minimized,
                      qtpyinheritance.properties.ReadonlyPassthroughProperty)
    obj = MyClass()
    assert hasattr(obj, 'label_text')
    obj.label_text
    obj.label_text = 'a'
    obj.label_minimized
