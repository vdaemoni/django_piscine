import sys
import os
import settings


def open_template_file(filename):
    try:
        fd = open(filename, 'r')
        template = "".join(fd.readlines())
        fd.close()
        return template
    except IOError:
        os.write(2, b"Error opening template file!\n")
    return None


def write_in_file(filename, text):
    try:
        fd = open(filename, 'w')
        fd.write(text)
        fd.close()
    except IOError:
        os.write(2, b"Error creating html file!\n")


def render_cv():
    if (len(sys.argv) != 2):
        return os.write(2, b"Error: Wrong number of arguments!\n")
    path = sys.argv[1]
    filename, file_extension = os.path.splitext(path)
    if file_extension != ".template":
        return os.write(2, b"Error: Wrong template file extention!\n")
    template = open_template_file(path)
    if template:
        try:
            text = template.format(
                title=settings.title, name=settings.name,
                surname=settings.surname, age=settings.age,
                profession=settings.profession)
            path = filename + ".html"
            write_in_file(path, text)
        except AttributeError:
            os.write(2, b"Error: lack of arguments in template file!\n")
        except KeyError:
            os.write(2, b"Error filling the template!\n")


if __name__ == '__main__':
    render_cv()
