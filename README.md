# Smite JSON Data

#### Version 1.0.0

This is for my personal data collection, to run data analysis on smite Gods, Items, and hopefully Maps, in a temporal manner.


## Guidelines

- Add a new file for each gods in the _gods folder
- Inside the root we will have the following information:
    -  Name (Name of the god)
    -  Release date (Date when god was first introduced into the game)
    -  Pantheon (Pantheon the god belongs to)
    -  Role (Gaurdian/Warrior/Mage/Hunter/Assassin)
    -  Type (Physical/Magical)
    -  Basic Attack Type (Melee/Ranged)
    -  Seasons (Empty JSON Object. Will be defined completely in the future.)

(This is Tentative and not currently required)<br>
<s>-  Inside the _Seasons_ JSON, there will be one entry for each season and the value will be a list of JSON Objects having the following:
    -  Date (Date when these stats of the god were announced/released)
    -  Basic Attack Progression
    -  Basic Attack Damage
    -  Physical Defense
    -  Magical Defense</s>


### Simple example

```JSON
{
"name": "Achilles",
"release date": "27022018",
"pantheon": "Greek",
"role": "Warrior",
"type": "Physical",
"basic attack type": "Melee",
"seasons: {}
}
```
