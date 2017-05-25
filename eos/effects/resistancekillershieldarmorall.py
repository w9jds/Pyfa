# resistanceKillerShieldArmorAll
#
# Used by:
# Modules named like: Polarized (12 of 18)
effectType = "passive"


def handler(fit, container, context):
    for layer in ('armor', 'shield'):
        for dmgType in ('em', 'thermal', 'kinetic', 'explosive'):
            tgtAttr = '{}{}DamageResonance'.format(layer, dmgType.capitalize())
            fit.ship.forceItemAttr(tgtAttr, container.getModifiedItemAttr("resistanceKiller"))
