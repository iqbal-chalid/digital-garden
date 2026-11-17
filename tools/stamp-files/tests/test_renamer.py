from datetime import date
from pathlib import Path

from stamp_files.renamer import stamp_paths

TEST_DATE = date(2026, 11, 17)


def test_stamp_single_file(tmp_path: Path):
    source = tmp_path / "hello.txt"
    source.write_text("Hello")

    stamp_paths([source], today=TEST_DATE)

    assert (tmp_path / "261117_hello.txt").exists()


def test_skip_existing_prefix(tmp_path: Path):
    source = tmp_path / "261110_report.pdf"
    source.write_text("Report")

    stamp_paths([source], today=TEST_DATE)

    assert source.exists()
    assert not (tmp_path / "261117_report.pdf").exists()


def test_update_existing_prefix(tmp_path: Path):
    source = tmp_path / "261110_report.pdf"
    source.write_text("Report")

    stamp_paths([source], update=True, today=TEST_DATE)

    assert (tmp_path / "261117_report.pdf").exists()


def test_folder_is_not_recursive(tmp_path: Path):
    folder = tmp_path / "documents"
    nested = folder / "nested"
    nested.mkdir(parents=True)

    (folder / "hello.txt").write_text("Hello")
    (nested / "inside.txt").write_text("Inside")

    stamp_paths([folder], today=TEST_DATE)

    assert (folder / "261117_hello.txt").exists()
    assert (nested / "inside.txt").exists()


def test_dry_run_does_not_rename(tmp_path: Path):
    source = tmp_path / "hello.txt"
    source.write_text("Hello")

    stamp_paths([source], dry_run=True, today=TEST_DATE)

    assert source.exists()
    assert not (tmp_path / "261117_hello.txt").exists()


def test_collision_does_not_overwrite(tmp_path: Path):
    source = tmp_path / "hello.txt"
    destination = tmp_path / "261117_hello.txt"

    source.write_text("Original")
    destination.write_text("Existing")

    stamp_paths([source], today=TEST_DATE)

    assert source.exists()
    assert destination.read_text() == "Existing"
