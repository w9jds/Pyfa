# eliteBonusCoverOpsNOSNeutFalloff1
#
# Used by:
# Ship: Caedes
effectType = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in ("Energy Nosferatu", "Energy Neutralizer"),
                                  "falloffEffectiveness", src.getModifiedItemAttr("eliteBonusCoverOps1"),
                                  stackingPenalties=True, skill="Covert Ops")
