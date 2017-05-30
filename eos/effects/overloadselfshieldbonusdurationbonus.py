# overloadSelfShieldBonusDurationBonus
#
# Used by:
# Modules from group: Ancillary Shield Booster (5 of 5)
# Modules from group: Shield Booster (93 of 93)
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("duration", container.getModifiedItemAttr("overloadSelfDurationBonus"))
    container.boostItemAttr("shieldBonus", container.getModifiedItemAttr("overloadShieldBonus"), stackingPenalties=True)
