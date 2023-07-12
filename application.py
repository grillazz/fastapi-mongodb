import uvicorn


if __name__ == "__main__":
    uvicorn.run("app_name.main:app", host="0.0.0.0", port=8989, reload=True)
