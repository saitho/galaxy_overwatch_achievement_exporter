import asyncio
from invoke import task
import sys
sys.path.append('./OverwatchAchievementExporter')
from exporter import Exporter


@task
def test(c):
    c.run('pytest')


@task
def update(c):
    asyncio.run(Exporter().generate_achievement_export())
