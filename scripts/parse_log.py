import re
from datetime import datetime

log_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) .* \[(.*?)\] "(\w+) (.*?) HTTP.*" (\d+) (\d+)'
)

def parse_line(line):
    match = log_pattern.match(line)
    if not match:
        return None

    ip, time_str, method, url, status, size = match.groups()

    time_obj = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")

    return (
        ip,
        time_obj,
        method,
        url,
        int(status),
        int(size)
    )


if __name__ == "__main__":
    with open("data/access.log", "r") as f:
        for line in f:
            result = parse_line(line.strip())
            print(result)