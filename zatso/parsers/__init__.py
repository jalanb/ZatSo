import importlib

from pysyte.types.paths import path


def make_parse_function(module):
    def parse_function(filename):
        parser = Parser()
        p = path(filename)
        return parser.parse(p.text(), filename=filename)

    Parser = getattr(module, 'Parser')
    return parse_function


def on_import():
    here = path(__file__).parent
    there = here.parent / "tatsu/parsers"
    result = []
    for source in there.files("*.py"):
        if source.name == "__init__.py":
            continue
        module_name = source.stem_name
        module_path = f"..tatsu.parsers.{module_name}"
        module = importlib.import_module(module_path, package="zatso.parsers")
        try:
            parse_function = make_parse_function(module)
        except AttributeError:
            continue
        globals()[module_name] = parse_function
        result.append(module_name)
    return result

__all__ = on_import()
