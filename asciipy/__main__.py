import argparse
from ascii_art import AsciiArt


def main():
    ap = argparse.ArgumentParser(prog="asciipy", description="Convert images into ASCII art.")
    ap.add_argument("-i", "--input", required=True, help="input file")
    ap.add_argument("-c", "--color", action="store_true", help="color/greyscale")
    ap.add_argument("-r", "--resolution", type=int, default=120, help="output resolution")
    ap.add_argument("-t", "--txt", action="store_true", help="save as text")
    ap.add_argument("-o", "--output", default="output.jpg", help="output file")
    args = vars(ap.parse_args())

    pic = AsciiArt(args["input"], args["resolution"])

    if args["txt"]:
        print(str(pic))
        return

    pic.to_image(args["color"]).save(args["output"])

if __name__ == "__main__":
    main()
