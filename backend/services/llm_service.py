from ollama import Client

class LLMService:
    def __init__(self, host: str = "http://localhost:11434", model: str = "mistral"):
        self.client = Client(host=host)
        self.model = model

    def generate_game_code(self, prompt: str) -> str:
        """Generate HTML5 game code using Phaser 3"""
        system_prompt = """You are an expert HTML5 game developer. Generate complete, runnable HTML5 game code using Phaser 3.
        The code must include HTML structure, Phaser 3 configuration, preload/create/update functions, sprites, physics, and input handling.
        Return ONLY valid HTML code that can be saved and run directly in a browser."""
        response = self.client.generate(model=self.model, prompt=prompt, system=system_prompt, stream=False)
        return response['response']

    def generate_sprite_description(self, description: str) -> str:
        """Generate detailed sprite specifications"""
        system_prompt = """Generate detailed sprite specifications including size, color palette, animation frames.
        Format as JSON for parsing."""
        response = self.client.generate(model=self.model, prompt=description, system=system_prompt, stream=False)
        return response['response']

    def refine_code(self, code: str, instruction: str) -> str:
        """Refine existing game code based on user instructions"""
        system_prompt = """Modify the provided game code according to instructions. Return ONLY complete updated HTML code."""
        prompt = f"Current code:\n{code}\n\nInstruction: {instruction}"
        response = self.client.generate(model=self.model, prompt=prompt, system=system_prompt, stream=False)
        return response['response']