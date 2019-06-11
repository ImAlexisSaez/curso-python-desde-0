import re

urls = ["https://pildorasinformaticas.es",
        "ftp://pildorasinformaticas.es",
        "https://pildorasinformaticas.com",
        "ftp://pildorasinformaticas.com",
        "https://informaticaenespaña.es"]

[print(url) for url in urls if re.findall("[ñ]", url)]
