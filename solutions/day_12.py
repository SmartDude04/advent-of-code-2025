import io

def part_1(f: io.TextIOWrapper) -> int:
    # This is way easier than it looks...
    # Since each piece is 3x3 and because the input is quite (very, actually) nice, we can just check
    # if each piece has the area to fit. Yep, that's all

    *shapes, regions = f.read().strip().split("\n\n")
    
    shape_sizes = [sum(char == "#" for char in shape) for shape in shapes]
    
    fitting_regions = 0
    for region in regions.split("\n"):
        width, height, *nums = map(int, region.replace("x", " ").replace(": ", " ").split(" "))
        if width * height >= sum(n * size for n, size in zip(nums, shape_sizes)):
            fitting_regions += 1
    return fitting_regions
            