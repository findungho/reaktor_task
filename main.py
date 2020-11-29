# Module main.
# Description: Create and run the application.
# Author : Dung Ho
# Email: fin.dungho@gmail.com

import os
from application import create_app


# Create an application
app = create_app()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
