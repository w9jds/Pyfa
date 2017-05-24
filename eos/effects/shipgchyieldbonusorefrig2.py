# shipGCHYieldBonusOREfrig2
#
# Used by:
# Ship: Prospect
# Ship: Venture
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Gas Cloud Harvester",
                                  "duration", container.getModifiedItemAttr("shipBonusOREfrig2"), skill="Mining Frigate")
