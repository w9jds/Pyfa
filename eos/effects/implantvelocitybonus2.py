# implantVelocityBonus2
#
# Used by:
# Implant: Republic Special Ops Field Enhancer - Gamma
effectType = "passive"


def handler(fit, implant, context):
    fit.ship.boostItemAttr("maxVelocity", implant.getModifiedItemAttr("velocityBonus2"))
