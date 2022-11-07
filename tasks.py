import os
import webbrowser

from invoke import task

@task
def clean_build(c):
    """
    Remove build artifacts
    """
    c.run("rm -fr build/")
    c.run("rm -fr dist/")
    c.run("rm -fr *.egg-info")

@task
def clean(c):
    """
    Remove python file and build artifacts
    """
    clean_build(c)

@task
def release(c):
    """
    Package and upload a release
    """
    clean(c)

    import subject_imagefield
    c.run("python3 setup.py sdist bdist_wheel")
    c.run("twine upload dist/*")
