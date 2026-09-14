# starting a new project
1. Clone it into place

    cd C:\Personal\ai_capstone_projects
    git clone https://github.com/gopix/convopro-private-chatgpt.git
    cd convopro-private-chatgpt

2. Turn it into a uv project : from inside the folder, with no name argument
    uv init --package

3. Check what uv did to your existing files
    dir
    type pyproject.toml
4. Add the project-convention pieces 
   (matching your other projects : config.py,   main.py, .env/.env.example
5. Add dependencies
    uv add python-dotenv

6. First commit back to GitHub
	git add .
	git commit -m "Scaffold uv project structure"
	git push

7. For adding extra library
   uv add pydantic pydantic-settings
   uv sync