import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

  
    lat_rad1 = math.radians(lat1)
    lon_rad1 = math.radians(lon1)
    lat_rad2 = math.radians(lat2)
    lon_rad2 = math.radians(lon2)

    
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_rad1) * math.cos(lat_rad2) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    
    distance = R * c

    return distance

def main():
    lat1 = float(input("Enter latitude of point 1: "))
    lon1 = float(input("Enter longitude of point 1: "))
    lat2 = float(input("Enter latitude of point 2: "))
    lon2 = float(input("Enter longitude of point 2: "))

    
    distance = calculate_distance(lat1, lon1, lat2, lon2)

    # Print result
    print(f"The distance between the two points is: {distance:.2f} km")



