from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import ollama
import json

app = FastAPI(title="Game AI Generator API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Ollama client
client = ollama.Client(host='http://localhost:11434')

@app.get("/")
def read_root():
    return {"message": "Game AI Generator API is running"}

@app.post("/api/generate-game")
async def generate_game(prompt: str):
    """
    Generate HTML5 game code from a text prompt using Ollama
    """
    try:
        # Create a detailed system prompt for game generation
        system_prompt = """You are an expert game developer. Generate complete HTML5 game code based on user prompts.\nThe code should include:\n1. HTML5 canvas setup\n2. JavaScript game logic with Phaser 3 framework\n3. CSS styling\n4. Complete, runnable code\n\nFormat the response as valid JSON with 'html', 'css', and 'javascript' keys."""

        response = client.generate(
            model='mistral',  # or 'llama2'
            prompt=f"Generate a game: {prompt}",
            system=system_prompt,
            stream=False
        )
        
        return {
            "status": "success",
            "prompt": prompt,
            "code": response['response']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-assets")
async def generate_assets(description: str):
    """
    Generate sprite sheet asset descriptions using Ollama
    """
    try:
        response = client.generate(
            model='mistral',
            prompt=f"Generate sprite sheet specifications for: {description}",
            stream=False
        )
        
        return {
            "status": "success",
            "description": description,
            "assets": response['response']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/edit-game")
async def edit_game(current_code: str, edit_prompt: str):
    """
    Edit existing game code based on user instructions
    """
    try:
        response = client.generate(
            model='mistral',
            prompt=f"Current game code:\n{current_code}\n\nEdit request: {edit_prompt}\n\nProvide the updated complete code.",
            stream=False
        )
        
        return {
            "status": "success",
            "updated_code": response['response']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)