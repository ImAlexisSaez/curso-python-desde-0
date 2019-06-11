import re

urls = ["https://pildorasinformaticas.es",
        "ftp://pildorasinformaticas.es",
        "https://pildorasinformaticas.com",
        "ftp://pildorasinformaticas.com"]

[print(url) for url in urls if re.findall("^ftp", url)]
