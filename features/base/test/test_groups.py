import pytest
from helper.tests.groups import groups 


@pytest.mark.parametrize(
    "group,user",
    [
        ("root", []),
        ("wheel", [])
    ]
)


def test_groups(client, group, user, non_dev, non_feature_github_action_runner):
     groups(client, group, user)
