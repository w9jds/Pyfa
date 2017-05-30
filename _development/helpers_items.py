import pytest

# noinspection PyPackageRequirements
from _development.helpers import DBInMemory as DB, Gamedata, Saveddata  # noqa: F401


# noinspection PyShadowingNames
@pytest.fixture  # noqa: F811
def StrongBluePillBooster(DB, Gamedata, Saveddata):
    print("Creating Strong Blue Pill Booster")
    item = DB['gamedata_session'].query(Gamedata['Item']).filter(Gamedata['Item'].name == "Strong Blue Pill Booster").first()
    return Saveddata['Booster'](item)


# noinspection PyShadowingNames
@pytest.fixture  # noqa: F811
def DamageControlII(DB, Gamedata, Saveddata):
    print("Creating Damage Control II")
    item = DB['gamedata_session'].query(Gamedata['Item']).filter(Gamedata['Item'].name == "Damage Control II").first()
    return Saveddata['Module'](item)


# noinspection PyShadowingNames
@pytest.fixture  # noqa: F811
def ExperimentalEnergizedAdaptiveNanoMembraneI(DB, Gamedata, Saveddata):
    print("Creating Experimental Energized Adaptive Nano Membrane I")
    item = DB['gamedata_session'].query(Gamedata['Item']).filter(Gamedata['Item'].name == "Experimental Energized Adaptive Nano Membrane I").first()
    return Saveddata['Module'](item)


# noinspection PyShadowingNames
@pytest.fixture  # noqa: F811
def EnergizedAdaptiveNanoMembraneI(DB, Gamedata, Saveddata):
    print("Creating Energized Adaptive Nano Membrane I")
    item = DB['gamedata_session'].query(Gamedata['Item']).filter(Gamedata['Item'].name == "Energized Adaptive Nano Membrane I").first()
    return Saveddata['Module'](item)
