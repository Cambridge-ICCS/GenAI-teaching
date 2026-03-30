---
name: netcdf-processing
description: Use this skill for any operations involving NetCDF (.nc) files, including inspecting metadata, reading variable shapes, extracting data slices, or generating new NetCDF datasets.
---

# What I do

This skill provides guidance for inspecting and generating NetCDF files using
standard command-line utilities. Use these commands to understand dataset
structures before writing extraction scripts.

# When to use this skill

Use this skill whenever a user mentions climate data, multidimensional arrays,
.nc files, or atmospheric datasets.

## Workflow Decision Tree

- **Inspecting Schema**: Use `ncdump -h` first to understand dimensions.
- **Data Access**: If the file is large, only request specific variable slices (don't read entire arrays into context).
- **Creating Files**: Use `ncgen` for small CDL templates or `netCDF4` Python scripts for large datasets.

## Viewing Metadata with `ncdump`
`ncdump` is the standard tool for converting NetCDF binary files into
human-readable text (CDL format).

* **View Header Only (Recommended):** Displays dimensions, variables, and attributes without printing raw data.
    ```bash
    ncdump -h filename.nc
    ```
* **View Specific Variable:** Look at the data for a single variable (e.g., 'temperature').
    ```bash
    ncdump -v temperature filename.nc
    ```
* **Coordinate Formatting:** Use `-c` to see the header plus the values of coordinate variables (lat, lon, time).
    ```bash
    ncdump -c filename.nc
    ```

## Creating Files with `ncgen`
`ncgen` takes a text-based CDL file and compiles it into a binary `.nc` file.

* **Generate Binary from CDL:**
    ```bash
    ncgen -o output_file.nc input_text.cdl
    ```
