def solution(sizes):
    maxWidth = 0
    maxHeight = 0

    for size in sizes:
        width, height = size
        maxWidth = max(maxWidth, max(width, height))
        maxHeight = max(maxHeight, min(width, height))

    return maxWidth * maxHeight
