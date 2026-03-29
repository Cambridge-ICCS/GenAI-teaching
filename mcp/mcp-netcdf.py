# /// script
# dependencies = [
#   "netCDF4",
#   "fastmcp",
# ]
# ///

import netCDF4
from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("nc-mcp")


@mcp.tool()
def get_netcdf_variables(path: str) -> str:
    """
    Reads a NetCDF file from the given path and returns its variables.

    Args:
        path: The absolute or relative path to the NetCDF (.nc) file.
    """
    try:
        # Open the dataset
        dset = netCDF4.Dataset(path)

        # Capture the variables as a string to return to the client
        variables_output = str(dset.variables)

        # Close the dataset to free up resources
        dset.close()

        return variables_output

    except FileNotFoundError:
        return f"Error: Could not find the file at path: {path}"
    except Exception as e:
        return f"Error reading NetCDF file: {str(e)}"


if __name__ == "__main__":
    # Run the server via stdio
    mcp.run()
