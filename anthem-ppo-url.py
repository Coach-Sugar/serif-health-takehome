import ijson
from datetime import datetime

def parse_json(json_file):
    """Parse through json file iteratively

    Args:
        json_file (.json): json file to be parsed
    """
    
    # Open json file to be read in binary format.
    with open(json_file, 'rb') as input:
        
        # Create ijson parser.
        parser = ijson.parse(input)
        
        # Create output file.
        with open("NY_PPO_URL_LIST.txt","w") as writer:
            # Loop through json file.
            for prefix, event, value in parser:
                # Save the most recent item description.
                if prefix=='reporting_structure.item.in_network_files.item.description':
                    description=value
                # Write the MRF URL for all New York PPO plans to a txt file.
                if prefix=='reporting_structure.item.in_network_files.item.location' and 'New York - PPO' in description:
                    writer.write(f"{value}\n")
        # Close the output file.
        writer.close()

# Get start time.
start_time=datetime.now()

# Table of Contents file.
toc='2024-01-01_anthem_index.json'

# Start streaming unzipped json file
parse_json(toc)

# Output run time.
print(datetime.now() - start_time)