import asyncio
from invoke import task
import sys
sys.path.append('./src')
from overwatch_achievement_exporter import generate_achievement_export


@task
def test(c):
    c.run('pytest')


@task
def update(c):
    asyncio.run(generate_achievement_export())
