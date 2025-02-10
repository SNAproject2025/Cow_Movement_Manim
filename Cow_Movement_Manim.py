from manim import *
import numpy as np
import json


class CowsMovement(Scene):
    def construct(self):
        json_file = "TimeStampCowCoordinates.json"
        with open(json_file, 'r') as f:
            timestampCowCoordinates = json.load(f)

        # Convert timestamps to sorted list (ensure they are integers)
        timestamps = sorted(map(float, timestampCowCoordinates.keys()))

        # Get unique indexes from the dataset
        # Each timestamp was assured to have 10 indexes in the notebook, to represent the 10 tracked cows
        num_ids = len(timestampCowCoordinates[str(timestamps[0])])

        # Find min and max values of x and y across all timestamps
        all_x, all_y = [], []
        for positions in timestampCowCoordinates.values():
            for pos in positions:
                if pos is not None:
                    all_x.append(pos[0])
                    all_y.append(pos[1])

        # Compute min and max
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)

        # Define Manim coordinate limits
        manim_x_range, manim_y_range = (-6, 6), (-3.5, 3.5)

        # Function to normalize the coordinates to match manim display boundaries
        def normalize_coord(x, y):
            norm_x = np.interp(x, [min_x, max_x], manim_x_range)
            norm_y = np.interp(y, [min_y, max_y], manim_y_range)
            return norm_x, norm_y

        # Add Barn Boundary (Rectangle)
        barn_boundary = Rectangle(
            width=manim_x_range[1] - manim_x_range[0],
            height=manim_y_range[1] - manim_y_range[0],
            stroke_color=WHITE,
            stroke_width=4
        )
        self.add(barn_boundary)  # Add the barn outline before cows

        # Get starting coordinates
        startingCoordinates = timestampCowCoordinates[str(timestamps[0])]
        last_known_positions = {
            i: normalize_coord(startingCoordinates[i][0], startingCoordinates[i][1])
            if startingCoordinates[i] is not None else (0, 0)
            for i in range(num_ids)
        }

        # Create Cow dots with id (number) labels
        cow_groups = []
        for i in range(num_ids):
            dot = Dot(
                point=np.array([last_known_positions[i][0], last_known_positions[i][1], 0]),
                color=WHITE
            )
            label = Text(str(i + 1), font_size=14).next_to(dot, UP, buff=0.1)
            group = VGroup(dot, label)
            cow_groups.append(group)
            self.add(group)

        # Animate movement over timestamps
        for i in range(len(timestamps) - 1):
            t1, t2 = str(timestamps[i]), str(timestamps[i + 1])

            # Get new positions
            new_positions = timestampCowCoordinates[t2]

            # Create animations
            animations = []
            for idx, group in enumerate(cow_groups):
                if new_positions[idx] is not None and not np.isnan(new_positions[idx][0]):
                    new_x, new_y, _ = new_positions[idx]
                    new_x, new_y = normalize_coord(new_x, new_y)
                    last_known_positions[idx] = (new_x, new_y)
                    animations.append(group.animate.move_to(np.array([new_x, new_y, 0])).set_rate_func(linear))
                    self.add(group)
                else:
                    self.remove(group)

            if len(animations) >= 1:
                # Animate movement over 1 second (smooth transition)
                self.play(*animations, run_time=1, rate_func=linear)

        self.wait(2)


