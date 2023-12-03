from app import app

if __name__ == "__main__":

    # Load configuration environment
    app.config.from_object("config.ProductionConfig")
    
    app.run()