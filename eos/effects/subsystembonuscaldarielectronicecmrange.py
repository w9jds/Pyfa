# subsystemBonusCaldariElectronicECMRange
#
# Used by:
# Subsystem: Tengu Electronics - Obfuscation Manifold
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                                  skill="Caldari Electronic Systems")
