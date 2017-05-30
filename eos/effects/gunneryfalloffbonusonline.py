# gunneryFalloffBonusOnline
#
# Used by:
# Modules from group: Tracking Enhancer (10 of 10)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "falloff", container.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties=True)
