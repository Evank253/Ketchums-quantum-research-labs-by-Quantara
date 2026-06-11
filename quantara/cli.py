# Lightweight CLI shim left at original location to preserve scripts that call it.
# Delegates to quantara.cli.main; this file is a MOVE wrapper and not a physics layer.
from quantara.cli.main import main

if __name__ == "__main__":
    main()
