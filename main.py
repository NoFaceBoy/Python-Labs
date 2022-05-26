import models as md


def main() -> None:
    dot = md.Dot("A", 2.5, 12.5, 2)
    rectangle = md.Rectangle("MTKC", 34, 21, 43, 45, 32)
    segment = md.Segment("BC", 3, 4, 5, 4, 5, 6)

    print(dot)
    dot.get_figure_center()
    print(rectangle)
    rectangle.get_figure_center()
    print(segment)
    segment.get_figure_center()


if __name__ == "__main__":
    main()
