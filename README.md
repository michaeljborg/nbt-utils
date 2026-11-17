# nbt-utils

Small scripts for inspecting and editing Minecraft NBT `.dat` files.

Requires Python 3 and [nbtlib](https://pypi.org/project/nbtlib/) (`pip install nbtlib`).

Folders: `inputs/` holds original `.dat` files, `outputs/` holds generated JSON/text

1. `view_nbt_as_json.py` – convert `.dat` files to JSON in `outputs/`
2. `modify_and_save_nbt.py` – edit a `.dat` file and save it as `<name>_cleaned.dat`
3. `sort.py` – sort the waystone data by player UID

Each script has placeholder paths (e.g. `inputs/<PLAYER_UUID>.dat`) at the top. Replace them with your own before running.