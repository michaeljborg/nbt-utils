import json

def read_waystones(file_path, output_file):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
        # The target OwnerUid first number we're looking for
        target_owner = -577769114
        
        # Get the waystones array from the correct path in the JSON structure
        waystones = data.get('data', {}).get('Waystones', [])
        
        # Count matching waystones
        matching_waystones = 0
        waystone_list = []
            
        with open(output_file, 'w') as out:
            out.write(f"Waystones owned by UID starting with {target_owner}\n")
            out.write("-" * 50 + "\n")
            
            for waystone in waystones:
                # Check if waystone has OwnerUid
                if 'OwnerUid' in waystone:
                    # Check if the first number in OwnerUid array matches our target
                    if waystone['OwnerUid'][0] == target_owner:
                        matching_waystones += 1
                        block_pos = waystone.get('BlockPos', ['?', '?', '?'])
                        # Remove quotes from name if present and handle empty names
                        name = waystone.get('NameV2', '""').strip('"')
                        name = name if name else "(Unnamed)"
                        
                        waystone_info = (
                            f"Name: {name}\n"
                            f"Coordinates: X={block_pos[0]}, Y={block_pos[1]}, Z={block_pos[2]}\n"
                            f"World: {waystone.get('World', 'unknown')}\n"
                            f"Origin: {waystone.get('Origin', 'unknown')}\n"
                            f"{'-' * 50}\n"
                        )
                        waystone_list.append(waystone_info)
            
            # Write the total count at the top
            out.write(f"Total waystones found: {matching_waystones}\n")
            out.write("-" * 50 + "\n\n")
            
            # Write all waystone information
            for info in waystone_list:
                out.write(info)
            
            print(f"Results have been written to {output_file}")
            print(f"Total waystones found: {matching_waystones}")
            
    except FileNotFoundError:
        print(f"Error: Could not find the file {file_path}")
    except json.JSONDecodeError:
        print("Error: The file is not valid JSON")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Updated path to be relative to the cobblemon directory
    file_path = "outputs/waystones.json"
    output_file = "outputs/waystone_locations.txt"
    read_waystones(file_path, output_file)
