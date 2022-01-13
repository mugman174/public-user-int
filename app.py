from pick import pick

guide = "https://github.com/Delitefully/DiscordLists/blob/master/flags.md"

input(f"""
From {guide}
Guide:
| Internal Name              | Description                                       |
|----------------------------|-----------------------------------------|
| STAFF                      | Discord Employee
| PARTNER                    | Discord Partner
| HYPESQUAD                  | HypeSquad Events
| BUG_HUNTER_LEVEL_1         | Bug Hunter Level 1
| HYPESQUAD_ONLINE_HOUSE_1   | HypeSquad Online House Bravery
| HYPESQUAD_ONLINE_HOUSE_2   | HypeSquad Online House Brilliance
| HYPESQUAD_ONLINE_HOUSE_3   | HypeSquad Online House Balance
| PREMIUM_EARLY_SUPPORTER    | Early Supporter
| SYSTEM                     | System User
| BUG_HUNTER_LEVEL_2         | Bug Hunter Level 2
| VERIFIED_DEVELOPER         | Early Verified Bot Developer
| CERTIFIED_MODERATOR        | Discord Certified Moderator
| SPAMMER                    | User is disabled for being a spammer

Press Return to continue...
""")

options = {"STAFF": 1, "PARTNER": 2, "HYPESQUAD": 4, "BUG_HUNTER_LEVEL_1": 8, "HYPESQUAD_ONLINE_HOUSE_1": 64, "HYPESQUAD_ONLINE_HOUSE_2": 128, "HYPESQUAD_ONLINE_HOUSE_3": 256, "PREMIUM_EARLY_SUPPORTER": 512, "SYSTEM": 4096, "BUG_HUNTER_LEVEL_2":16384, "VERIFIED_BOT":65536, "VERIFIED_DEVELOPER": 131072, "CERTIFIED_MODERATOR": 262144, "SPAMMER": 1<<20}

selected = pick(list(options), "Pick which flags to enable (Space to mark, ENTER to submit)", multiselect=True, min_selection_count=1)

print(selected)
flag_num = 0

for sel_flag in selected:
	flag_num += options[sel_flag[0]]

print(flag_num)
