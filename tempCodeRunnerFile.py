if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    
    port = int(os.environ.get("PORT", 10000))  # Render  PORT
    app.run(host="0.0.0.0", port=port)   