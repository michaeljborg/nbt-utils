import nbtlib
import json
import os

# NBT files to convert (replace with your own .dat file paths)
nbt_files = [
    'inputs/<PLAYER_UUID>_PARTY.dat',
    'inputs/<PLAYER_UUID>_PC.dat',
]

os.makedirs('outputs', exist_ok=True)

# Function to convert NBT data to a JSON-serializable format
def nbt_to_serializable(obj):
    if isinstance(obj, nbtlib.tag.IntArray):
        return list(obj)
    elif isinstance(obj, nbtlib.tag.List):
        return [nbt_to_serializable(item) for item in obj]
    elif isinstance(obj, nbtlib.tag.Compound):
        return {key: nbt_to_serializable(value) for key, value in obj.items()}
    else:
        return obj

for nbt_file_path in nbt_files:
    # Load and convert NBT data to a dictionary and then to a JSON string
    nbt_file = nbtlib.load(nbt_file_path)
    nbt_dict = nbt_to_serializable(nbt_file)
    json_data = json.dumps(nbt_dict, indent=4)

    # Determine the output file name
    output_file_name = os.path.join('outputs', os.path.basename(nbt_file_path).replace('.dat', '.json'))

    # Open a file to write the JSON data
    with open(output_file_name, 'w') as json_file:
        json_file.write(json_data)

    print(f'JSON data has been written to {output_file_name}')