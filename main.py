from format_factory import FormatFactory
from argparser import cli_parser
from unification_source_data import unification_source_data


def main():
    factory = FormatFactory()

    # load source dicts
    format_to_load = 'json'
    format_json = factory.get_format(format_to_load)
    rooms = format_json.load('rooms.json')
    students = format_json.load('students.json')

    # process initial dicts
    rooms_with_studs = unification_source_data(rooms, students)

    # CLI parser
    format, files = cli_parser()
    serializer = factory.get_format(format)
    for file in files:
        serializer.dump(rooms_with_studs, f'{file}')


if __name__ == "__main__":
    main()
