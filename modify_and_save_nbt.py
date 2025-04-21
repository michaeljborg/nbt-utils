import nbtlib

# Path to your NBT .dat file
file_path = r'C:\cursor-workspace\cobblemon\dd8ff166-064a-4343-93d3-8baaa48dc9e5.dat'

# Load the NBT file (as a compound)
nbt_data = nbtlib.load(file_path)

# Make sure Box2 exists
if 'Box2' not in nbt_data:
    raise KeyError("Box2 not found in the NBT file.")

box2 = nbt_data['Box2']

# Check if Slot5 exists and delete it
if 'Slot5' in box2:
    print(f"Removing Slot5")
    del box2['Slot5']
else:
    print("Slot5 not found in Box2.")

# Save to a new file
output_path = file_path.replace('.dat', '_cleaned.dat')
nbt_data.save(output_path)
print(f"✅ Cleaned file saved to: {output_path}")