import json

import pytest

from eco_genetic_warning_extensions.protocol002_cli import main
from eco_genetic_warning_extensions.protocol002_source_example import example_source_skeleton_artifact


def test_protocol002_cli_writes_source_skeleton_example(tmp_path) -> None:
    output = tmp_path / "source_skeleton_example.json"
    assert main(["write-source-skeleton-example", "--output", str(output)]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == example_source_skeleton_artifact()
    assert payload["simulation_result_present"] is False


def test_protocol002_cli_source_skeleton_example_stdout(capsys) -> None:
    assert main(["write-source-skeleton-example", "--stdout"]) == 0
    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert payload == example_source_skeleton_artifact()


def test_protocol002_cli_source_skeleton_example_refuses_overwrite_without_force(tmp_path) -> None:
    output = tmp_path / "source_skeleton_example.json"
    output.write_text("{}\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        main(["write-source-skeleton-example", "--output", str(output)])


def test_protocol002_cli_source_skeleton_example_force_overwrites(tmp_path) -> None:
    output = tmp_path / "source_skeleton_example.json"
    output.write_text("{}\n", encoding="utf-8")
    assert main(["write-source-skeleton-example", "--output", str(output), "--force"]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == example_source_skeleton_artifact()
