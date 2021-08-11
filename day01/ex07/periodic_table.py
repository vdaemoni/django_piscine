def parse_line(line):
    el = line.split("=")
    result = dict((value.strip().split(":") for value in el[1].split(", ")))
    result["name"] = el[0].strip()
    print(result)
    return result


def html_declaration():
    HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>periodic_table</title>
  <style>
    table{{
      border-collapse: collapse;
    }}
    h4 {{
      text-align: center;
    }}
    ul {{
      list-style:none;
      padding-left:0px;
    }}
  </style>
</head>
<body>
  <table>
    {body}
  </table>
</body>
</html>
"""

    TEMPLATE = """
      <td style="border: 1px solid black; padding:10px">
        <h4>{name}</h4>
        <ul>
          <li>No {number}</li>
          <li>{small}</li>
          <li>{molar}</li>
          <li>{electron} electron</li>
        </ul>
      </td>
"""

    return (HTML, TEMPLATE)

def main():
    HTML, TEMPLATE = html_declaration()
    body = "<tr>"

    fd = open("periodic_table.txt", "r")
    for line in fd.readlines():
        periodic_table = parse_line(line)
    fd.close()
    position = 0
    for item in periodic_table:
        if position > int(item["position"]):
            body += "    </tr>\n    <tr>"
            position = 0
        for _ in range(position, int(item["position"]) - 1):
            body += "      <td></td>\n"
        position = int(item["position"])
        body += TEMPLATE.format(
            name=item["name"],
            number=item["number"],
            small=item["small"],
            molar=item["molar"],
            electron=item["electron"],
        )
    body += "    </tr>\n"
    fd = open("periodic_table.html", "w")
    fd.write(HTML.format(body=body))
    fd.close()

if __name__ == '__main__':
    main()
