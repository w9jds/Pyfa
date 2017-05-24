# Not used by any item
effectType = "active"
runTime = "early"


def handler(fit, container, context):
    # Resistances
    for layer, attrPrefix in (('shield', 'shield'), ('armor', 'armor'), ('hull', '')):
        for damageType in ('Kinetic', 'Thermal', 'Explosive', 'Em'):
            bonus = "%s%sDamageResonance" % (attrPrefix, damageType)
            bonus = "%s%s" % (bonus[0].lower(), bonus[1:])
            booster = "%s%sDamageResonance" % (layer, damageType)
            penalize = False if layer == 'hull' else True
            fit.ship.multiplyItemAttr(bonus, container.getModifiedItemAttr(booster),
                                      stackingPenalties=penalize, penaltyGroup="preMul")

    # Turrets
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret") or
                                              mod.item.requiresSkill("Large Hybrid Turret") or
                                              mod.item.requiresSkill("Large Projectile Turret"),
                                  "maxRange", container.getModifiedItemAttr("maxRangeBonus"),
                                  stackingPenalties=True)
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret") or
                                              mod.item.requiresSkill("Large Hybrid Turret") or
                                              mod.item.requiresSkill("Large Projectile Turret"),
                                  "falloff", container.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties=True)

    # Missiles
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes") or
                                                mod.charge.requiresSkill("Cruise Missiles") or
                                                mod.charge.requiresSkill("Heavy Missiles"),
                                    "maxVelocity", container.getModifiedItemAttr("missileVelocityBonus"))

    # Tanking
    fit.modules.filteredItemBoost(
            lambda mod: mod.item.requiresSkill("Capital Repair Systems") or mod.item.requiresSkill("Repair Systems"),
            "armorDamageAmount", container.getModifiedItemAttr("armorDamageAmountBonus"),
            stackingPenalties=True)
    fit.modules.filteredItemBoost(
            lambda mod: mod.item.requiresSkill("Capital Shield Operation") or mod.item.requiresSkill("Shield Operation"),
            "shieldBonus", container.getModifiedItemAttr("shieldBoostMultiplier"),
            stackingPenalties=True)

    # Speed penalty
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("speedFactor"))

    # Max locked targets
    fit.ship.forceItemAttr("maxLockedTargets", container.getModifiedItemAttr("maxLockedTargets"))

    # Block Hostile ewar
    fit.ship.forceItemAttr("disallowOffensiveModifiers", container.getModifiedItemAttr("disallowOffensiveModifiers"))
