import nox

locations = "src", "noxfile.py"  # , "tests"
nox.options.sessions = "lint", "tests"


@nox.session(python=["3.8", "3.7"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8",
                    # "flake8-bandit",  # identify security issues
                    "flake8-black",
                    "flake8-bugbear",
                    "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python='3.8')
def docs(session) -> None:
    """Build documentations"""
    session.install("sphinx")
    session.run("sphinx-build", "docs", "docs/_build")

# def install_with_constraints(session, *args, **kwargs):
#     with tempfile.NameTemporaryFile() as requirements:
#         session.run(
#             "poetry",
#             "export",
#             "--dev",
#             "--format=requirements.txt",
#             f"--output={requirements.name}",
#             external=True,
#         )
#         session.install(f"--constraint={requirements.name}", *args, **kwargs)


# @nox.session(python='3.8')
# def mypy(session):
#     args = session.posargs or locations
#     install_with_constraints(session, "mypy")
#     session.run("mypy", *args)