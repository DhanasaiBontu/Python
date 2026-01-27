def right_pad_lines(lines, width):
    aligned_lines = []
    for line in lines:
        aligned_lines.append(line.rjust(width))
    return aligned_lines
lines = ["Hello", "World"]
width = 10
result = right_pad_lines(lines, width)
for line in result:
    print(line)