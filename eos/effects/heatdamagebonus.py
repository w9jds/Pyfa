# heatDamageBonus
#
# Used by:
# Modules from group: Shield Boost Amplifier (25 of 25)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "heatDamage", container.getModifiedItemAttr("heatDamageBonus"))
