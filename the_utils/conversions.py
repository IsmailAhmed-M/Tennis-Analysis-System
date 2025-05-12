# Convert a distance in pixels to meters using a known reference height
def convert_pixel_distance_to_meters(pixel_distance, refrence_height_in_meters, refrence_height_in_pixels):

    return (pixel_distance * refrence_height_in_meters) / refrence_height_in_pixels

# Convert a distance in meters to pixels using a known reference height
def convert_meters_to_pixel_distance(meters, refrence_height_in_meters, refrence_height_in_pixels):
    # multiplying by reference_pixels converts it to pixel units
    return (meters * refrence_height_in_pixels) / refrence_height_in_meters