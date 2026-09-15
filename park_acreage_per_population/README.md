# Purpose

The purpose of this tool is to calculate the acreage of parks per 1000 people living in a selected census place. This information is commonly used to analyze need for additional parks within park and recreation agencies. This tool provides a simple method for calculating this information.

# Data Inputs
## Overview
This tool requires the input of a shapefile containing census place boundaries, a standalone table providing the population of each census place within the census place boundary shapefile, and a shapefile containing parks within state or county that the desired census place is within. Rasters are not supported by this tool. All shapefiles input into the tool should contain only polygons; other shapefiles are not supported.

## Required Fields
This tool requires seven fields. These fields are as follows:
1. `places_shp` - A string indicating the name of a shapefile containing census place names and boundaries within the desired state or county.
2. `places_join_field` - A string indicating the name of the field within `places_shp` that describes the name of the census places.
3. `pop_csv` - A string indicating the name of a standalone table containing the names of census places and their populations. There must be the same number of entries in this table as in the attribute table for `places_shp`. This standalone table should be contained in a .csv file.
4. `pop_join_field` - A string indicating the name of the field within `pop_csv` that describes the name of the census places. Each place name in this standalone table must match a name in the attribute table for `places_shp` exactly. Census data usually appends the classification of a census place to the end of its name. For example, name entries in `pop_csv` may be formatted as "Brigham City city", rather than "Brigham City". The name of the table field indicated here must be formatted in the same way as `places_join_field`.
5. `parks_shp` - A string indicating a shapefile containing the boundaries and acreage of parks within the desired state or county.
6. `selected_place` - A string indicating the name of the desired census place exactly as it appears in the fields associated with `places_join_field` and `pop_join_field`.
7. `acreage_field` - A string indicating the name of the field associated with park acreage within the entry for `parks_shp`.

# Outputs
## Overview
This tool creates one join and produces two output shapefiles onto the current map. Both of these shapefiles are saved within the current project's folder. Lastly, the tool will return the value of park acreage per 1000 people once the tool has finish executing.

## Output Files
This tool creates two output files in the project folder:
1. 'Selected_Place' - A shapefile created when the tool makes a copy of the selected census place polygon to clip the shapefile entered in `parks_shp` to.
2. 'Selected_Parks' - A shapefile created by the tool when the shapefile entered in the `parks_shp` field is clipped to the 'Selected_Place' shapefile.

## Created Join
This tool also creates a join between the shapefile entered in the `places_shp` field and the standalone table entered in the `pop_csv` field. This join should be removed before subsequent execution of the tool, but this can be done through the use of the `reset()` function also present in the script.

## Returned Value
This tool will return the value of park acreage per 1000 people. This value is returned where the tool was executed (usually within a notebook) and is returned as a float value. Once this value is present, the tool has completely finished executing.

## `reset()` function
The two shapefiles created by the `acre_per_1000` function can be deleted with the use of the the `reset()` function. This function requires no input fields. Additionally, the `reset()` function will remove the join created between the shapefile entered in the `places_shp` field and the standalone table entered in the `pop_csv` field. This function is recommended for use after each execution of the `acre_per_1000` function, as multiple joins cannot be exist between these two files at the same time.

# Other Details
## Required Python Libraries or ArcGIS Extensions
This tool requires no additional Python libraries or ArcGIS Extensions. Once the module containing the tool has been imported, no other modules are required. The tool will automatically `import arcpy` before its code is executed. However, the user may need to use `arcpy` outside of the tool's execution to set the workspace folder and overwrite outputs.

## Expected Folder Structure
This tool expects that all required input files are present directly within the project folder or selected workspace, not in any subdirectories.

## Troubleshooting
### Common Errors
1. "ERROR 160090: A persisted domain record with the specified name does not exist." - Indicates that a join already exists between the shapefile entered in the `places_shp` field and the standalone table entered in the `pop_csv` field. This can be resolved by either executing the `reset()` function (which will also delete 'Selected_Parks' and 'Selected_Place' from the project folder) or by manually removing the join.
2. "StopIteration" Error - Indicates that iteration was unable to continue when the tool searched for the string entered in the `selected_place` field. If this occurs, check that the string was spelled correctly and exists within the census place boundary shapefile and census place population standalone table. 
### Unusual Output
An unusually high returned output could indicate that the tool was unable to properly join the shapefile entered in the `places_shp` field with the standalone table entered in the `pop_csv`. If this occurs, check that the correct table field names were entered in the `places_join_field` and `pop_join_field` input fields.
