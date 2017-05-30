# TODO: Drop the `_2` from the file name once one of our fit files are renamed

# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

# noinspection PyPackageRequirements
from _development.helpers import DBInMemory as DB, Gamedata, Saveddata  # noqa: E402, E401
from _development.helpers_fits import RifterFit, KeepstarFit, HeronFit, GnosisFit  # noqa: E402, E401
from _development.helpers_items import DamageControlII, ExperimentalEnergizedAdaptiveNanoMembraneI, EnergizedAdaptiveNanoMembraneI  # noqa: E402, E401


def test_calculateModifiedAttributes(DB, RifterFit, KeepstarFit):  # noqa: F811
    rifter_modifier_dicts = {
        '_ModifiedAttributeDict__affectedBy'          : 26,
        '_ModifiedAttributeDict__forced'              : 0,
        '_ModifiedAttributeDict__intermediary'        : 0,
        '_ModifiedAttributeDict__modified'            : 26,
        '_ModifiedAttributeDict__multipliers'         : 22,
        '_ModifiedAttributeDict__overrides'           : 0,
        '_ModifiedAttributeDict__penalizedMultipliers': 0,
        '_ModifiedAttributeDict__postIncreases'       : 0,
        '_ModifiedAttributeDict__preAssigns'          : 0,
        '_ModifiedAttributeDict__preIncreases'        : 4,
    }

    # Test before calculating attributes
    for test_dict in rifter_modifier_dicts:
        assert len(getattr(RifterFit.ship.itemModifiedAttributes, test_dict)) == 0

    RifterFit.calculateFitAttributes()

    for test_dict in rifter_modifier_dicts:
        assert len(getattr(RifterFit.ship.itemModifiedAttributes, test_dict)) == rifter_modifier_dicts[test_dict]

    # Keepstars don't have any basic skills that would change their attributes
    keepstar_modifier_dicts = {
        '_ModifiedAttributeDict__affectedBy'          : 0,
        '_ModifiedAttributeDict__forced'              : 0,
        '_ModifiedAttributeDict__intermediary'        : 0,
        '_ModifiedAttributeDict__modified'            : 0,
        '_ModifiedAttributeDict__multipliers'         : 0,
        '_ModifiedAttributeDict__overrides'           : 0,
        '_ModifiedAttributeDict__penalizedMultipliers': 0,
        '_ModifiedAttributeDict__postIncreases'       : 0,
        '_ModifiedAttributeDict__preAssigns'          : 0,
        '_ModifiedAttributeDict__preIncreases'        : 0,
    }

    # Test before calculating attributes
    for test_dict in keepstar_modifier_dicts:
        assert len(getattr(KeepstarFit.ship.itemModifiedAttributes, test_dict)) == 0

    KeepstarFit.calculateFitAttributes()

    for test_dict in keepstar_modifier_dicts:
        assert len(getattr(KeepstarFit.ship.itemModifiedAttributes, test_dict)) == keepstar_modifier_dicts[test_dict]


def test_calculateStackingPenaltyNoPenalty(DB, Saveddata, GnosisFit, DamageControlII, ExperimentalEnergizedAdaptiveNanoMembraneI):  # noqa: F811
    resist_stats = {
        "armorEmDamageResonance",
        "armorThermalDamageResonance",
        "armorKineticDamageResonance",
        "armorExplosiveDamageResonance",
    }

    # Base stats
    # resists should equal 32.5%
    GnosisFit.clear()
    GnosisFit.calculateFitAttributes()
    for resist in resist_stats:
        assert GnosisFit.ship.getModifiedItemAttr(resist) == 0.675

    # Damage Control II
    # resists should equal 42.6%
    GnosisFit.clear()

    DamageControlII.state = Saveddata['State'].ONLINE
    GnosisFit.modules.append(DamageControlII)

    GnosisFit.calculateFitAttributes()

    for resist in resist_stats:
        assert GnosisFit.ship.getModifiedItemAttr(resist) == 0.57375

    # Damage Control II
    # Experimental Energized Adaptive Nano Membrane I
    # resists should equal 42.6%
    GnosisFit.clear()

    DamageControlII.state = Saveddata['State'].ONLINE
    GnosisFit.modules.append(ExperimentalEnergizedAdaptiveNanoMembraneI)

    GnosisFit.calculateFitAttributes()

    for resist in resist_stats:
        assert GnosisFit.ship.getModifiedItemAttr(resist) == 0.4876875


