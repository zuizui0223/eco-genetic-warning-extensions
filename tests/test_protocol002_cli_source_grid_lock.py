import json

import pytest

from eco_genetic_warning_extensions.protocol002_cli import main
from eco_genetic_warning_extensions.protocol002_source_grid import planned_source_grid_lock_artifact


def test_protocol002_cli_writes_source_grid_lock(tmp_path) -> None:
    output = tmp_path / "source_grid_planned_lock.json"
    assert main(["write-source-grid-lock", "--output", str(output)]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == planned_source_grid_lock_artifact()
    assert payload["simulation_result_present"] is False


def test_protocol002_cli_source_grid_lock_stdout(capsys) -> None:
    assert main(["write-source-grid-lock", "--stdout"]) == 0
    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert payload == planned_source_grid_lock_artifact()


def test_protocol002_cli_source_grid_lock_refuses_overwrite_without_force(tmp_path) -> None:
    output = tmp_path / "source_grid_planned_lock.json"
    output.write_text("{}\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        main(["write-source-grid-lock", "--output", str(output)])


def test_protocol002_cli_source_grid_lock_force_overwrites(tmp_path) -> None:
    output = tmp_path / "source_grid_planned_lock.json"
    output.write_text("{}\n", encoding="utf-8")
    assert main(["write-source-grid-lock", "--output", str(output), "--force"]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == planned_source_grid_lock_artifact()
