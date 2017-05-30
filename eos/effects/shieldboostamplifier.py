# shieldBoostAmplifier
#
# Used by:
# Modules from group: Capacitor Power Relay (20 of 20)
# Modules from group: Shield Boost Amplifier (25 of 25)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(
            lambda mod: mod.item.requiresSkill("Shield Operation") or mod.item.requiresSkill("Capital Shield Operation"),
            "shieldBonus", container.getModifiedItemAttr("shieldBoostMultiplier"),
            stackingPenalties=True)