def test_calculateStackingPenaltyWithPenalty(DB, Saveddata, GnosisFit, EnergizedAdaptiveNanoMembraneI, ExperimentalEnergizedAdaptiveNanoMembraneI):  # noqa: F811
    resist_stats = {
        "armorEmDamageResonance",
        "armorThermalDamageResonance",
        "armorKineticDamageResonance",
        "armorExplosiveDamageResonance",
    }

    # Base stats
    # resists should equal 32.5%
    GnosisFit.clear()
    GnosisFit.calculateFitAttributes()
    for resist in resist_stats:
        assert GnosisFit.ship.getModifiedItemAttr(resist) == 0.675

    # Energized Adaptive Nano Membrane I
    # resists should equal 42.6%
    GnosisFit.clear()

    DamageControlII.state = Saveddata['State'].ONLINE
    GnosisFit.modules.append(EnergizedAdaptiveNanoMembraneI)

    GnosisFit.calculateFitAttributes()

    for resist in resist_stats:
        assert GnosisFit.ship.getModifiedItemAttr(resist) == 0.57375

    # Energized Adaptive Nano Membrane I
    # Experimental Energized Adaptive Nano Membrane I
    # resists should equal 50.1%
    GnosisFit.clear()

    DamageControlII.state = Saveddata['State'].ONLINE
    GnosisFit.modules.append(ExperimentalEnergizedAdaptiveNanoMembraneI)

    GnosisFit.calculateFitAttributes()

    for resist in resist_stats:
        assert GnosisFit.ship.getModifiedItemAttr(resist) == 0.49895136165236575


def test_calculateModifiedAttributes_withBooster(DB, RifterFit, HeronFit):  # noqa: F811
    # TODO: This test is not currently functional or meaningful as projections are not happening correctly.
    # This is true for all tested branches (master, dev, etc)
    rifter_modifier_dicts = {
        '_ModifiedAttributeDict__affectedBy'          : 26,
        '_ModifiedAttributeDict__forced'              : 0,
        '_ModifiedAttributeDict__intermediary'        : 0,
        '_ModifiedAttributeDict__modified'            : 26,
        '_ModifiedAttributeDict__multipliers'         : 22,
        '_ModifiedAttributeDict__overrides'           : 0,
        '_ModifiedAttributeDict__penalizedMultipliers': 0,
        '_ModifiedAttributeDict__postIncreases'       : 0,
        '_ModifiedAttributeDict__preAssigns'          : 0,
        '_ModifiedAttributeDict__preIncreases'        : 4,
    }

    # Test before calculating attributes
    for test_dict in rifter_modifier_dicts:
        assert len(getattr(RifterFit.ship.itemModifiedAttributes, test_dict)) == 0

    # Get base stats
    # max_target_range_1 = RifterFit.ship.getModifiedItemAttr('maxTargetRange')
    # scan_resolution_1 = RifterFit.ship.getModifiedItemAttr('scanResolution')

    RifterFit.clear()
    RifterFit.calculateFitAttributes()

    # Get self calculated stats
    # max_target_range_2 = RifterFit.ship.getModifiedItemAttr('maxTargetRange')
    # scan_resolution_2 = RifterFit.ship.getModifiedItemAttr('scanResolution')

    RifterFit.clear()
    # Project Heron fit onto Rifter
    RifterFit._Fit__projectedFits[HeronFit.ID] = HeronFit

    # DB['saveddata_session'].commit()
    # DB['saveddata_session'].flush()
    # DB['saveddata_session'].refresh(HeronFit)

    RifterFit.calculateFitAttributes()

    # Get stats with projections
    # max_target_range_3 = RifterFit.ship.getModifiedItemAttr('maxTargetRange')
    # scan_resolution_3 = RifterFit.ship.getModifiedItemAttr('scanResolution')

    RifterFit.clear()
    RifterFit.calculateFitAttributes(withBoosters=True)

    # Get stats with projections
    # max_target_range_4 = RifterFit.ship.getModifiedItemAttr('maxTargetRange')
    # scan_resolution_4 = RifterFit.ship.getModifiedItemAttr('scanResolution')

    RifterFit.clear()
    HeronFit.calculateFitAttributes(targetFit=RifterFit, withBoosters=True)
    RifterFit.calculateFitAttributes(withBoosters=True)

    # Get stats with projections
    # max_target_range_5 = RifterFit.ship.getModifiedItemAttr('maxTargetRange')
    # scan_resolution_5 = RifterFit.ship.getModifiedItemAttr('scanResolution')

    for test_dict in rifter_modifier_dicts:
        assert len(getattr(RifterFit.ship.itemModifiedAttributes, test_dict)) == rifter_modifier_dicts[test_dict]
