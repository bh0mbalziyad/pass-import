**Local install**

Alternatively, from git or from a stable version you can do a local install with:
```sh
cd pass-import
python3 setup.py install --user
```

> [!IMPORTANT]  
> For local install you need to:
>
>  1. Set `PASSWORD_STORE_ENABLE_EXTENSIONS` to `true` for the local extension to be enabled.
>  2. Set `PASSWORD_STORE_EXTENSIONS_DIR` to local the install path of python
>
>  Example:
>  ```sh
>  export PASSWORD_STORE_ENABLE_EXTENSIONS=true
>  export PASSWORD_STORE_EXTENSIONS_DIR="$(python -m site --user-site)/usr/lib/password-store/extensions/"
>  ```

## The import Library

One can use pass-import as a python library. Simply import the classes of the password manager you want to import and export. Then use them in a context manager. For instance, to import password from a cvs Lastpass exported file to password-store:

```python
from pass_import.managers.lastpass import LastpassCSV
from pass_import.managers.passwordstore import PasswordStore

with LastpassCSV('lastpass-export.csv') as importer:
    importer.parse()

    with PasswordStore('~/.password-store') as exporter:
        exporter.data = importer.data
        exporter.clean(True, True)
        for entry in exporter.data:
            exporter.insert(entry)
```
