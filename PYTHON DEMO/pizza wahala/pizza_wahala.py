def get_slices_per_box(pizza_type):
    if type(pizza_type) in [int]:
        raise TypeError	
    if pizza_type == "sapa":
        return 4
    elif pizza_type == "smallmoney":
        return 6
    elif pizza_type == "bigboys":
        return 8
    elif pizza_type == "odogwu":
        return 12
    return 0


def get_price_per_box(pizza_type):
    if pizza_type == "sapa":
        return 1500
    elif pizza_type == "smallmoney":
        return 2500
    elif pizza_type == "bigboys":
        return 3500
    elif pizza_type == "odogwu":
        return 5200
    return 0


def calculate_boxes_needed(guests, slices_per_box):
    return (guests + slices_per_box - 1) // slices_per_box


def calculate_leftover_slices(guests, slices_per_box, boxes):
    return (boxes * slices_per_box) - guests


def calculate_total_cost(boxes, price_per_box):
    return boxes * price_per_box



    