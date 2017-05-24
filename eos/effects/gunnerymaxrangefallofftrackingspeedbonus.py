# gunneryMaxRangeFalloffTrackingSpeedBonus
#
# Used by:
# Modules from group: Tracking Computer (11 of 11)
effectType = "active"


def handler(fit, container, context):
    for attr in ("maxRange", "falloff", "trackingSpeed"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      attr, container.getModifiedItemAttr("%sBonus" % attr),
                                      stackingPenalties=True)
