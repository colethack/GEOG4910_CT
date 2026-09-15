def acre_per_1000(places_shp, places_join_field, pop_csv, pop_join_field, parks_shp, selected_place, acreage_field):
    import arcpy
    
    # Join census place population standalone table with census place shapefile
    arcpy.management.AddJoin(places_shp, places_join_field, pop_csv, pop_join_field)
    
    # Create new shapefile from selected census place
    where_clause = f"{places_join_field} = '{selected_place}'"
    sel_place_shp = arcpy.analysis.Select(places_shp, 'Selected_Place', where_clause)
    
    # Clip parks shapefile to the selected place shapefile
    selected_parks = arcpy.analysis.Clip(parks_shp, sel_place_shp, 'Selected_Parks')
    
    # Sum park acreage in selected census place
    total_acres = 0.0
    with arcpy.da.SearchCursor(selected_parks, acreage_field) as cursor:
        for row in cursor:
            total_acres += row[0]
    
    # Divide population of selected place by 1000
    with arcpy.da.SearchCursor(sel_place_shp, ['UtahCens_3']) as pop_cursor:
        population = next(pop_cursor)[0]
        pop1000 = int(population) / 1000
    
    # Return park acreage in selected place per 1000 people in selected place
    return total_acres / pop1000

def reset():
    import arcpy
    
    # Delete 'Selected_Place' and 'Selected Parks' shapefiles that are created after running acre_per_1000
    arcpy.management.Delete('Selected_Place')
    arcpy.management.Delete('Selected_Parks')
    
    # Remove join between census place population standalone table and census place shapefile created after running acre_per_1000
    arcpy.management.RemoveJoin('CensusPlaces2020')
    
    # Return the string 'Compelete' to indicate that the reset tool has ran successfully
    return 'Complete'
