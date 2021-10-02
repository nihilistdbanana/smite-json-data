# Contributing

To contribute to this repository, 
read about submitting a pull request in the 
DigitalOcean tutorial "[How To Create a Pull Request on GitHub](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github)" 
and then follow the following steps:

1. Read the [`README.md`](https://github.com/nihilistdbanana/smite-json-data#readme)
2. Check out [`Issues`](https://github.com/nihilistdbanana/smite-json-data/issues)
3. Pick an issue you would like to work on.If you cant find one, raise an issue that you see and would like to contribute towards.
4. Make a fork of this repo.
5. Commit the changes you think solve the issue you picked.
    - Make sure you follow the guidelines
    - Take care that your file does not have any field null or empty.<br>
      _( You can test using [`check_missing_data.py`](https://github.com/nihilistdbanana/smite-json-data/blob/master/_status_tools/check_missing_data.py) if you are doubtful.<br>
        We wont hold it against you if you don't. )_
7. Make sure your remote (github repo) is up to date with the changes. 
8. Create the pull request




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
