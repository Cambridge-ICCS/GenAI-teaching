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
def get_variables(path: str) -> str:
    """
    Reads a NetCDF file from the given path and returns its variables.

    Args:
        path: The absolute or relative path to the NetCDF (.nc) file.

    Returns:
        A string representation of the NetCDF file's variables.
    """
    try:
        # Open the dataset
        dset = netCDF4.Dataset(path)

        # Capture the variables as a string to return to the client
        variables_output = ", ".join(dset.variables.keys())

        # Close the dataset to free up resources
        dset.close()

        return variables_output

    except FileNotFoundError:
        return f"Error: Could not find the file at path: {path}"
    except Exception as e:
        return f"Error reading NetCDF file: {str(e)}"


@mcp.tool()
def get_variable_shape(path: str, variable_name: str) -> dict:
    """
    Reads a NetCDF file from the given path and returns the shape of a specific
    variable.

    Args:
        path: The absolute or relative path to the NetCDF (.nc) file.
        variable_name: The name of the variable to get the shape for.

    Returns:
        A dictionary containing the shape of the specified variable.
        Example: {'temperature': (365, 180, 360)}
        Returns an error if the variable is not found.
    """
    pass


if __name__ == "__main__":
    mcp.run()
