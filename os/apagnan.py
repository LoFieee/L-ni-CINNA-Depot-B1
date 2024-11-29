import nbtlib
import os

# List of block and entity IDs from Minecraft 1.14
minecraft_1_14_ids = [
    "minecraft:barrel", "minecraft:bell", "minecraft:blast_furnace", "minecraft:cartography_table", 
    "minecraft:campfire", "minecraft:composter", "minecraft:fletching_table", "minecraft:grindstone", 
    "minecraft:lantern", "minecraft:lectern", "minecraft:loom", "minecraft:smithing_table", 
    "minecraft:smoker", "minecraft:stonecutter", "minecraft:wandering_trader", "minecraft:trader_llama",
    "minecraft:cat", "minecraft:pillager", "minecraft:ravager", "minecraft:fox"
]

# Function to filter and print out results
def search_mca_file(file_path):
    try:
        # Load the NBT data from the .mca file
        nbt_file = nbtlib.load(file_path)

        # Traverse through the regions, chunks, and entities
        for region in nbt_file["Regions"]:
            for chunk in region["Chunks"]:
                chunk_data = chunk["Level"]

                # Searching blocks (TileEntities) for matching block IDs
                for block in chunk_data["TileEntities"]:
                    block_id = block.get("id")
                    if block_id and block_id in minecraft_1_14_ids:
                        print(f"Found Block: {block_id} at {block.get('x')}, {block.get('y')}, {block.get('z')}")

                # Searching entities for matching entity IDs
                for entity in chunk_data["Entities"]:
                    entity_id = entity.get("id")
                    if entity_id and entity_id in minecraft_1_14_ids:
                        print(f"Found Entity: {entity_id} at {entity.get('x')}, {entity.get('y')}, {entity.get('z')}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Main function to process all MCA files in a folder
def process_mca_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mca"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                search_mca_file(file_path)

# Provide the path to the folder containing your .mca files
folder_path = r"C:\Users\doubo\AppData\Roaming\.minecraft\saves\2\region"
process_mca_files(folder_path)



def apagnan()