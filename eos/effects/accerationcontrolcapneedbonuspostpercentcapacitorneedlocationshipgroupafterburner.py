# accerationControlCapNeedBonusPostPercentCapacitorNeedLocationShipGroupAfterburner
#
# Used by:
# Modules named like: Dynamic Fuel Valve (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))
