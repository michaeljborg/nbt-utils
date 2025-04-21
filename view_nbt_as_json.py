import nbtlib
import json
import os

# NBT files
nbt_files = [
    #'C:\\cursor-workspace\\cobblemon\\inputs\\0551caec-10fa-4656-814c-2bf8dec6e792_M-PARTY.dat',
    #'C:\\cursor-workspace\\cobblemon\\inputs\\0551caec-10fa-4656-814c-2bf8dec6e792_M-PC.dat',
    #'C:\\cursor-workspace\\cobblemon\\inputs\\dd8ff166-064a-4343-93d3-8baaa48dc9e5_N-PARTY.dat',
    #'C:\\cursor-workspace\\cobblemon\\inputs\\dd8ff166-064a-4343-93d3-8baaa48dc9e5_N-PC.dat',
    #'C:\\cursor-workspace\\cobblemon\\inputs\\0cb67792-53d6-4fde-a10f-70ad0719792e_G-PARTY.dat',
    #'C:\\cursor-workspace\\cobblemon\\inputs\\0cb67792-53d6-4fde-a10f-70ad0719792e_G-PC.dat',
    #'C:\\cursor-workspace\\cobblemon\\inputs\\dd8ff166-064a-4343-93d3-8baaa48dc9e5_N-PC-FIXED.dat'
    'C:\\cursor-workspace\\cobblemon\\inputs\\dd8ff166-064a-4343-93d3-8baaa48dc9e5 (1).dat',
    'C:\\cursor-workspace\\cobblemon\\inputs\\dd8ff166-064a-4343-93d3-8baaa48dc9e5_cleaned.dat'
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
    output_file_name = os.path.join('outputs', nbt_file_path.split('\\')[-1].replace('.dat', '.json'))

    # Open a file to write the JSON data
    with open(output_file_name, 'w') as json_file:
        json_file.write(json_data)

    print(f'JSON data has been written to {output_file_name}')