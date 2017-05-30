# eliteBonusExpeditionMining1
#
# Used by:
# Ship: Prospect
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "miningAmount", container.getModifiedItemAttr("eliteBonusExpedition1"),
                                  skill="Expedition Frigates")
