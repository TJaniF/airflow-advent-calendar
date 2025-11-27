from pathlib import Path
from airflow.plugins_manager import AirflowPlugin
from fastapi import FastAPI
from fastapi.responses import FileResponse
from airflow.models import DagRun
from airflow.utils.state import DagRunState

PLUGIN_DIR = Path(__file__).parent.absolute()
app = FastAPI(title="Advent Calendar Plugin", version="1.0.0")


@app.get("/advent-calendar-widget.js")
async def serve_react_component():
    js_file_path = PLUGIN_DIR / "react-src" / "dist" / "advent-calendar-widget.js"
    
    if not js_file_path.exists():
        return {"error": f"File not found: {js_file_path}"}, 404

    return FileResponse(
        path=str(js_file_path),
        media_type="application/javascript",
        filename="advent-calendar-widget.js",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )


@app.get("/img/{image_name}")
async def serve_image(image_name: str):
    img_path = PLUGIN_DIR / "react-src" / "img" / image_name
    if not img_path.exists():
        return {"error": f"Image not found: {image_name}"}, 404
    return FileResponse(path=str(img_path))


@app.get("/calendar-status")
async def get_calendar_status():
    import json
    
    links_file = PLUGIN_DIR / "react-src" / "links.json"
    links = {}
    if links_file.exists():
        with open(links_file, 'r') as f:
            links = json.load(f)
    
    status = {}
    for day in range(1, 25):
        dag_id = f"day_{day}"
        runs = DagRun.find(dag_id=dag_id, state=DagRunState.SUCCESS) 
        
        status[dag_id] = {
            "day": day,
            "isOpen": len(runs) > 0,
            "text": f"Day {day}",
            "link": links.get(str(day), "")
        }
    return status


@app.get("/")
async def root():
    return {
        "message": "🎄 Advent Calendar Plugin",
        "type": "react_app",
        "component_url": "/advent-calendar-plugin/advent-calendar-widget.js",
        "description": "Advent Calendar with 24 windows linked to DAGs",
    }


class AdventCalendarPlugin(AirflowPlugin):

    name = "advent_calendar_plugin"

    fastapi_apps = [
        {"app": app, "url_prefix": "/advent-calendar-plugin", "name": "Advent Calendar Plugin"}
    ]

    react_apps = [
        {
            "name": "Advent Calendar",
            "bundle_url": "/advent-calendar-plugin/advent-calendar-widget.js",
            "destination": "nav",
            "category": "browse",
            "url_route": "advent-calendar",
        }
    ]
