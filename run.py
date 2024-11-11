from app import create_app

# Create the app instance using the create_app function
app = create_app()

if __name__ == "__main__":
    # Run the app in debug mode for development purposes
    app.run(debug=True, host='0.0.0.0', port=5000)
