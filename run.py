from app import create_app

app = create_app()

print("🔧 Starting the Flask server...")  # Add this line

if __name__ == '__main__':
    app.run(debug=True)
