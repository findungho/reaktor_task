# Module main.
# Description: Create and run the application.
# Author : Dung Ho
# Email: fin.dungho@gmail.com


from application import create_app


# Create an application
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
