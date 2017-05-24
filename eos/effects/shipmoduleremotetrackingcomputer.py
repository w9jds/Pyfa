# shipModuleRemoteTrackingComputer
#
# Used by:
# Modules from group: Remote Tracking Computer (8 of 8)
effectType = "projected", "active"


def handler(fit, container, context, **kwargs):
    if "projected" in context:
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus"),
                                      stackingPenalties=True, **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "maxRange", container.getModifiedItemAttr("maxRangeBonus"),
                                      stackingPenalties=True, **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "falloff", container.getModifiedItemAttr("falloffBonus"),
                                      stackingPenalties=True, **kwargs)
