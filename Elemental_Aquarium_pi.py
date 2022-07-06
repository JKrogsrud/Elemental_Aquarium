#!/usr/bin/env python
import sys
import Aquarium, Cell
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from samplebase import SampleBase
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import random

class PracticeBoard(SampleBase):
    def __init__(self, *args, **kwargs):
        super(PracticeBoard, self).__init__(*args, **kwargs)

    def run(self):

        # Object for control over the LED Matrix
        options = RGBMatrixOptions()

        # The following are all options for control over the LED Matrix, most of these are left as their defaults
        options.hardware_mapping = 'adafruit-hat'
        options.rows = 32
        options.cols = 32
        options.chain_length = 1
        options.parallel = 1
        options.row_address_type = 0
        options.multiplexing = 0
        options.pwm_bits = 11
        options.brightness = 100
        options.pwm_lsb_nanoseconds = 50
        options.led_rgb_sequence = "RGB"
        options.pixel_mapper_config = ""
        options.gpio_slowdown = 4

        # Set the following options for an instance of out matrix
        matrix = RGBMatrix(options=options)

        #  Initialize the canvas
        offset_canvas = matrix.CreateFrameCanvas()

        row = 32
        column = 32
        size = (row, column)

        aquarium = Aquarium.Aquarium(row, column)
        aquarium.populate()
        current_time = time.time()
        next_storm = current_time + float(random.randrange(10, 30))
        lightning_due = False

        while True:
            current_time = time.time()
            # Every so often a thunderstorm drops rain, followed by lightning
            if current_time > next_storm:
                # Rain falls
                aquarium.rain(10)
                next_storm = current_time + float(random.randrange(10, 30))
                next_lightning = current_time + float(random.randrange(2, 3))
                lightning_due = True

            if lightning_due and (current_time > next_lightning):
                lightning_due = False
                aquarium.lightning(10)
                # Flash White on screen

                im = Image.new("RGB", size)
                draw = ImageDraw.Draw(im, None)
                for x in range(0, len(aquarium.grid)):
                    for y in range(0, len(aquarium.grid[0])):
                        draw.point((x, y), (255, 255, 255))
                im = ImageOps.flip(im)
                offset_canvas.SetImage(im, 0, unsafe=False)  # Project the image to the RGB-Matrix
                offset_canvas = matrix.SwapOnVSync(offset_canvas)  # Update the matrix

                time.sleep(0.1)

                im = Image.new("RGB", size)
                draw = ImageDraw.Draw(im, None)
                for x in range(0, len(aquarium.grid)):
                    for y in range(0, len(aquarium.grid[0])):
                        draw.point((x, y), (200, 200, 200))
                im = ImageOps.flip(im)
                offset_canvas.SetImage(im, 0, unsafe=False)  # Project the image to the RGB-Matrix
                offset_canvas = matrix.SwapOnVSync(offset_canvas)  # Update the matrix

                time.sleep(0.1)

                im = Image.new("RGB", size)
                draw = ImageDraw.Draw(im, None)
                for x in range(0, len(aquarium.grid)):
                    for y in range(0, len(aquarium.grid[0])):
                        draw.point((x, y), (255, 255, 255))
                im = ImageOps.flip(im)
                offset_canvas.SetImage(im, 0, unsafe=False)  # Project the image to the RGB-Matrix
                offset_canvas = matrix.SwapOnVSync(offset_canvas)  # Update the matrix
                time.sleep(0.1)

            im = Image.new("RGB", size)
            draw = ImageDraw.Draw(im, None)
            for x in range(0, len(aquarium.grid)):
                for y in range(0, len(aquarium.grid[0])):
                    draw.point((x, y), aquarium.grid[x][y].color)

            im = ImageOps.flip(im)
            offset_canvas.SetImage(im, 0, unsafe=False)  # Project the image to the RGB-Matrix
            offset_canvas = matrix.SwapOnVSync(offset_canvas)  # Update the matrix
            changed = aquarium.step()
            time.sleep(0.2)


# Main
if __name__ == "__main__":
    practice_board = PracticeBoard()
    if (not practice_board.process()):
        practice_board.process()

