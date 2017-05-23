# shipSHTFalloffBonusRookie
#
# Used by:
# Ship: Violator
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "falloff", ship.getModifiedItemAttr("rookieSHTFalloff"))
