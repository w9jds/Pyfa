# resistanceKillerHullAll
#
# Used by:
# Modules named like: Polarized (12 of 18)
effectType = "passive"


def handler(fit, container, context):
    for dmgType in ('em', 'thermal', 'kinetic', 'explosive'):
        tgtAttr = '{}DamageResonance'.format(dmgType)
        fit.ship.forceItemAttr(tgtAttr, container.getModifiedItemAttr("resistanceKillerHull"))
