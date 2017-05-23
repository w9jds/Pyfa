# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

from service.attribute import Attribute  # noqa: E402, E401


def test_attribute():
    """
    We don't really have much to test here, so throw a generic attribute at it and validate we get the expected results

    :return:
    """
    sAttr = Attribute.getInstance()
    info = sAttr.getAttributeInfo("maxRange")

    assert info.attributeID == 54
    assert isinstance(info.attributeID, int)
    assert info.attributeName == 'maxRange'
    assert isinstance(info.attributeName, unicode)
    assert info.defaultValue == 0.0
    assert isinstance(info.defaultValue, float)
    assert info.description == 'Distance below which range does not affect the to-hit equation.'
    assert isinstance(info.description, unicode)
    assert info.displayName == 'Optimal Range'
    assert isinstance(info.displayName, unicode)
    assert info.highIsGood is True
    assert isinstance(info.highIsGood, bool)
    assert info.iconID == 1391
    assert isinstance(info.iconID, int)
    assert info.name == 'maxRange'
    assert isinstance(info.name, unicode)
    assert info.published is True
    assert isinstance(info.published, bool)
    assert info.unitID == 1
    assert isinstance(info.unitID, int)
    assert info.unit.ID == 1
    assert isinstance(info.unit.ID, int)
    assert info.unit.displayName == 'm'
    assert isinstance(info.unit.displayName, unicode)
    assert info.unit.name == 'Length'
    assert isinstance(info.unit.name, unicode)
    assert info.unit.unitID == 1
    assert isinstance(info.unit.unitID, int)
    assert info.unit.unitName == 'Length'
    assert isinstance(info.unit.unitName, unicode)
