def pytest_addoption(parser):
    parser.addoption(
        "--show_diff",
        action="store_true",
        default=False,
        help="Show diff of the scenes in case of a failure",
    )
    parser.addoption(
        "--set_test",
        action="store_true",
        default=False,
        help="Generate control data for the running tests ",
    )

