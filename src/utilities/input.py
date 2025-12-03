"""Utility File for reading Advent of Code Input Data"""
import os
from pathlib import Path
import requests
from dotenv import load_dotenv

from utilities.grid import Grid

load_dotenv()

def fetch_input(year: int, day: int, session_token: str) -> str:
    """Fetches input data from Advent of Code website"""
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {'Cookie': f'session={session_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text.strip()


def _get_input_file(year: int, day: int, demo: bool = False) -> Path:
    """Returns the Path to the input file for a given day/year"""
    filename = f"day{day}{'demo' if demo else ''}.txt"
    file_path = Path(f"{year}/inputs") / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return file_path


def _read_or_fetch(year: int, day: int, demo: bool = False) -> str:
    """Reads the input file if it exists, otherwise fetches it"""
    file_path = _get_input_file(year, day, demo)

    if file_path.exists():
        return file_path.read_text(encoding="utf-8").strip()
    
    if demo:
        raise FileNotFoundError(f"Demo input file not found: {file_path}")

    session_token = os.getenv("SESSION_COOKIE")
    if not session_token:
        raise ValueError("SESSION_COOKIE not found in environment")

    try:
        input_data = fetch_input(year, day, session_token)
        file_path.write_text(input_data, encoding="utf-8")
        return input_data
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Failed to fetch input data: {e}") from e


def read_line(year: int, day: int, demo: bool = False) -> str:
    """Reads input as a single line"""
    return _read_or_fetch(year, day, demo)


def read_lines(year: int, day: int, demo: bool = False) -> list[str]:
    """Reads input as a list of lines"""
    return _read_or_fetch(year, day, demo).splitlines()


def read_grid(year: int, day: int, demo: bool = False) -> Grid:
    """Reads input as a grid of characters"""
    return Grid([list(line) for line in read_lines(year, day, demo)])