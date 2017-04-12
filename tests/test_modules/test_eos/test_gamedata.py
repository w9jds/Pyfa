# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import os
import sys
import os

sys.path.append(os.path.realpath(os.getcwd()))

# noinspection PyPackageRequirements
from _development.helpers import DBInMemory as DB, Gamedata, Saveddata
from _development.helpers_fits import RifterFit, KeepstarFit


def test_race(DB, RifterFit, KeepstarFit):
    """
    Test race code
    """
    assert RifterFit.ship.item.race == 'minmatar'
    assert KeepstarFit.ship.item.race == 'upwell'
