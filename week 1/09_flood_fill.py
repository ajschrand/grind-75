# An image is represented by an m x n integer grid `image` 
# where image[i][j] represents the pixel value of the image.

# You are also given three integers `sr`, `sc`, and `color`. 
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel 
# of the same color as the starting pixel, 
# plus any pixels connected 4-directionally to those pixels 
# (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with `color`.

# Return the modified image after performing the flood fill.
from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def is_in_bounds(x, y):
            return (x >= 0 
                    and x <= len(image) - 1
                    and y >= 0
                    and y <= len(image[0]) - 1)
        
        # If the starting pixel is already the same color as the new color,
        # then we don't need to fill anything.
        if image[sr][sc] == color:
            return image
        
        # Remember the color of the original pixel
        # because we should only change the color of the connected pixels
        # that are the same color as the original pixel.
        original_color = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Perform a BFS to fill the connected pixels with the new color.
        q = deque()
        q.append((sr, sc))
        while len(q) > 0:
            # Visit the pixel
            visiting_x, visiting_y = q.popleft()
            # Change the color of the pixel
            image[visiting_x][visiting_y] = color
            
            # Visit the connected pixels
            for direction in directions:
                dx, dy = direction
                new_x, new_y = visiting_x + dx, visiting_y + dy
                if is_in_bounds(new_x, new_y) and image[new_x][new_y] == original_color:
                    q.append((new_x, new_y))
                    
        return image