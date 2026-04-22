"""Unit tests for sync_gantt_project.py pure-function logic."""

import pytest
from sync_gantt_project import (
    Task,
    build_phase_color,
    col_to_index,
    header_map_from_row,
    issue_body,
    issue_title,
    normalize,
    phase_slug,
)


# ---------------------------------------------------------------------------
# normalize
# ---------------------------------------------------------------------------

class TestNormalize:
    def test_strips_whitespace(self):
        assert normalize("  hello  ") == "hello"

    def test_lowercases(self):
        assert normalize("HELLO") == "hello"

    def test_removes_accents(self):
        assert normalize("tâche") == "tache"
        assert normalize("Micro-Tâche") == "micro-tache"
        assert normalize("phase") == "phase"

    def test_replaces_special_chars_with_space(self):
        result = normalize("hello@world!")
        assert "@" not in result
        assert "!" not in result

    def test_collapses_multiple_spaces(self):
        result = normalize("hello   world")
        assert result == "hello world"

    def test_empty_string(self):
        assert normalize("") == ""

    def test_hash_preserved(self):
        assert normalize("#18") == "#18"


# ---------------------------------------------------------------------------
# phase_slug
# ---------------------------------------------------------------------------

class TestPhaseSlug:
    def test_basic(self):
        assert phase_slug("Gestion") == "gestion"

    def test_spaces_become_dashes(self):
        slug = phase_slug("Phase Développement")
        assert " " not in slug
        assert slug == "phase-developpement"

    def test_leading_trailing_dashes_removed(self):
        slug = phase_slug("  Phase  ")
        assert not slug.startswith("-")
        assert not slug.endswith("-")

    def test_consecutive_dashes_collapsed(self):
        slug = phase_slug("Phase  --  Test")
        assert "--" not in slug

    def test_max_48_chars(self):
        long_text = "A" * 100
        assert len(phase_slug(long_text)) <= 48

    def test_empty_returns_phase(self):
        assert phase_slug("") == "phase"

    def test_emoji_stripped(self):
        slug = phase_slug("📋 Gestion")
        assert "gestion" in slug


# ---------------------------------------------------------------------------
# col_to_index
# ---------------------------------------------------------------------------

class TestColToIndex:
    def test_a_is_0(self):
        assert col_to_index("A1") == 0

    def test_b_is_1(self):
        assert col_to_index("B2") == 1

    def test_z_is_25(self):
        assert col_to_index("Z1") == 25

    def test_aa_is_26(self):
        assert col_to_index("AA1") == 26

    def test_ab_is_27(self):
        assert col_to_index("AB5") == 27

    def test_c_is_2(self):
        assert col_to_index("C10") == 2


# ---------------------------------------------------------------------------
# header_map_from_row
# ---------------------------------------------------------------------------

class TestHeaderMapFromRow:
    def _make_cells(self, values):
        return {i: v for i, v in enumerate(values)}

    def test_standard_headers(self):
        cells = self._make_cells(["#", "Phase", "Micro tache", "Resp"])
        mapping = header_map_from_row(cells)
        assert mapping["id"] == 0
        assert mapping["phase"] == 1
        assert mapping["microtask"] == 2
        assert mapping["resp"] == 3

    def test_accented_headers(self):
        cells = self._make_cells(["#", "Phase", "Micro-Tâche", "Responsable"])
        mapping = header_map_from_row(cells)
        assert "id" in mapping
        assert "microtask" in mapping
        assert "resp" in mapping

    def test_missing_column_raises(self):
        cells = self._make_cells(["Phase", "Micro tache", "Resp"])  # no id column
        with pytest.raises(RuntimeError, match="Colonnes manquantes"):
            header_map_from_row(cells)

    def test_all_missing_raises(self):
        with pytest.raises(RuntimeError):
            header_map_from_row({})

    def test_alias_owner(self):
        cells = self._make_cells(["#", "Phase", "Task", "Owner"])
        mapping = header_map_from_row(cells)
        assert mapping["resp"] == 3


# ---------------------------------------------------------------------------
# issue_title
# ---------------------------------------------------------------------------

class TestIssueTitle:
    def test_format(self):
        task = Task(raw_id="#18", phase="📋 Gestion", microtask="Créer une issue GitHub par micro-tâche", resp="M1,M2,M3")
        assert issue_title(task) == "#18 - Créer une issue GitHub par micro-tâche"

    def test_simple(self):
        task = Task(raw_id="#1", phase="Dev", microtask="Setup project", resp="Alice")
        assert issue_title(task) == "#1 - Setup project"


# ---------------------------------------------------------------------------
# issue_body
# ---------------------------------------------------------------------------

class TestIssueBody:
    def test_contains_phase(self):
        task = Task(raw_id="#1", phase="📋 Gestion", microtask="Do something", resp="M1")
        body = issue_body(task, "gantt.xlsx")
        assert "📋 Gestion" in body

    def test_contains_resp(self):
        task = Task(raw_id="#1", phase="Dev", microtask="Do something", resp="M1,M2")
        body = issue_body(task, "gantt.xlsx")
        assert "M1,M2" in body

    def test_contains_source(self):
        task = Task(raw_id="#1", phase="Dev", microtask="Do something", resp="Bob")
        body = issue_body(task, "gantt.xlsx")
        assert "gantt.xlsx" in body

    def test_contains_checkboxes(self):
        task = Task(raw_id="#1", phase="Dev", microtask="Do something", resp="Bob")
        body = issue_body(task, "gantt.xlsx")
        assert "- [ ] Développement effectué" in body
        assert "- [ ] Vérification locale faite" in body
        assert "- [ ] PR ouverte avec une description claire" in body

    def test_empty_phase_fallback(self):
        task = Task(raw_id="#1", phase="", microtask="Do something", resp="Bob")
        body = issue_body(task, "gantt.xlsx")
        assert "Phase non précisée" in body

    def test_empty_resp_fallback(self):
        task = Task(raw_id="#1", phase="Dev", microtask="Do something", resp="")
        body = issue_body(task, "gantt.xlsx")
        assert "Non défini" in body


# ---------------------------------------------------------------------------
# build_phase_color
# ---------------------------------------------------------------------------

class TestBuildPhaseColor:
    VALID_HEX = set("0123456789abcdef")

    def test_returns_6_char_hex(self):
        color = build_phase_color("Gestion")
        assert len(color) == 6
        assert all(c in self.VALID_HEX for c in color)

    def test_deterministic(self):
        assert build_phase_color("Dev") == build_phase_color("Dev")

    def test_different_phases_may_differ(self):
        colors = {build_phase_color(f"Phase {i}") for i in range(20)}
        # palette has 8 entries; different phases should spread across them
        assert len(colors) > 1
