import json

import pytest

from eco_genetic_warning_extensions.protocol002_cli import main


def test_protocol002_cli_writes_stage0_certificate(tmp_path) -> None:
    output = tmp_path / "stage0.json"
    assert main(["write-stage0", "--output", str(output)]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["stage"] == "Stage 0 — algebraic and implementation certificate"
    assert payload["coordinate_count"] == 15
    assert payload["interpretation"]["simulation_result_present"] is False


def test_protocol002_cli_refuses_to_overwrite_without_force(tmp_path) -> None:
    output = tmp_path / "stage0.json"
    output.write_text("{}\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        main(["write-stage0", "--output", str(output)])


def test_protocol002_cli_force_overwrites_existing_certificate(tmp_path) -> None:
    output = tmp_path / "stage0.json"
    output.write_text("{}\n", encoding="utf-8")
    assert main(["write-stage0", "--output", str(output), "--force"]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["coordinate_count"] == 15


def test_protocol002_cli_can_write_certificate_to_stdout(capsys) -> None:
    assert main(["write-stage0", "--stdout"]) == 0
    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert payload["coordinate_count"] == 15
    assert payload["interpretation"]["simulation_result_present"] is False
