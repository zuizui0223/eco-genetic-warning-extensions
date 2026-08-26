from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = (ROOT / "manuscript" / "main_text.md").read_text(encoding="utf-8")
REFS = (ROOT / "manuscript" / "references.md").read_text(encoding="utf-8")


def test_abstract_retains_state_defined_synthesis_and_new_boundary() -> None:
    assert "Natural-data tests then separated informative partial states, missing process coordinates, inadequate proxies" in MAIN
    assert "representations that erased mechanistic weighting" in MAIN
    assert "Future-relevant state inference requires joint representation" in MAIN


def test_oenothera_is_mating_state_not_direct_function() -> None:
    assert "Spatial mating opportunity remained after pollinator treatment in *Oenothera*" in MAIN
    assert "20.93%" in MAIN
    assert "p=0.00130" in MAIN
    assert "This is a mating-state result, not a direct functional-loss result" in MAIN
    assert "10.1111/mec.14115" in REFS


def test_eschscholzia_preserves_preregistered_nonidentifiability() -> None:
    assert "A plausible pollinator proxy did not earn general state status in *Eschscholzia*" in MAIN
    assert "multi_endpoint_not_identifiable" in MAIN
    assert "Fallow ground" in MAIN
    assert "Fallow graound" in MAIN
    assert "post hoc typo repair was prohibited" in MAIN
    assert "process_state_not_predictively_supported" in MAIN


def test_empirical_gate_requires_measurement_and_representation_adequacy() -> None:
    assert "measurement adequacy -> representation/information preservation -> residual origin/history test" in MAIN
    assert "cannot simply be assumed to constitute an effective-interaction state" in MAIN
    assert "Pan traps are treated as an array-level pollinator availability/community proxy" in MAIN
    assert "Only a candidate state that is endpoint-informative and remains distinguishable after preprocessing" in MAIN


def test_campanula_records_representation_failure_not_efficiency_irrelevance() -> None:
    assert "Mechanistic weighting was erased by the declared *Campanula* representation" in MAIN
    assert "no_interaction_representation_supported" in MAIN
    assert "constant positive rescalings" in MAIN
    assert "8.88e-16" in MAIN
    assert "representation/information-preservation failure" in MAIN
    assert "not evidence that per-visit efficiency is biologically irrelevant" in MAIN
    assert "10.1098/rspb.2018.0635" in REFS


def test_eschscholzia_eidc_sources_are_cited() -> None:
    for doi in (
        "10.5285/7b721c07-bc38-4815-8669-4675867663d0",
        "10.5285/01906784-6742-44bf-b244-a4b63bed8d82",
        "10.5285/5b400b69-b828-45e8-b04e-7ccbfdb0987f",
        "10.5285/8caf2d8a-564d-4f2e-a797-174165a83796",
    ):
        assert doi in REFS
