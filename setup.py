from setuptools import setup

setup(
    name='rat-bot',
    version='1.0.0',
    description='A Telegram bot for remote command and control.',
    author='Ethan Lacerenza',
    scripts=[''],
    install_requires=[
        'requests',
        'python-telegram-bot'
        'logging'
    ],
)