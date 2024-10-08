from pass_import.managers.bitwarden import BitwardenJSON
from pass_import.managers.passwordstore import PasswordStore


with BitwardenJSON('bitwarden.json') as importer:
    importer.parse()
    with PasswordStore("/Users/radical/.password-store") as exporter:
        exporter.data = importer.data
        exporter.clean(True, True)
        for entry in exporter.data:
            exporter.insert(entry)
